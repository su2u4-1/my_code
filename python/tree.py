from random import randint
from typing import TypeVar, Callable
from json import loads

T = TypeVar("T")


def print_tree(node: T, tree_structure: dict[T, list[T]], tree: dict[T, T], output: list[str], indent: str = "", is_last: bool = True) -> None:
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


def load_tree_1(filename: str) -> tuple[dict[str, str], dict[str, list[str]]]:
    tree: dict[str, str] = {}
    tree_structure: dict[str, list[str]] = {}
    with open(filename, "r") as f:
        tree_structure = loads(f.read())
    for k, v in tree_structure.items():
        if len(v) == 0:
            continue
        for i in v:
            tree[i] = k
    return tree, tree_structure


def main_0() -> None:
    tree, tree_structure = load_tree_0("./virus.txt")
    output: list[str] = ["1"]
    children = tree_structure[0]
    for i, k in enumerate(children):
        print_tree(k, tree_structure, tree, output, "", i == len(children) - 1)
    with open("./python/data/m_tree.txt", "w+") as f:
        f.write("\n".join(output))
    draw_tree(tree_structure, 0, str)


def main_1() -> None:
    tree, tree_structure = load_tree_1("./python/data/f_tree.json")
    output: list[str] = ["0"]
    children = tree_structure["0"]
    for i, k in enumerate(children):
        print_tree(k, tree_structure, tree, output, "", i == len(children) - 1)
    with open("./python/data/f_tree.txt", "w+") as f:
        f.write("\n".join(output))
    with open("./python/data/.txt", "a") as f:
        f.write("\n".join([f"{k} {v}" for k, v in tree.items()]))


def main_2() -> None:
    tree, tree_structure = load_tree_1("./python/data/m_tree.json")
    output: list[str] = ["1"]
    children = tree_structure["1"]
    for i, k in enumerate(children):
        print_tree(k, tree_structure, tree, output, "", i == len(children) - 1)
    with open("./python/data/m_tree.txt", "w+") as f:
        f.write("\n".join(output))
    with open("./python/data/.txt", "a") as f:
        f.write("\n".join([f"{k} {v}" for k, v in tree.items()]))


if __name__ == "__main__":
    # main_0()
    main_1()
    main_2()
