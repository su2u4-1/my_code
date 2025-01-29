import pygame, sys


def main():
    pygame.init()
    pygame.display.set_caption("遊戲4.0")
    screen = pygame.display.set_mode((700, 700))
    clock = pygame.time.Clock()
    img_bg = pygame.image.load("五行.png")
    img_pat = pygame.image.load("太極.png")
    img_pat = pygame.transform.scale(img_pat, [50, 50])
    font = pygame.font.Font(None, 40)
    tmr = 0
    f = 0

    while True:
        tmr += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    f += 1
                    if f % 2 == 1:
                        screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)
                    if f % 2 == 0:
                        screen = pygame.display.set_mode((800, 600))

        txt = font.render(str(tmr), True, (0, 0, 0))
        screen.fill((255, 255, 255))
        screen.blit(img_bg, [0, 0])
        screen.blit(img_pat, [650, 0])
        screen.blit(txt, [0, 0])
        pygame.display.update()
        clock.tick(10)


if __name__ == "__main__":
    main()
