import pygame
from random import randint as ri
from math import cos, sin, radians, sqrt
import numpy as np

W, H = 1366, 768
DEFAULT_ENERGY = 8000
FOOD_ENERGY = 10
FOOD_UPDATE_INTERVAL = 10
NUM_FOOD_SOURCES = 100
PREY_CELL_SIZE = 10
PREY_WEIGHT = 100
GRID_CELL = 60


def wrap_delta(a: float, b: float, length: int) -> float:
    d = a - b
    if d > length / 2:
        d -= length
    elif d < -length / 2:
        d += length
    return d


class Creature:
    def __init__(self, x: float = W // 2, y: float = H // 2):
        self.x = float(x)
        self.y = float(y)
        self.speed = 2
        self.size = 1
        self.perception = 30
        self.energy = DEFAULT_ENERGY

    def move(self, grid: dict[tuple[int, int], list["Creature"]]):
        if self.energy <= 0:
            return
        x, y = self.x, self.y
        size = self.size
        p = self.perception
        p2 = p * p
        bigger = size * 1.2
        smaller = size * 0.8

        ci, cj = int(x) % W, int(y) % H
        if min(int(food_map[ci, cj]), 50) * FOOD_ENERGY > p:
            self.energy -= p
            return

        cx, cy = int(x) // GRID_CELL, int(y) // GRID_CELL
        r = int(p) // GRID_CELL + 1

        nearest_threat = None
        threat_d2 = p2
        prey_cells: dict[tuple[int, int], int] = {}
        for di in range(-r, r + 1):
            for dj in range(-r, r + 1):
                cell = grid.get((cx + di, cy + dj))
                if cell is None:
                    continue
                for c in cell:
                    if c is self:
                        continue
                    dx = wrap_delta(c.x, x, W)
                    dy = wrap_delta(c.y, y, H)
                    d2 = dx * dx + dy * dy
                    if d2 > p2:
                        continue
                    cs = c.size
                    if cs >= bigger:
                        if d2 < threat_d2:
                            threat_d2 = d2
                            nearest_threat = c
                    elif cs <= smaller:
                        key = (int(c.x) // PREY_CELL_SIZE, int(c.y) // PREY_CELL_SIZE)
                        prey_cells[key] = prey_cells.get(key, 0) + 1

        best_food_cell: tuple[int, int] | None = None
        best_food_val = 0
        ip = int(p)
        xs = np.arange(int(x) - ip, int(x) + ip + 1) % W
        ys = np.arange(int(y) - ip, int(y) + ip + 1) % H
        region = food_map[np.ix_(xs, ys)]
        max_v = int(region.max())
        if max_v > 0:
            idxs = np.flatnonzero(region == max_v)
            k = int(idxs[int(np.random.randint(len(idxs)))])
            di2, dj2 = divmod(k, len(ys))
            best_food_cell = (int(xs[di2]), int(ys[dj2]))
            best_food_val = max_v

        if nearest_threat is not None:
            dx = wrap_delta(x, nearest_threat.x, W)
            dy = wrap_delta(y, nearest_threat.y, H)
        else:
            best_prey_key: tuple[int, int] | None = None
            best_prey_attract = 0
            if prey_cells:
                best_prey_key = max(prey_cells, key=(lambda kk: prey_cells.get(kk, 0)))
                best_prey_attract = prey_cells[best_prey_key] * PREY_WEIGHT

            if best_prey_key is not None and best_prey_attract >= best_food_val:
                tx = best_prey_key[0] * PREY_CELL_SIZE + PREY_CELL_SIZE // 2
                ty = best_prey_key[1] * PREY_CELL_SIZE + PREY_CELL_SIZE // 2
                dx = wrap_delta(tx, x, W)
                dy = wrap_delta(ty, y, H)
            elif best_food_cell is not None:
                dx = wrap_delta(best_food_cell[0], x, W)
                dy = wrap_delta(best_food_cell[1], y, H)
            else:
                a = radians(ri(0, 359))
                dx = cos(a)
                dy = sin(a)

        mag = sqrt(dx * dx + dy * dy)
        if mag < 1e-6:
            a = radians(ri(0, 359))
            dx = cos(a)
            dy = sin(a)
            mag = 1.0

        step = self.speed / mag
        nx = (x + dx * step) % W
        ny = (y + dy * step) % H

        mdx = wrap_delta(nx, x, W)
        mdy = wrap_delta(ny, y, H)
        moved = sqrt(mdx * mdx + mdy * mdy)
        self.x = nx
        self.y = ny

        speed = self.speed
        move_ratio = moved / speed if speed > 0 else 0.0
        self.energy -= speed * speed * size * size * size * move_ratio + p

    def reproduction(self):
        if self.energy < DEFAULT_ENERGY * 2:
            return
        self.energy -= DEFAULT_ENERGY
        c = Creature(self.x, self.y)
        c.speed = max(1, int(self.speed + ri(-1, 1)))
        c.size = max(1, int(self.size + ri(-1, 1)))
        c.perception = max(1, int(self.perception + ri(-1, 1)))
        creatures.append(c)


pygame.init()
screen = pygame.display.set_mode((W, H))
front = pygame.font.SysFont(None, 20)
clock = pygame.time.Clock()

creatures: list[Creature] = [Creature(ri(0, W), ri(0, H)) for _ in range(100)]

food_map: np.ndarray = np.zeros((W, H), dtype=np.uint8)
food_sources: list[tuple[int, int]] = []

food_surface = pygame.Surface((W, H))


def update_food_map():
    global food_map, food_sources
    fm = food_map.astype(np.int32)
    s = fm + np.roll(fm, 1, axis=0) + np.roll(fm, -1, axis=0) + np.roll(fm, 1, axis=1) + np.roll(fm, -1, axis=1) + np.roll(np.roll(fm, 1, axis=0), 1, axis=1) + np.roll(np.roll(fm, 1, axis=0), -1, axis=1) + np.roll(np.roll(fm, -1, axis=0), 1, axis=1) + np.roll(np.roll(fm, -1, axis=0), -1, axis=1)
    divisor = 8.0 + min(1.0, len(creatures) / 500.0)
    food_map = np.minimum(s / divisor, 255).astype(np.uint8)
    food_sources = [(ri(0, W - 1), ri(0, H - 1)) for _ in range(NUM_FOOD_SOURCES)]
    for fi, fj in food_sources:
        food_map[fi, fj] = 255


def build_grid() -> dict[tuple[int, int], list[Creature]]:
    g: dict[tuple[int, int], list[Creature]] = {}
    for c in creatures:
        key = (int(c.x) // GRID_CELL, int(c.y) // GRID_CELL)
        g.setdefault(key, []).append(c)
    return g


def refresh_food_surface():
    px = pygame.surfarray.pixels3d(food_surface)
    px[:, :, 0] = 0
    px[:, :, 1] = food_map
    px[:, :, 2] = 0
    del px


space = False
t = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            elif event.key == pygame.K_SPACE:
                space = not space

    clock.tick(60)

    if space:
        continue

    if t % FOOD_UPDATE_INTERVAL == 0:
        update_food_map()

    grid = build_grid()
    for c in creatures:
        c.move(grid)
    creatures = [c for c in creatures if c.energy > 0]

    for c in creatures:
        i, j = int(c.x) % W, int(c.y) % H
        v = int(food_map[i, j])
        if v > 0:
            eaten = min(v, 50)
            c.energy += eaten * FOOD_ENERGY
            food_map[i, j] = v - eaten

    grid = build_grid()
    dead: set[int] = set()
    for c1 in creatures:
        cx = int(c1.x) // GRID_CELL
        cy = int(c1.y) // GRID_CELL
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                cell = grid.get((cx + di, cy + dj))
                if cell is None:
                    continue
                for c2 in cell:
                    if c1 is c2 or id(c2) in dead:
                        continue
                    dx = wrap_delta(c2.x, c1.x, W)
                    dy = wrap_delta(c2.y, c1.y, H)
                    if dx * dx + dy * dy < c1.size * c1.size and c1.size > c2.size * 1.2:
                        # print(f"Creature {id(c1)}({c1.energy}, {c1.size}) ate creature {id(c2)}({c2.energy}, {c2.size})")
                        dead.add(id(c2))
                        c1.energy += c2.energy
    creatures = [c for c in creatures if id(c) not in dead]

    for c in creatures:
        c.reproduction()

    if len(creatures) < 10:
        creatures.append(Creature(ri(0, W), ri(0, H)))
        for _ in range(DEFAULT_ENERGY // 10):
            i, j = ri(0, W - 1), ri(0, H - 1)
            food_map[i, j] = max(0, int(food_map[i, j]) - 10)

    refresh_food_surface()
    screen.blit(food_surface, (0, 0))
    for c in creatures:
        cv = max(0, min(255, int(c.energy * 255 / (DEFAULT_ENERGY * 2 + 2500))))
        pygame.draw.circle(screen, (0, 0, cv), (int(c.x), int(c.y)), int(c.perception), 1)
        pygame.draw.circle(screen, (cv, 0, 0), (int(c.x), int(c.y)), c.size)

    screen.blit(front.render(f"Creatures: {len(creatures)}", True, (255, 255, 255)), (10, 10))

    pygame.display.flip()
    t += 1
