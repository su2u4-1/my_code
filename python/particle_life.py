import pygame
import numpy as np

W, H = 1920, 1080
PARTICLE_COUNT = 3000
PARTICLE_RADIUS = 3
R_MIN = PARTICLE_RADIUS * 3 + 1
R_MAX = 100
FRICTION = 0.75
DT = 0.25
# 滑鼠斥力參數
MOUSE_REPULSE_RADIUS = 100.0
MOUSE_REPULSE_STRENGTH = 1000.0
# force_table = [
#     [1.25, -1.0, -0.15],  # r -> r, g, b
#     [1.0, 1.25, -0.15],  # g -> r, g, b
#     [0.5, 0.25, -0.1],  # b -> r, g, b
# ]
force_table = [
    [1, 1, 1],  # r -> r, g, b
    [1, 1, 1],  # g -> r, g, b
    [1, 1, 1],  # b -> r, g, b
]
FORCE_MATRIX = np.array(force_table, dtype=np.float32) * 5.0
COLOR_TABLE = np.array([[255, 0, 0], [0, 255, 0], [0, 0, 255]], dtype=np.uint8)
# 類型數量比例權重（可自行調整，例如 [0.7, 0.2, 0.1]）。
TYPE_WEIGHTS = np.array([0.25, 0.25, 0.5], dtype=np.float32)


class ParticleSystem:
    def __init__(self, n: int) -> None:
        # 粒子總數。
        self.n = n
        type_count = COLOR_TABLE.shape[0]

        # 粒子初始位置與速度都以向量化陣列儲存，方便一次更新全部粒子。
        self.pos = np.random.rand(n, 2).astype(np.float32) * [W, H]
        self.vel = np.zeros((n, 2), dtype=np.float32)
        # 依權重抽樣粒子類型，權重越高的類型數量越多。
        self.types = np.random.choice(type_count, size=n, p=TYPE_WEIGHTS / float(np.sum(TYPE_WEIGHTS))).astype(np.int32)
        self.colors = [tuple(c) for c in COLOR_TABLE[self.types]]
        # 預先計算交互矩陣以節省每一幀的索引開銷。
        self.inter_matrix = FORCE_MATRIX[self.types[:, np.newaxis], self.types[np.newaxis, :]]
        self.r_half_range = (R_MAX - R_MIN) * 0.5
        self.r_avg = (R_MAX + R_MIN) * 0.5

    def update(self, mouse_pos: tuple[int, int] | None = None) -> None:
        # 分離 X 與 Y 座標以減少記憶體壓力
        px = self.pos[:, 0]
        py = self.pos[:, 1]
        dx = px[:, np.newaxis] - px[np.newaxis, :]
        dy = py[:, np.newaxis] - py[np.newaxis, :]

        # 週期邊界修正：超過半個邊長就從另一側繞回（環面空間）。
        dx[dx > W * 0.5] -= W
        dx[dx < -W * 0.5] += W
        dy[dy > H * 0.5] -= H
        dy[dy < -H * 0.5] += H

        # 計算距離平方與距離。
        dist = np.sqrt(dx**2 + dy**2)

        # 處理自作用力與除零風險。
        dist = np.maximum(dist, 1e-5)

        # 計算力的大小。
        force_mag = np.zeros((self.n, self.n), dtype=np.float32)

        # 1. 強大斥力：當距離小於 R_MIN 時，force_mag 應為正值以推開粒子。
        mask_repel = dist < R_MIN
        force_mag[mask_repel] = (1.0 - dist[mask_repel] / R_MIN) * 20.0

        # 2. 中距離互動：根據交互矩陣決定吸引（負值）或排斥（正值）。
        mask_act = (dist >= R_MIN) & (dist < R_MAX)
        # 注意：此處加上負號是因為在 force_table 中 1 代表吸引，而在我們的向量運算中負值才代表吸引。
        force_mag[mask_act] = -self.inter_matrix[mask_act] * (1.0 - np.abs(dist[mask_act] - self.r_avg) / self.r_half_range)

        # 加速度向量計算：force_mag / dist 得到單位向量的力強度。
        inv_dist = force_mag / dist
        acc_x = np.sum(dx * inv_dist, axis=1)
        acc_y = np.sum(dy * inv_dist, axis=1)

        # 處理滑鼠斥力源。
        if mouse_pos:
            mx, my = mouse_pos
            mdx = px - mx
            mdy = py - my
            # 滑鼠交互同樣套用週期邊界修正。
            mdx[mdx > W * 0.5] -= W
            mdx[mdx < -W * 0.5] += W
            mdy[mdy > H * 0.5] -= H
            mdy[mdy < -H * 0.5] += H
            m_dist = np.sqrt(mdx**2 + mdy**2)
            m_dist = np.maximum(m_dist, 1.0)
            m_mask = m_dist < MOUSE_REPULSE_RADIUS
            m_force = (1.0 - m_dist[m_mask] / MOUSE_REPULSE_RADIUS) * MOUSE_REPULSE_STRENGTH
            acc_x[m_mask] += mdx[m_mask] * (m_force / m_dist[m_mask])
            acc_y[m_mask] += mdy[m_mask] * (m_force / m_dist[m_mask])

        # 物理積分與摩擦力。
        self.vel[:, 0] = (self.vel[:, 0] + acc_x * DT) * FRICTION
        self.vel[:, 1] = (self.vel[:, 1] + acc_y * DT) * FRICTION
        # 位置更新後以取模維持在環面邊界內。
        self.pos = (self.pos + self.vel * DT) % [W, H]

    def draw(self, screen: pygame.Surface) -> None:
        # 直接把粒子畫進螢幕。
        screen.fill((0, 0, 0))
        for i in range(self.n):
            pygame.draw.rect(screen, self.colors[i], (int(self.pos[i, 0]), int(self.pos[i, 1]), PARTICLE_RADIUS, PARTICLE_RADIUS))


def main() -> None:
    # 建立視窗並持續更新模擬，直到使用者關閉程式。
    pygame.init()
    screen = pygame.display.set_mode((W, H), pygame.FULLSCREEN)
    pygame.display.set_caption("Particle Life Optimized")
    clock = pygame.time.Clock()
    ps = ParticleSystem(PARTICLE_COUNT)
    run = True
    while True:
        # 處理事件。
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                return
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                elif e.key == pygame.K_SPACE:
                    run = not run

        # 檢測滑鼠按壓狀態。
        m_pos = None
        if pygame.mouse.get_pressed()[0]:
            m_pos = pygame.mouse.get_pos()

        # 每幀：更新物理、重畫畫面、提交到螢幕。
        if run:
            ps.update(m_pos)
        ps.draw(screen)
        pygame.display.flip()
        clock.tick()


if __name__ == "__main__":
    main()
