import pygame
import numpy as np
from numpy.typing import NDArray
from random import randint as ri
from random import choices, sample

W, H = 512, 512
# 定義 8 個方向的位移向量
DIRE_VEC: list[tuple[int, int]] = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
# 預處理感測器映射：當前方向 -> [(位移向量, 方向索引), ...]
SENSOR_MAP: dict[int, list[tuple[tuple[int, int], int]]] = {i: [(DIRE_VEC[(i - 1) % 8], (i - 1) % 8), (DIRE_VEC[i], i), (DIRE_VEC[(i + 1) % 8], (i + 1) % 8)] for i in range(8)}


class Weight:
    def __init__(self, w: int, params: tuple[float, float, float, float, float]) -> None:
        self.w = w
        self.params = params

    def mutation(self) -> tuple[float, float, float, float, float]:
        return tuple(p + ri(-10, 10) for p in self.params)  # type: ignore


def choice_weight(weights: list[Weight]) -> Weight:
    w = choices(weights, [item.w for item in weights])[0]
    if ri(0, 100) < 5:
        w = Weight(1, w.mutation())
        weights.append(w)
    return w


def diffuse_directional(ph: NDArray[np.float32], rate: float) -> None:
    # 增加全域衰減速度，防止色塊堆積
    ph *= 0.9
    # 取得當前所有像素的總強度（作為擴散源）
    intensity = np.sum(ph, axis=2)
    # 隨機選取 2~4 個方向進行「箭頭」擴散
    target_dirs = sample(range(8), ri(2, 4))

    for d in target_dirs:
        dx, dy = DIRE_VEC[d]
        # 指向當前像素的方向是反方向
        opposite_d = (d + 4) % 8
        # 將強度資訊「推」給鄰居
        shifted = np.roll(intensity, (dy, dx), axis=(0, 1))
        # 鄰居在 opposite_d 方向上的強度增加
        ph[..., opposite_d] = ph[..., opposite_d] * (1 - rate) + shifted * (rate * 0.4)

    # 針對部分方向進行強化衰減，快速清除過期路徑
    decay_dirs = sample(range(8), ri(2, 4))
    for d in decay_dirs:
        ph[..., d] *= 0.9

    # 清除微小數值，防止背景噪訊累積
    ph[ph < 0.5] = 0


def diffuse_special(ph: NDArray[np.float32], rate: float) -> None:
    # 特殊費洛蒙 (食物/家) 擴散但不衰減，使用拉普拉斯算子簡化版
    kernel = (np.roll(ph, 1, 0) + np.roll(ph, -1, 0) + np.roll(ph, 1, 1) + np.roll(ph, -1, 1)) * 0.25
    ph[:] = ph * (1 - rate) + kernel * rate


class Ant:
    def __init__(self, nest: tuple[int, int], weights: list[Weight]) -> None:
        self.nest = nest
        self.x, self.y = float(nest[0]), float(nest[1])
        self.carrying_food = False
        # self.direction = ri(0, 7)
        self.direction = 3
        self.w = choice_weight(weights)

    def update(self, ph_go: NDArray[np.float32], ph_back: NDArray[np.float32], ph_food: NDArray[np.float32], ph_home: NDArray[np.float32]) -> None:
        sensors = SENSOR_MAP[self.direction]
        scores = [0.0, 0.0, 0.0]

        # 尋找食物時：追蹤 ph_food 與 ph_back 的反向 (沿著別人回家的路反著找)
        # 回家時：追蹤 ph_home 與 ph_go 的反向 (沿著自己或別人的出發路反著回)
        target_special = ph_home if self.carrying_food else ph_food
        start_special = ph_food if self.carrying_food else ph_home
        other_directional = ph_go if self.carrying_food else ph_back
        self_directional = ph_back if self.carrying_food else ph_go

        for i, ((dx, dy), s_dir) in enumerate(sensors):
            nx, ny = int(self.x + dx * 8), int(self.y + dy * 8)
            if 0 <= nx < W and 0 <= ny < H:
                s_spec = target_special[ny, nx] * self.w.params[0] + start_special[ny, nx] * self.w.params[1]
                # 偵測鄰居點上「指向自己這端」的方向強度
                s_rev = other_directional[ny, nx, (s_dir + 4) % 8] * self.w.params[2] + self_directional[ny, nx, s_dir] * self.w.params[3]
                scores[i] = s_spec + s_rev

        # 轉向決策
        if scores[0] > scores[1] and scores[0] > scores[2]:
            self.direction = (self.direction - 1) % 8
        elif scores[2] > scores[1] and scores[2] > scores[0]:
            self.direction = (self.direction + 1) % 8
        elif ri(0, 100) < self.w.params[4]:
            self.direction = (self.direction + ri(-1, 1)) % 8

        vx, vy = DIRE_VEC[self.direction]
        new_x, new_y = self.x + vx * 1.5, self.y + vy * 1.5

        # 邊界處理：碰壁繞回對向
        if not (0 <= new_x < W) or not (0 <= new_y < H):
            self.direction = (self.direction + 4) % 8
            # if new_x < 0:
            #     self.x = W - ri(1, 10)
            # elif new_x >= W:
            #     self.x = ri(1, 10)
            # if new_y < 0:
            #     self.y = H - ri(1, 10)
            # elif new_y >= H:
            #     self.y = ri(1, 10)
        else:
            self.x, self.y = new_x, new_y

        ix, iy = int(self.x), int(self.y)
        if 0 <= ix < W and 0 <= iy < H:
            # 拾取食物
            if not self.carrying_food and ph_food[iy, ix] > 20:
                self.carrying_food = True
                ph_food[iy, ix] = max(0, ph_food[iy, ix] - 15)
                self.w.w += 1

            # 留下目前方向的費洛蒙，數值調整以配合快速衰減
            if self.carrying_food:
                if ph_back[iy, ix, (self.direction + 4) % 8] > 60:
                    ph_back[iy, ix, (self.direction + 4) % 8] -= 60
                elif ph_back[iy, ix, (self.direction + 4) % 8] > 0:
                    ph_back[iy, ix, self.direction] = min(255, ph_back[iy, ix, self.direction] + (60 - ph_back[iy, ix, (self.direction + 4) % 8]))
                    ph_back[iy, ix, (self.direction + 4) % 8] = 0
                else:
                    ph_back[iy, ix, self.direction] = min(255, ph_back[iy, ix, self.direction] + 60)
            else:
                if ph_go[iy, ix, (self.direction + 4) % 8] > 60:
                    ph_go[iy, ix, (self.direction + 4) % 8] -= 60
                elif ph_go[iy, ix, (self.direction + 4) % 8] > 0:
                    ph_go[iy, ix, self.direction] = min(255, ph_go[iy, ix, self.direction] + (60 - ph_go[iy, ix, (self.direction + 4) % 8]))
                    ph_go[iy, ix, (self.direction + 4) % 8] = 0
                else:
                    ph_go[iy, ix, self.direction] = min(255, ph_go[iy, ix, self.direction] + 60)


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((W, H))
    clock = pygame.time.Clock()

    ph_go = np.zeros((H, W, 8), dtype=np.float32)
    ph_back = np.zeros((H, W, 8), dtype=np.float32)
    ph_food = np.zeros((H, W), dtype=np.float32)
    ph_home = np.zeros((H, W), dtype=np.float32)

    # 初始化地圖
    ph_food[H - 150 : H - 50, W - 150 : W - 50] = 255.0
    ph_home[75:125, 75:125] = 255.0
    nest_pos = (100, 100)

    # 調整初始權重比例，增加方向引導的敏感度
    weights: list[Weight] = [Weight(1, (100, -100, 1000, -50, -100))]
    ants = [Ant(nest_pos, weights) for _ in range(3000)]

    run = True
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                return
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                run = not run

        if run:
            diffuse_directional(ph_go, 0.1)
            diffuse_directional(ph_back, 0.1)
            diffuse_special(ph_food, 0.02)
            diffuse_special(ph_home, 0.02)

            for ant in ants:
                ant.update(ph_go, ph_back, ph_food, ph_home)
                # 回到蟻巢
                if ant.carrying_food and abs(ant.x - nest_pos[0]) < 20 and abs(ant.y - nest_pos[1]) < 20:
                    ant.carrying_food = False
                    ant.w.w += 20
                    if ant.w not in log:
                        log[ant.w] = 0
                    log[ant.w] += 1

        # 視覺化渲染
        vis_array = np.zeros((H, W, 3), dtype=np.uint8)
        # R: 尋路路徑 (ph_go), G: 回家路徑與巢穴 (ph_back + ph_home), B: 食物 (ph_food)
        vis_array[..., 0] = np.sum(ph_go, axis=2).clip(0, 255).astype(np.uint8)
        vis_array[..., 1] = np.maximum(np.sum(ph_back, axis=2), ph_home).clip(0, 255).astype(np.uint8)
        vis_array[..., 2] = ph_food.clip(0, 255).astype(np.uint8)

        surf = pygame.surfarray.make_surface(vis_array.transpose(1, 0, 2))  # type: ignore
        screen.blit(surf, (0, 0))

        # 繪製蟻巢
        pygame.draw.circle(screen, (150, 75, 0), nest_pos, 10)

        # 繪製螞蟻
        for ant in ants:
            color = (255, 255, 0) if ant.carrying_food else (255, 128, 128)
            pygame.draw.rect(screen, color, (int(ant.x), int(ant.y), 2, 2))

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    log: dict[Weight, int] = {}
    main()
    # 輸出訓練日誌
    for w, count in sorted(log.items(), key=lambda x: x[1], reverse=True):
        print(f"Weight: ({w.w}, {w.params}), Count: {count}")
