from typing import Sequence
import pygame
from random import randint, random

# constants
FOOD_GROWTH_RATE = 0.05
INITIAL_CELLS = 50
INITIAL_FOOD = 50
# MAX_CELLS = 1000
MAX_CELLS = float("inf")
LOGFILE_PATH = "cell_logs.json"

id = 0
logs: list[str] = []


class Cell:
    def __init__(self, x: int, y: int, dna: Sequence[float], energy: int = 100, parent: int = -1) -> None:
        global id
        self.x = x
        self.y = y
        self.energy = energy
        assert len(dna) == 6
        # dna: (eat_max, mutation_rate, attack, defense, reproduction_rate, move_tendency)
        self.dna = list(dna)
        self.id = id
        logs.append(f'{{"ID": {id}, "parent": {parent}, "pos": "({self.x}, {self.y})", "energy": {self.energy}, "dna": [{', '.join(f'{i:.2f}' for i in self.dna)}]}}')
        id += 1

    def __str__(self) -> str:
        return f"{{pos: ({self.x}, {self.y}), energy: {self.energy}, dna: ({", ".join(f"{i:.2f}" for i in self.dna)}), dna_sum: {sum(self.dna):.2f}}}"

    def update(self) -> None:
        self.energy -= min(int(sum(self.dna)), self.energy)
        if self.energy < 255:
            original_energy = self.energy
            self.energy = min(255, self.energy + min(int(self.dna[0] * 100), grid[self.x][self.y]))
            eaten_amount = self.energy - original_energy
            grid[self.x][self.y] -= eaten_amount
        move_rate = 1
        if grid[self.x][self.y] < self.dna[0] * 100:
            move_rate = 1.5
        elif grid[self.x][self.y] >= self.dna[0] * 110:
            move_rate = 0.7
        for cell in cell_list:
            if cell != self and cell.x == self.x and cell.y == self.y:
                move_rate *= 1.5
                if self.dna[2] * sum(self.dna) > cell.dna[3] * sum(cell.dna) and self.dna[2] > cell.dna[3]:
                    damage = min(cell.energy, int((self.dna[2] - cell.dna[3]) * 50))
                    cell.energy -= damage
                    cell.energy = max(0, cell.energy)
                    self.energy += damage // 2
                    self.energy = min(255, self.energy)
                if self.dna[3] * sum(self.dna) < cell.dna[2] * sum(cell.dna) and self.dna[3] < cell.dna[2]:
                    damage = min(self.energy, int((cell.dna[2] - self.dna[3]) * 50))
                    self.energy -= damage
                    self.energy = max(0, self.energy)
                    cell.energy += damage // 2
                    cell.energy = min(255, cell.energy)
            else:
                move_rate *= 0.5
        if random() < self.dna[5] * move_rate:
            self.move()
        if len(cell_list) < MAX_CELLS and self.energy >= self.dna[4] * 255 and random() * 4 < self.dna[4]:
            self.energy //= 2
            child_dna = list(self.dna)
            for i in range(len(child_dna)):
                if random() < self.dna[1]:
                    mx = max(0, child_dna[i] - random() * self.dna[1])
                    mi = min(1, child_dna[i] + random() * self.dna[1])
                    child_dna[i] = (mx, mi)[randint(0, 1)]
            cell_list.append(Cell(self.x, self.y, child_dna, self.energy, self.id))
            cell_list[-1].move()

    def move(self) -> None:
        dx, dy = self.x, self.y
        mx = grid[dx][dy]
        for x in range(-3, 4):
            for y in range(-3, 4):
                nx, ny = max(0, min(grid_h - 1, self.x + x)), max(0, min(grid_w - 1, self.y + y))
                if grid[nx][ny] >= mx:
                    mx = grid[nx][ny]
                    dx, dy = nx, ny
        self.x, self.y = dx, dy


def summon_cell(n: int) -> None:
    for _ in range(n):
        # dna: (eat_max, mutation_rate, attack, defense, reproduction_rate, move_tendency)
        cell_list.append(Cell(randint(0, grid_h - 1), randint(0, grid_w - 1), [random(), random(), random(), random(), random(), random()]))
        # cell_list.append(Cell(randint(0, grid_h - 1), randint(0, grid_w - 1), [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]))


def update() -> None:
    for i in range(grid_h):
        for j in range(grid_w):
            if random() < FOOD_GROWTH_RATE and grid[i][j] < 255:
                grid[i][j] += 1
    for cell in cell_list:
        cell.update()
        if cell.energy <= 0:
            cell_list.remove(cell)
    cell_list.sort(key=lambda c: c.energy)


def draw() -> None:
    for i in range(grid_h):
        for j in range(grid_w):
            if grid[i][j] > 0:
                pygame.draw.rect(screen, (0, grid[i][j], 0), (j * 10, i * 10, 10, 10))
    h_cell = None
    for cell in cell_list:
        try:
            pygame.draw.rect(screen, (0, 0, cell.energy), (cell.y * 10, cell.x * 10, 10, 10))
        except Exception as e:
            print(f"Error drawing cell: {cell}, error: {e}")
        if cell == highlighted_cell:
            h_cell = pygame.Rect(cell.y * 10, cell.x * 10, 10, 10)
    if h_cell:
        pygame.draw.rect(screen, (255, 0, 0), h_cell, 1)
    text = font.render(f"Cells: {len(cell_list)}", True, (255, 255, 255))
    cell_status = font.render(f"Cell Status: {highlighted_cell}", True, (255, 255, 255))
    food_value_text = font.render(f"Food Value: {food_value}", True, (255, 255, 255))
    screen.blit(text, (10, 10))
    screen.blit(cell_status, (10, 50))
    screen.blit(food_value_text, (10, 90))


def stop() -> None:
    with open(LOGFILE_PATH, "w") as f:
        f.write("[" + ",\n".join(logs) + "]")
    pygame.quit()
    exit()


# init
screen_w, screen_h = 800, 600
grid_w, grid_h = screen_w // 10, screen_h // 10
cell_list: list[Cell] = []
grid: list[list[int]] = [[INITIAL_FOOD for _ in range(grid_w)] for _ in range(grid_h)]
summon_cell(INITIAL_CELLS)
running = True
highlighted_cell = None
food_value = -1
year = 0
step = False

# pygame init
pygame.init()
screen = pygame.display.set_mode((screen_w, screen_h), pygame.RESIZABLE)
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# main loop
while True:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                stop()
            elif event.key == pygame.K_SPACE:
                running = not running
            elif event.key == pygame.K_k:
                cell_list = cell_list[len(cell_list) // 2 :]
            elif event.key == pygame.K_z:
                for cell in cell_list:
                    cell.x = randint(0, grid_h - 1)
                    cell.y = randint(0, grid_w - 1)
            elif event.key == pygame.K_s:
                step = True
        elif event.type == pygame.VIDEORESIZE:
            screen_w, screen_h = event.w, event.h
            grid = [[grid[i][j] if i < grid_h and j < grid_w else INITIAL_FOOD for j in range(screen_w // 10)] for i in range(screen_h // 10)]
            grid_w, grid_h = screen_w // 10, screen_h // 10
            screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            grid_y: int = event.pos[0] // 10
            grid_x: int = event.pos[1] // 10
            if 0 <= grid_x < grid_h and 0 <= grid_y < grid_w:
                food_value = grid[grid_x][grid_y]
            if event.button == 1:
                for cell in cell_list[::-1]:
                    if cell.x == grid_x and cell.y == grid_y:
                        highlighted_cell = cell
                        break
                else:
                    highlighted_cell = None
            else:
                highlighted_cell = None

    # clear screen
    screen.fill((0, 0, 0))

    # game logic
    if not running and step:
        year += 1
        update()
        step = False
    # if year % 100 == 0 and len(cell_list) >= 250:
    #     cell_list = cell_list[len(cell_list) // 2 :]
    if running:
        year += 1
        update()
    draw()

    # flip display
    pygame.display.flip()
    clock.tick(60)
