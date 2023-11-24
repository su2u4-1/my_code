import pygame, sys

color = [
    (0, 255, 255),
    (0, 0, 0),
    (0, 0, 255),
    (255, 0, 255),
    (128, 128, 128),
    (0, 128, 0),
    (0, 255, 0),
    (128, 0, 0),
    (0, 0, 128),
    (128, 128, 0),
    (128, 0, 128),
    (255, 0, 0),
    (192, 192, 192),
    (0, 128, 128),
    (255, 255, 255),
    (255, 255, 0),
]


def main():
    pygame.init()
    pygame.display.set_caption("遊戲4.0")
    screen = pygame.display.set_mode((800, 450))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 40)
    tmr = 0
    f = 0
    r = 255
    b = 0
    g = 0
    a = 0
    pygame.display.update(screen.fill((255, 255, 255)))
    mouse = False

    while True:
        tmr += 1
        mousex, mousey = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    f += 1
                    if f % 2 == 1:
                        screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
                    if f % 2 == 0:
                        screen = pygame.display.set_mode((800, 450))
            if event.type == pygame.MOUSEBUTTONUP:
                pygame.display.update(screen.fill((255, 255, 255)))
                if mouse == False:
                    mouse = True
                else:
                    mouse = False

        if mouse == False:
            if r == 255 and b < 255 and g == 0:
                b += 5
            if r > 1 and b == 255 and g == 0:
                r -= 5
            if r == 0 and b == 255 and g < 255:
                g += 5
            if r == 0 and b > 1 and g == 255:
                b -= 5
            if r < 255 and b == 0 and g == 255:
                r += 5
            if r == 255 and b == 0 and g > 1:
                g -= 5
        txt = font.render(f"R:{r},B:{b},G:{g}", True, (0, 0, 0))
        pygame.display.update(
            pygame.draw.rect(
                screen,
                (r, b, g),
                (
                    screen.get_size()[0] / 4,
                    screen.get_size()[1] / 4,
                    screen.get_size()[0] / 2,
                    screen.get_size()[1] / 2,
                ),
                width=0,
            )
        )
        pygame.display.update(
            pygame.draw.rect(screen, (255, 255, 255), (0, 0, 214, 27))
        )
        for i in range(16):
            pygame.display.update(
                pygame.draw.rect(screen, color[i], (i * 50, 30, 50, 50))
            )
        pygame.display.update(screen.blit(txt, [0, 0]))
        clock.tick(10)


if __name__ == "__main__":
    main()
