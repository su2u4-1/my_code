from __future__ import annotations
from random import randint, random
import torch
import torch.nn as nn
import torch.optim as optim
import pickle


# ===============================
# 封裝 class
# ===============================
class StringVectorAI:
    def __init__(self, charset: str, vector_dim: int, weight: tuple[float, float] = (1.0, 0.0)) -> None:
        self.device: torch.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.charset: str = charset
        self.vocab_size: int = len(charset)
        self.char_to_idx: dict[str, int] = {c: i for i, c in enumerate(charset)}
        self.idx_to_char: dict[int, str] = {i: c for i, c in enumerate(charset)}

        self.vector_dim: int = vector_dim
        self.weight: tuple[float, float] = weight  # 額外加減分權重

        # 模型初始化
        hidden_dim: int = 32
        self.model: nn.Module = self._build_model(hidden_dim).to(self.device)
        self.optimizer: torch.optim.Optimizer = optim.Adam(self.model.parameters(), lr=0.01)
        self.loss_fn: nn.Module = nn.MSELoss()

        # 紀錄歷史
        self.records: list[tuple[str, tuple[float, ...]]] = []

    # -------------------------------
    # 模型建構
    # -------------------------------
    def _build_model(self, hidden_dim: int) -> nn.Module:
        class RNNModel(nn.Module):
            def __init__(self, vocab_size: int, hidden_dim: int, vector_dim: int) -> None:
                super().__init__()
                self.rnn: nn.GRU = nn.GRU(input_size=vocab_size, hidden_size=hidden_dim, batch_first=True)
                self.fc: nn.Linear = nn.Linear(hidden_dim, vector_dim)

            def forward(self, x: torch.Tensor) -> torch.Tensor:
                _, h = self.rnn(x)
                h = h.squeeze(0)
                return self.fc(h)

        return RNNModel(self.vocab_size, hidden_dim, self.vector_dim)

    # -------------------------------
    # 字串編碼工具
    # -------------------------------
    def _string_to_tensor(self, s: str) -> torch.Tensor:
        if not s:
            # 若字串為空，補一個隨機字元
            s = self.charset[0]  # 或 random 選一個
        tensor: torch.Tensor = torch.zeros(len(s), self.vocab_size, device=self.device)
        for i, c in enumerate(s):
            tensor[i, self.char_to_idx[c]] = 1.0
        return tensor

    def _tensor_to_string(self, tensor: torch.Tensor) -> str:
        probs = torch.softmax(tensor, dim=1)
        indices = torch.multinomial(probs, 1).squeeze(1)
        return "".join(self.idx_to_char[idx.item()] for idx in indices)

    # -------------------------------
    # 核心函式 1：猜測向量並更新模型
    # -------------------------------
    def guess_vector(self, input_str: str, target_vec: tuple[float, ...], extra_weight: tuple[float, float] = (1.0, 0.0)) -> float:
        x: torch.Tensor = self._string_to_tensor(input_str).unsqueeze(0)  # (1, seq_len, vocab_size)
        y: torch.Tensor = torch.tensor(target_vec, device=self.device).unsqueeze(0)
        # 額外加減分權重調整 target
        adjusted_y: torch.Tensor = y * extra_weight[0] + y * extra_weight[1]

        self.optimizer.zero_grad()
        pred: torch.Tensor = self.model(x)
        loss: torch.Tensor = self.loss_fn(pred, adjusted_y)
        loss.backward()
        self.optimizer.step()

        # 紀錄
        self.records.append((input_str, tuple(pred.squeeze(0).detach().tolist())))
        return loss.item()

    # -------------------------------
    # 核心函式 2：根據歷史紀錄生成新的向量與字串
    # -------------------------------
    def generate_vector(self) -> tuple[tuple[float, ...], str]:
        if not self.records:
            vec: tuple[float, ...] = tuple(torch.rand(self.vector_dim).tolist())
            s_len: int = max(1, self.vector_dim)
            string: str = "".join(self.charset[i % self.vocab_size] for i in range(s_len))
            return vec, string

        last_str, last_vec = self.records[-1]
        x: torch.Tensor = self._string_to_tensor(last_str).unsqueeze(0)  # shape: (1, seq_len, vocab_size)
        with torch.no_grad():
            pred: torch.Tensor = self.model(x)
        vec: tuple[float, ...] = tuple(pred.squeeze(0).tolist())

        # 修正這裡，加上 squeeze(0) 去掉 batch 維度
        string: str = self._tensor_to_string(x.squeeze(0))

        return vec, string

    # -------------------------------
    # 保存與載入
    # -------------------------------
    def save(self, path_prefix: str) -> None:
        torch.save(self.model.state_dict(), f"{path_prefix}_model.pth")
        with open(f"{path_prefix}_records.pkl", "wb") as f:
            pickle.dump(self.records, f)

    def load(self, path_prefix: str) -> None:
        self.model.load_state_dict(torch.load(f"{path_prefix}_model.pth", map_location=self.device))
        with open(f"{path_prefix}_records.pkl", "rb") as f:
            self.records = pickle.load(f)


ALPHABET = "abcdefghijklmnopqrstuvwxyz "
DIMENSION = 32
ROUNDS = 100000
STEP = 100

if __name__ == "__main__":
    ai1 = StringVectorAI(charset=ALPHABET, vector_dim=DIMENSION)
    ai2 = StringVectorAI(charset=ALPHABET, vector_dim=DIMENSION)

    now_str = "".join(ALPHABET[randint(0, len(ALPHABET) - 1)] for _ in range(DIMENSION))
    now_vector = tuple(random() for _ in range(DIMENSION))
    print(f"'{now_str}'")
    for i in range(ROUNDS):
        # 猜測向量
        loss = ai1.guess_vector(now_str, now_vector, extra_weight=(1.0, 0.0))
        now_vector, now_str = ai1.generate_vector()
        if i % STEP == 0:
            print("a1 Loss:", loss)
            print(f"'{now_str}'")
        # 猜測向量
        loss = ai2.guess_vector("world", now_vector, extra_weight=(1.0, 0.0))
        now_vector, now_str = ai2.generate_vector()
        if i % STEP == 0:
            print("a2 Loss:", loss)
            print(f"'{now_str}'")

    # 根據歷史生成向量與字串
    vec, s = ai1.generate_vector()
    print("Generated vector:", vec)
    print("Generated string:", s)

    # # 保存模型與紀錄
    # ai.save("my_ai")

    # # 載入模型與紀錄
    # ai2 = StringVectorAI(charset="abcdefghijklmnopqrstuvwxyz ", vector_dim=5)
    # ai2.load("my_ai")
    # print("Loaded records:", ai2.records)
