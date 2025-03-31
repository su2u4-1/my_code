from random import randint
from typing import TypeVar, Callable

T = TypeVar("T")


def print_tree(node: int, tree_structure: dict[int, list[int]], tree: dict[int, int], output: list[str], indent: str = "", is_last: bool = True) -> None:
    branch = "└── " if is_last else "├── "
    output.append(f"{indent}{branch}{tree[node]}>{node}")
    indent += "    " if is_last else "│   "
    if node in tree_structure:
        children = tree_structure[node]
        for i, child in enumerate(children):
            print_tree(child, tree_structure, tree, output, indent, i == len(children) - 1)


def calculate_wh(tree_structure: dict[T, list[T]], start: T, w: int = 1, h: int = 1) -> tuple[int, int]:
    w += len(tree_structure[start]) - 1
    sh = 0
    for i in tree_structure[start]:
        if i in tree_structure:
            sw, ssh = calculate_wh(tree_structure, i, 0, h + 1)
            w += sw
            sh = max(sh, ssh)
    h = max(sh, h)
    return w, h


def draw_tree(tree_structure: dict[T, list[T]], start: T, show: Callable[[T], str]) -> None:
    import pygame

    pygame.init()

    def draw_tree_node(
        screen: pygame.Surface,
        tree_structure: dict[T, list[T]],
        start: T,
        show: Callable[[T], str],
        font: pygame.font.Font,
        x: int = 0,
        y: int = 0,
        w: int = 50,
        r: int = 10,
    ) -> int:
        if start not in color:
            color[start] = (randint(0, 255), randint(0, 255), randint(0, 255))
        pygame.draw.circle(screen, color[start], (x * w + (w // 2), y * w + (w // 2)), r, 3)
        text = font.render(show(start), True, (0, 0, 0))
        screen.blit(text, (x * w + (w // 2 - r), y * w + (w // 2 - r)))
        ox = x
        if start in tree_structure:
            pygame.draw.line(screen, color[start], (x * w + (w // 2), y * w + (w // 2 + r)), (x * w + (w // 2), y * w + (w // 2 + 4 * r)), 3)
            children = tree_structure[start]
            x = draw_tree_node(screen, tree_structure, children[0], show, font, x, y + 1)
            for child in children[1:]:
                pygame.draw.line(screen, color[start], ((x + 1) * w + (w // 2), y * w + w), (ox * w + (w // 2), y * w + w), 3)
                pygame.draw.line(screen, color[start], ((x + 1) * w + (w // 2), y * w + w), ((x + 1) * w + (w // 2), y * w + (w // 2 + 4 * r)), 3)
                x = draw_tree_node(screen, tree_structure, child, show, font, x + 1, y + 1)
        return x

    color: dict[T, tuple[int, int, int]] = {}

    w, h = calculate_wh(tree_structure, start)
    screen = pygame.display.set_mode((w * 50 + 50, h * 50 + 50))
    font = pygame.font.Font(None, 30)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        screen.fill((255, 255, 255))
        draw_tree_node(screen, tree_structure, start, show, font)
        pygame.display.update()
        clock.tick(10)


def load_tree_0(filename: str) -> tuple[dict[int, int], dict[int, list[int]]]:
    tree: dict[int, int] = {}
    tree_structure: dict[int, list[int]] = {}
    with open(filename, "r") as f:
        for i in f.readlines()[102:-1]:
            i = i.split()
            tree[int(i[0][:-1])] = int(i[-1][:-2])
    for k, v in tree.items():
        if v == -1:
            continue
        elif v not in tree_structure:
            tree_structure[v] = []
        tree_structure[v].append(k)
    return tree, tree_structure


tree, tree_structure = load_tree_0("./virus.txt")
output: list[str] = ["0"]
children = tree_structure[0]
for i, k in enumerate(children):
    print_tree(k, tree_structure, tree, output, "", i == len(children) - 1)

# print(tree_structure)
# {0: [1, 2, 8, 9, 10, 20, 29, 38, 50], 20: [22, 36], 8: [24], 29: [34], 10: [35, 42, 43], 9: [37], 2: [39], 24: [41, 49, 52], 1: [44, 47], 38: [48], 41: [51]}

with open("./tree.txt", "w+") as f:
    f.write("\n".join(output))

draw_tree(tree_structure, 0, str)
