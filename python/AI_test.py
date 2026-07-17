import random
import torch
import torch.nn as nn
import torch.optim as optim
from torch.distributions import Categorical

# ---------- Hyperparameters ----------
VOCAB_SIZE = 20  # vocabulary size (0 is EOS)
MAX_LEN = 6  # maximum generation length
EMBED_DIM = 32
HIDDEN_DIM = 64
LR = 0.001
BASELINE_ALPHA = 0.9
EPISODES = 100000
PRINT_INTERVAL = 500

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ---------- Environment ----------
colors = ["red", "blue", "green", "yellow"]
shapes = ["circle", "square", "triangle", "star"]
all_items: list[tuple[str, str, torch.Tensor]] = []
for c in colors:
    for s in shapes:
        feat = [0] * 8
        feat[colors.index(c)] = 1
        feat[4 + shapes.index(s)] = 1
        all_items.append((c, s, torch.tensor(feat, dtype=torch.float32)))


def random_pair():
    target = random.choice(all_items)
    distractors = [it for it in all_items if it != target]
    distractor = random.choice(distractors)
    candidates = [target, distractor]
    random.shuffle(candidates)
    return target, candidates


# ---------- Model ----------
class CommunicationModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.embedding = nn.Embedding(VOCAB_SIZE, EMBED_DIM)
        self.encoder = nn.GRU(EMBED_DIM, HIDDEN_DIM, batch_first=True)
        self.decoder = nn.GRU(EMBED_DIM, HIDDEN_DIM, batch_first=True)
        self.speaker_fc = nn.Linear(HIDDEN_DIM, VOCAB_SIZE)
        self.item_fc = nn.Linear(8, HIDDEN_DIM)

    def forward_speaker(self, target_feat: torch.Tensor):
        # initial hidden state from target feature, shape (1,1,H)
        h0 = self.item_fc(target_feat).unsqueeze(0).unsqueeze(0)

        bos_embed = torch.zeros(1, 1, EMBED_DIM, device=target_feat.device)
        decoder_input = bos_embed

        log_probs: list[torch.Tensor] = []
        symbols: list[int] = []

        for _ in range(MAX_LEN):
            output, h0 = self.decoder(decoder_input, h0)
            logits = self.speaker_fc(output.squeeze(1))
            dist = Categorical(logits=logits)
            action = dist.sample()
            t = dist.log_prob(action)  # type: ignore
            if isinstance(t, torch.Tensor):
                log_probs.append(t)
            else:
                raise TypeError(f"Expected torch.Tensor, got {type(t)}")  # type: ignore
            token = action.item()
            if token == 0:  # EOS
                break
            symbols.append(int(token))
            decoder_input = self.embedding(action).unsqueeze(0)

        if log_probs:
            stacked_log_probs = torch.stack(log_probs)
        else:
            stacked_log_probs = torch.zeros(0, device=target_feat.device)
        return symbols, stacked_log_probs

    def forward_listener(self, symbols: list[int], cand_feats: list[torch.Tensor]):
        if not symbols:
            return torch.zeros(2, device=cand_feats[0].device)

        seq_tensor = torch.tensor([symbols], dtype=torch.long, device=cand_feats[0].device)
        embedded = self.embedding(seq_tensor)
        _, hidden = self.encoder(embedded)

        item_h = torch.stack([self.item_fc(f) for f in cand_feats])  # (2, H)
        seq_rep = hidden.squeeze(0).squeeze(0)  # (H,)
        scores = torch.mv(item_h, seq_rep)
        return scores


# ---------- Training ----------
model = CommunicationModel().to(device)
optimizer = optim.Adam(model.parameters(), lr=LR)

baseline = 0.0
log_history: list[str] = []

for episode in range(1, EPISODES + 1):
    target, candidates = random_pair()
    target_feat = target[2]
    cand_feats = [c[2] for c in candidates]

    symbols, speaker_log_probs = model.forward_speaker(target_feat)

    listener_scores = model.forward_listener(symbols, cand_feats)
    listener_probs = torch.softmax(listener_scores, dim=0)
    listener_dist = Categorical(probs=listener_probs)
    listener_action = listener_dist.sample()
    t = listener_dist.log_prob(listener_action)  # type: ignore
    if isinstance(t, torch.Tensor):
        listener_log_prob = t
    else:
        raise TypeError(f"Expected torch.Tensor, got {type(t)}")  # type: ignore

    target_idx = [i for i, c in enumerate(candidates) if c[0] == target[0] and c[1] == target[1]][0]
    reward = 1.0 if listener_action.item() == target_idx else -1.0
    reward -= 0.02 * len(symbols)  # length penalty

    advantage = reward - baseline
    total_log_prob = speaker_log_probs.sum() + listener_log_prob
    loss = -total_log_prob * advantage

    optimizer.zero_grad()
    loss.backward()  # type: ignore
    torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
    optimizer.step()  # type: ignore

    baseline = BASELINE_ALPHA * baseline + (1 - BASELINE_ALPHA) * reward

    if episode % PRINT_INTERVAL == 0 or episode == 1:
        print(f"Episode {episode:5d} | Reward: {reward:4.1f} | Len: {len(symbols):2d} | " f"Symbols: {symbols} | Target: {target[0]}-{target[1]}")
        log_history.append(f"Ep {episode}: symbols={symbols}, reward={reward}")

torch.save(model.state_dict(), "comm_model.pth")
print("\nTraining completed, model saved.")

# ---------- Testing ----------
print("\n--- Final test (10 random rounds) ---")
model.eval()
for _ in range(10):
    target, candidates = random_pair()
    target_feat = target[2]
    cand_feats = [c[2] for c in candidates]
    with torch.no_grad():
        symbols, _ = model.forward_speaker(target_feat)
        scores = model.forward_listener(symbols, cand_feats)
        pred_idx = int(torch.argmax(scores).item())
    pred_name = f"{candidates[pred_idx][0]}-{candidates[pred_idx][1]}"
    target_name = f"{target[0]}-{target[1]}"
    print(f"Target: {target_name:12s} | Symbols: {symbols} | Predicted: {pred_name:12s} | Correct: {target_name == pred_name}")
