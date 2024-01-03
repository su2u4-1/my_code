import pygame
from random import randint as ri


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xy = (x, y)
        self.color = (ri(64, 255), ri(64, 255), ri(64, 255))

    def display(self, screen):
        pygame.draw.circle(screen, self.color, self.xy, 5)


class Side:
    def __init__(self, s, e, n):
        self.s = s
        self.e = e
        self.n = n
        self.color = (ri(64, 255), ri(64, 255), ri(64, 255))
        self.l = ((s.x - e.x) ** 2 + (s.y - e.y) ** 2) ** 0.5

    def display(self, screen):
        pygame.draw.line(screen, self.color, self.s.xy, self.e.xy)


def selection_sort(list):
    for i in range(len(list) - 1):
        x = i
        for j in range(i, len(list)):
            if list[j].l < list[x].l:
                x = j
        list[i], list[x] = list[x], list[i]
    return list


pygame.init()
pygame.display.set_caption("視窗")
W = pygame.display.Info().current_w
H = pygame.display.Info().current_h
screen = pygame.display.set_mode((W, H), pygame.FULLSCREEN)
clock = pygame.time.Clock()
font = pygame.font.Font("C:\\Windows\\Fonts\\kaiu.ttf", 48)
n = 10
node_list = []
for _ in range(n):
    node_list.append(Node(ri(10, W - 10), ri(10, H - 10)))
side_list = []
for i in range(n):
    for j in range(i + 1, n):
        side_list.append(Side(node_list[i], node_list[j], (i, j)))

side_list = selection_sort(side_list)
for i in node_list:
    print(i.xy)

new_node_list = [node_list[0]]
new_side_list = []
while len(new_node_list) < n:
    for j in side_list:
        if j.s in new_node_list:
            new_side_list.append(j)
            side_list.remove(j)
            new_node_list.append(node_list[j.n[0]])
        elif j.e in new_node_list:
            new_side_list.append(j)
            side_list.remove(j)
            new_node_list.append(node_list[j.n[1]])

while True:
    mousex, mousey = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    screen.fill((0, 0, 0))
    for i in new_node_list:
        i.display(screen)
    for i in new_side_list:
        i.display(screen)

    pygame.display.update()
    clock.tick(10)
