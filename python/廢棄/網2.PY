from random import randint as ri
import pygame


class Point:
    def __init__(self,x,y):
        self.s = (x,y)
        self.color = (ri(128,255),ri(128,255),ri(128,255))
        self.link_list = []
        d = 10000
        ex,ey = 0,0
        for i in point_list:
            new_d = ((self.s[0]-i.s[0])**2+(self.s[1]-i.s[1])**2)**0.5
            if d > new_d:
                d = new_d
                ex,ey = i.s[0],i.s[1]
        self.e = (ex,ey)
    def draw(self):
        pygame.draw.line(screen,self.color,self.s,self.e)
        pygame.draw.circle(screen,self.color,self.s,5,0)


pygame.init()
pygame.display.set_caption("網")
W = pygame.display.Info().current_w
H = pygame.display.Info().current_h
screen = pygame.display.set_mode((W,H), pygame.FULLSCREEN)
clock = pygame.time.Clock()
point_list = []
point_list.append(Point(round(W/2),round(H/2)))
point_list[0].e = (round(W/2),round(H/2))
t = 0

while True:
    t += 1
    mousex, mousey = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for i in point_list:
                    del i
                point_list = [Point(round(W/2),round(H/2))]
                point_list[0].e = (round(W/2),round(H/2))

    point_list.append(Point(ri(10,W-11),ri(10,H-11)))
    screen.fill((0,0,0))
    for i in point_list:
        i.draw()
    pygame.display.update()
    clock.tick(10)