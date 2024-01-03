import pygame, sys
from random import randint as ri


def main():
    pygame.init()
    pygame.display.set_caption("遊戲4.0")
    screen = pygame.display.set_mode((800, 450))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 40)
    r = 255
    b = 0
    g = 0

    while True:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    r += 5
                    r = (255, r)[r < 255]
                elif event.key == pygame.K_s:
                    r -= 5
                    r = (0, r)[r > 0]
                elif event.key == pygame.K_e:
                    b += 5
                    b = (255, b)[b < 255]
                elif event.key == pygame.K_d:
                    b -= 5
                    b = (0, b)[b > 0]
                elif event.key == pygame.K_r:
                    g += 5
                    g = (255, g)[g < 255]
                elif event.key == pygame.K_f:
                    g -= 5
                    g = (0, g)[g > 0]
                elif event.key == pygame.K_SPACE:
                    r = ri(0, 51) * 5
                    b = ri(0, 51) * 5
                    g = ri(0, 51) * 5

        txt = font.render(f"R:{r},B:{b},G:{g}", True, (0, 0, 0))
        pygame.draw.rect(screen, (r, b, g), (100, 100, 400, 300), 0)
        screen.blit(txt, [0, 0])
        pygame.display.update()
        clock.tick(10)


if __name__ == "__main__":
    main()
