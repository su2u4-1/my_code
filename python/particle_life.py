import pygame
import numpy as np
from numpy.typing import NDArray
from random import randint as ri
from random import choices

W, H = 512, 512

DIRE_VEC = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
SENSOR_MAP = {i: (DIRE_VEC[(i - 1) % 8], DIRE_VEC[i], DIRE_VEC[(i + 1) % 8]) for i in range(8)}
color_table = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
force_table = [
    # r g  b
    [2, 0, 0],  # r
    [0, 2, 0],  # g
    [0, 0, 2],  # b
]


class Weight:
    def __init__(self, w: int, params: tuple[float, float, float, float]):
        self.w = w
        self.params = params

    def mutation(self) -> tuple[float, float, float, float]:
        return tuple(p + ri(-10, 10) for p in self.params)  # type: ignore


def choice_weight(weights: list[Weight]) -> Weight:
    w = choices(weights, [item.w for item in weights])[0]
    if ri(0, 100) < 10:
        w = Weight(1, w.mutation())
        weights.append(w)
    return w


# (1000, -1000, 10, -10)
weight: list[Weight] = [Weight(90, (1000, -1000, 10, -10)), Weight(9, (1000, -1000, 1, -1)), Weight(1, (1000, -1000, 0, 0))]


def fast_diffuse(arr: NDArray[np.float32], attenuate: float) -> NDArray[np.float32]:
    diffused = arr.copy()
    diffused[1:-1, 1:-1] = arr[1:-1, 1:-1] * 0.6 + (arr[:-2, 1:-1] + arr[2:, 1:-1] + arr[1:-1, :-2] + arr[1:-1, 2:]) * 0.1
    diffused[diffused < 0.5] = 0
    return diffused * attenuate


class Ant:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.kind = ri(0, 2)
        self.direction = ri(0, 7)

    def update(self, ph: list[NDArray[np.float32]]) -> None:
        sensor_dirs = [(self.direction + i) % 8 for i in range(-1, 2)]
        sensors = [DIRE_VEC[d] for d in sensor_dirs]
        scores = [0.0 for _ in range(3)]
        for idx, (dx, dy) in enumerate(sensors):
            nx, ny = int(self.x + dx * 5), int(self.y + dy * 5)
            if 0 <= nx < W and 0 <= ny < H:
                for i in range(len(ph)):
                    scores[idx] += ph[i][ny, nx] * force_table[self.kind][i]
        best_idx = max(range(3), key=lambda i: scores[i])
        if ri(0, 100) < 50:
            self.direction = self.direction
        else:
            self.direction = sensor_dirs[best_idx]
        dx, dy = DIRE_VEC[self.direction]
        new_x, new_y = self.x + dx * 1.5, self.y + dy * 1.5
        # 修改後的邊界傳送邏輯
        if not (0 <= new_x < W) or not (0 <= new_y < H):
            # self.direction = (self.direction + 4) % 8
            if new_x < 0:
                self.x = W - ri(1, 10)
            elif new_x >= W:
                self.x = ri(1, 10)
            if new_y < 0:
                self.y = H - ri(1, 10)
            elif new_y >= H:
                self.y = ri(1, 10)
        else:
            self.x, self.y = new_x, new_y
        ix, iy = int(self.x), int(self.y)
        if 0 <= ix < W and 0 <= iy < H:
            ph[self.kind][iy, ix] = min(255, ph[self.kind][iy, ix] + 60)


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((W, H))
    clock = pygame.time.Clock()
    ph: list[NDArray[np.float32]] = [np.zeros((H, W), dtype=np.float32), np.zeros((H, W), dtype=np.float32), np.zeros((H, W), dtype=np.float32)]
    ants = [Ant(ri(10, W - 10), ri(10, H - 10)) for _ in range(5000)]
    run = True
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                return
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                run = not run
        if run:
            for ant in ants:
                ant.update(ph)
            for k in range(len(ph)):
                ph[k] = fast_diffuse(ph[k], 0.98)
        vis_array = np.zeros((H, W, 3), dtype=np.uint8)
        for k in range(len(ph)):
            vis_array[..., k] = np.clip(ph[k], 0, 255)
        surf = pygame.surfarray.make_surface(vis_array.transpose(1, 0, 2))  # type: ignore
        screen.blit(surf, (0, 0))
        for ant in ants:
            color = color_table[ant.kind]
            pygame.draw.rect(screen, color, (int(ant.x), int(ant.y), 2, 2))
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
