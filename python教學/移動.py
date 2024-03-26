import pygame


def check_click(a: list[int | float] | tuple[int | float], b: list[int | float] | tuple[int | float]):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 < 100


pygame.init()
pygame.display.set_caption("移動")
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 20)

click = 0
pos = [400, 300]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0] and check_click(pos, mouse_pos):
                click += 1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and pos[1] > 10:
                pos[1] -= 10
            elif event.key == pygame.K_a and pos[0] > 10:
                pos[0] -= 10
            elif event.key == pygame.K_s and pos[1] < 790:
                pos[1] += 10
            elif event.key == pygame.K_d and pos[0] < 590:
                pos[0] += 10

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), pos, 10)

    text = font.render(f"click time:{click}", True, (255, 255, 255))
    screen.blit(text, (0, 0))

    pygame.display.update()
    clock.tick(10)
