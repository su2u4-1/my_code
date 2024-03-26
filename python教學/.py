import pygame

pygame.init()
pygame.display.set_caption("移動")
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
clock = pygame.time.Clock()
sky_blue = (135, 206, 235)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

    screen.fill(sky_blue)
    pygame.draw.rect(screen, (255, 255, 255), (100, 200, 200, 200))
    pygame.draw.polygon(screen, (255, 0, 0), ((100, 200), (300, 200), (200, 100)))
    pygame.draw.rect(screen, sky_blue, (130, 230, 30, 30))
    pygame.draw.rect(screen, sky_blue, (130, 270, 30, 30))
    pygame.draw.rect(screen, sky_blue, (170, 230, 30, 30))
    pygame.draw.rect(screen, sky_blue, (170, 270, 30, 30))
    pygame.draw.rect(screen, (210, 180, 140), (230, 310, 50, 85))
    pygame.draw.circle(screen, (105, 90, 70), (270, 350), 5)

    pygame.display.update()
    clock.tick(10)
