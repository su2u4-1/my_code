from os.path import isfile
from random import randint
from collections import Counter
from math import sqrt

import torch
import torch.nn as nn
import torch.optim as optim
from torch.distributions import Categorical


class SymbolS2SModel(nn.Module):
    def __init__(self, vocab_size: int, embed_dim: int, hidden_dim: int) -> None:
        super().__init__()
        self.vocab_size = vocab_size
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.encoder = nn.GRU(embed_dim, hidden_dim, batch_first=True)
        self.decoder = nn.GRU(embed_dim, hidden_dim, batch_first=True)
        self.fc_out = nn.Linear(hidden_dim, vocab_size)

    def forward(self, input_seq: torch.Tensor, bos_token_id: int, eos_token_id: int, max_length: int) -> tuple[torch.Tensor, list[int]]:
        embedded = self.embedding(input_seq)
        _, hidden = self.encoder(embedded)

        decoder_input = torch.tensor([[bos_token_id]], dtype=torch.long, device=input_seq.device)

        log_probs: list[torch.Tensor] = []
        output_symbols: list[int] = []

        for _ in range(max_length):
            embedded_dec = self.embedding(decoder_input)
            output, hidden = self.decoder(embedded_dec, hidden)
            logits = self.fc_out(output.squeeze(1))

            dist = Categorical(logits=logits)
            action = dist.sample()

            log_probs.append(dist.log_prob(action))  # type: ignore
            token_id = int(action.item())

            if token_id == eos_token_id:
                break

            output_symbols.append(token_id)
            decoder_input = action.unsqueeze(0)

        if len(log_probs) == 0:
            stacked_log_probs = torch.zeros(1, device=input_seq.device, requires_grad=True)
        else:
            stacked_log_probs = torch.cat(log_probs)

        return stacked_log_probs, output_symbols


class SymbolAIEnvironment:
    def __init__(self, vocab_size: int, embed_dim: int = 128, hidden_dim: int = 256, lr: float = 0.001, bos_token_id: int = 0, eos_token_id: int = 1) -> None:
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = SymbolS2SModel(vocab_size, embed_dim, hidden_dim).to(self.device)
        self.optimizer = optim.Adam(self.model.parameters(), lr=lr)
        self.bos_token_id = bos_token_id
        self.eos_token_id = eos_token_id

        self.current_log_probs: dict[int, torch.Tensor] = {}

        # 在初始化時先將梯度清零
        self.optimizer.zero_grad()

    def predict(self, input_list: list[int], max_length: int = 100) -> tuple[list[int], int]:
        self.model.train()
        input_tensor = torch.tensor([input_list], dtype=torch.long, device=self.device)

        log_probs, output_symbols = self.model(input_tensor, self.bos_token_id, self.eos_token_id, max_length)
        self.current_log_probs[id(log_probs)] = log_probs

        return output_symbols, id(log_probs)

    def reward(self, output_id: int, score: float) -> None:
        """
        根據指定的 output_id 計算該輸出路徑的梯度並累積，但不立刻更新模型權重。
        """
        if output_id not in self.current_log_probs:
            raise RuntimeError("在給予評分前，必須先呼叫 predict 產生輸出，或該輸出已被處理過。")

        # 計算對應輸出路徑的 loss
        loss = -self.current_log_probs[output_id].sum() * score

        # 反向傳播以累積梯度 (PyTorch 預設會將梯度加總至 .grad 屬性中)
        loss.backward()  # type: ignore

        # 清除該輸出的暫存，避免重複評分
        del self.current_log_probs[output_id]

    def update(self) -> None:
        """
        在所有 Agent 的 reward 都呼叫完畢後執行，將累積的梯度更新至模型參數中，並重設梯度。
        """
        self.optimizer.step()  # type: ignore
        self.optimizer.zero_grad()

    def save(self, path: str) -> None:
        state = {  # type: ignore
            "model_state_dict": self.model.state_dict(),
            "optimizer_state_dict": self.optimizer.state_dict(),
            "vocab_size": self.model.vocab_size,
            "embed_dim": self.model.embedding.embedding_dim,
            "hidden_dim": self.model.encoder.hidden_size,
            "bos_token_id": self.bos_token_id,
            "eos_token_id": self.eos_token_id,
        }
        torch.save(state, path)  # type: ignore

    def load(self, path: str) -> None:
        if not isfile(path):
            raise FileNotFoundError(f"找不到檔案：{path}")

        state = torch.load(path, map_location=self.device, weights_only=False)

        self.bos_token_id = state["bos_token_id"]
        self.eos_token_id = state["eos_token_id"]
        self.model = SymbolS2SModel(vocab_size=state["vocab_size"], embed_dim=state["embed_dim"], hidden_dim=state["hidden_dim"]).to(self.device)

        self.model.load_state_dict(state["model_state_dict"])
        self.optimizer = optim.Adam(self.model.parameters())
        self.optimizer.load_state_dict(state["optimizer_state_dict"])
        self.current_log_probs = {}
        self.optimizer.zero_grad()


class DynamicRepetitionPenalty:
    """
    動態重複懲罰追蹤器（適用於訓練迴圈）
    使用 dict[int, float] 儲存衰減後的歷史權重，完全相容型別檢查。
    """

    def __init__(self, decay: float = 0.85):
        self.decay = decay
        # 直接使用原生 dict，值為 float，不會有型別衝突
        self.history: dict[int, float] = {}

    def step(self, current_list: list[int]) -> float:
        # 這裡用 Counter 只負責統計當下輸入，不影響 history 的型別
        current_counts = Counter(current_list)

        # ---- 1. 計算懲罰（餘弦相似度） ----
        if not current_list or not self.history:
            penalty = 0.0
        else:
            dot_product = sum(self.history.get(k, 0.0) * v for k, v in current_counts.items())
            norm_hist = sqrt(sum(v**2 for v in self.history.values()))
            norm_curr = sqrt(sum(v**2 for v in current_counts.values()))

            if norm_hist == 0 or norm_curr == 0:
                penalty = 0.0
            else:
                penalty = dot_product / (norm_hist * norm_curr)

        # ---- 2. 重構歷史（衰減 + 疊加當前輸出） ----
        # 2a. 歷史權重乘上衰減
        for key in list(self.history.keys()):
            new_val = self.history[key] * self.decay
            if new_val < 1e-9:
                del self.history[key]
            else:
                self.history[key] = new_val

        # 2b. 加入當前的計數（權重給 1）
        for key, count in current_counts.items():
            self.history[key] = self.history.get(key, 0.0) + count

        return penalty


Symbol = {
    0: "start",
    1: "end",
    2: "empty",
    3: "wall",
    4: "placeholder",
    5: "placeholder",
    6: "placeholder",
    7: "food",
    8: "danger",
    9: "placeholder",
    10: "move_lu",
    11: "move_u",
    12: "move_ru",
    13: "move_r",
    14: "move_rd",
    15: "move_d",
    16: "move_ld",
    17: "move_l",
    18: "p1",
    19: "p2",
    20: "sound_20",
    21: "sound_21",
    22: "sound_22",
    23: "sound_23",
    24: "sound_24",
    25: "sound_25",
    26: "sound_26",
    27: "sound_27",
    28: "sound_28",
    29: "sound_29",
    30: "sound_30",
    31: "sound_31",
    32: "sound_32",
    33: "sound_33",
    34: "sound_34",
    35: "sound_35",
    36: "sound_36",
    37: "sound_37",
    38: "sound_38",
    39: "sound_39",
    40: "sound_40",
    41: "sound_41",
    42: "sound_42",
    43: "sound_43",
    44: "sound_44",
    45: "sound_45",
    46: "sound_46",
    47: "sound_47",
    48: "sound_48",
    49: "sound_49",
}

DIRE = ((-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0))
SIZE = 20

model = SymbolAIEnvironment(50)
if isfile("model.pth"):
    model.load("model.pth")
log: list[str] = []

guid = [[2 for _ in range(SIZE)] for _ in range(SIZE)]
for i in range(SIZE):
    guid[i][0] = 3
    guid[i][SIZE - 1] = 3
    guid[0][i] = 3
    guid[SIZE - 1][i] = 3

p1 = [randint(1, SIZE - 2), randint(1, SIZE - 2)]
p2 = [p1[0] + 1, p1[1] + 1]
guid[p1[0]][p1[1]] = 18
guid[p2[0]][p2[1]] = 19
s1: list[int] = []
s2: list[int] = []
times = 1
d1 = DynamicRepetitionPenalty()
d2 = DynamicRepetitionPenalty()
move = [0, 0, 0, 0, 0, 0, 0, 0]

while True:
    for _ in range(10):
        x, y = randint(1, SIZE - 2), randint(1, SIZE - 2)
        if guid[x][y] == 2:
            guid[x][y] = 7
        x, y = randint(1, SIZE - 2), randint(1, SIZE - 2)
        if guid[x][y] == 7:
            guid[x][y] = 2
        x, y = randint(1, SIZE - 2), randint(1, SIZE - 2)
        if guid[x][y] == 7:
            guid[x][y] = 2

    # P1 預測
    p1_input: list[int] = []
    p1_sound: list[int] = []
    for dx, dy in DIRE:
        t = guid[p1[0] + dx][p1[1] + dy]
        p1_input.append(t)
        if t == 19:
            p1_sound.extend(s2)
    p1_input.extend(p1_sound)
    p1_output, p1_id = model.predict(p1_input)

    # P2 預測
    p2_input: list[int] = []
    p2_sound: list[int] = []
    for dx, dy in DIRE:
        t = guid[p2[0] + dx][p2[1] + dy]
        p2_input.append(t)
        if t == 18:
            p2_sound.extend(s1)
    p2_input.extend(p2_sound)
    p2_output, p2_id = model.predict(p2_input)

    # 計算 P1 與 P2 評分
    p1_eval = 0.0
    p2_eval = 0.0
    if len(p1_output) < 1 or p1_output[0] < 10 or p1_output[0] > 17:
        p1_eval -= 10.0
    if len(p2_output) < 1 or p2_output[0] < 10 or p2_output[0] > 17:
        p2_eval -= 10.0

    if p1_eval == 0.0:
        p1_nx, p1_ny = p1[0] + DIRE[p1_output[0] - 10][0], p1[1] + DIRE[p1_output[0] - 10][1]
        move[p1_output[0] - 10] += 1
        if move[p1_output[0] - 10] > sum(move) / 8:
            p1_eval -= 1.0
        else:
            p1_eval += 3.0
    else:
        p1_nx, p1_ny = p1[0], p1[1]
    if p2_eval == 0.0:
        p2_nx, p2_ny = p2[0] + DIRE[p2_output[0] - 10][0], p2[1] + DIRE[p2_output[0] - 10][1]
        move[p2_output[0] - 10] += 1
        if move[p2_output[0] - 10] > sum(move) / 8:
            p2_eval -= 1.0
        else:
            p2_eval += 3.0
    else:
        p2_nx, p2_ny = p2[0], p2[1]

    if guid[p1_nx][p1_ny] == 7:
        p1_eval += 1.0
    elif guid[p1_nx][p1_ny] == 8:
        p1_eval -= 1.0
    if guid[p2_nx][p2_ny] == 7:
        p2_eval += 1.0
    elif guid[p2_nx][p2_ny] == 8:
        p2_eval -= 1.0

    if guid[p1_nx][p1_ny] == 3:
        p1_eval -= 3.0
    else:
        guid[p1[0]][p1[1]] = 2
        p1 = [p1_nx, p1_ny]
        guid[p1[0]][p1[1]] = 18
    if guid[p2_nx][p2_ny] == 3:
        p2_eval -= 3.0
    else:
        guid[p2[0]][p2[1]] = 2
        p2 = [p2_nx, p2_ny]
        guid[p2[0]][p2[1]] = 19

    if 5 < len(p1_output) < 15:
        p1_eval += 3.0
    elif len(p1_output) <= 5:
        p1_eval -= 3.0
    else:
        p1_eval -= 0.1 * (len(p1_output) - 15)
    if 5 < len(p2_output) < 15:
        p2_eval += 3.0
    elif len(p2_output) <= 5:
        p2_eval -= 3.0
    else:
        p2_eval -= 0.1 * (len(p2_output) - 15)

    s1, s2 = [], []
    for s in p1_output[1:]:
        if s >= 20:
            p1_eval += 0.1
        else:
            p1_eval -= 1.0
        s1.append(s)

    for s in p2_output[1:]:
        if s >= 20:
            p2_eval += 0.1
        else:
            p2_eval -= 1.0
        s2.append(s)

    dd1 = d1.step(p1_output) * 1.2
    dd2 = d2.step(p2_output) * 1.2
    if p1_eval <= 0:
        p1_eval *= 1 + dd1
    else:
        p1_eval *= 1 - dd1
    if p2_eval <= 0:
        p2_eval *= 1 + dd2
    else:
        p2_eval *= 1 - dd2

    # 依據特定的 output_id 分別進行反向傳播，累積梯度
    model.reward(p1_id, p1_eval)
    model.reward(p2_id, p2_eval)
    print(f"p1: {float(p1_eval):.2f}, {dd1:.2f}, ({p1[0]}, {p1[1]}), [{', '.join(Symbol[x] for x in p1_input)}], [{', '.join(Symbol[x] for x in p1_output)}]")
    print(f"p2: {float(p2_eval):.2f}, {dd2:.2f}, ({p2[0]}, {p2[1]}), [{', '.join(Symbol[x] for x in p2_input)}], [{', '.join(Symbol[x] for x in p2_output)}]")
    log.append(f"p1: {float(p1_eval):.2f}, {dd1:.2f}, ({p1[0]}, {p1[1]}), [{', '.join(Symbol[x] for x in p1_input)}], [{', '.join(Symbol[x] for x in p1_output)}]")
    log.append(f"p2: {float(p2_eval):.2f}, {dd2:.2f}, ({p2[0]}, {p2[1]}), [{', '.join(Symbol[x] for x in p2_input)}], [{', '.join(Symbol[x] for x in p2_output)}]")

    # 兩者的梯度都累積完畢後，再統一呼叫 update 更新模型參數
    model.update()

    times -= 1
    if times <= 0:
        s = input("是否要繼續?或再來幾次? ").strip()
        if s.lower() in ("exit", "quit", "n", "x", "no", "q", "stop"):
            break
        elif s.isdigit():
            times = int(s)
            model.save("model.pth")
    else:
        print(f"剩餘 {times} 次")
        if times % 100 == 0:
            model.save("model.pth")

model.save("model.pth")
with open("temp_log.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(log))

"""
Symbol:
    0: start
    1: end
    2: empty
    3: wall
    4: placeholder
    5: placeholder
    6: placeholder
    7: food
    8: danger
    9: placeholder
    10: move left-up
    11: move up
    12: move right-up
    13: move right
    14: move right-down
    15: move down
    16: move left-down
    17: move left
    18: p1
    19: p2
    20~49: sound symbol

memory = [sound * n]
surround = [lu, u, ru, r, rd, d, ld, l]
listen = [sound symbol * n]
input = surround + listen + memory

output = [move_direction, sound, ..., say, sound, ...]
"""
