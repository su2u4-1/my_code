from random import randint as ri
import pygame


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.color = (ri(128,255),ri(128,255),ri(128,255))
        self.link_list = []
    def draw_line(self):
        d = 10000
        x,y = 0,0
        for i in point_list:
            if self != i and i not in self.link_list:
                new_d = ((self.x-i.x)**2+(self.y-i.y)**2)**0.5
                if d > new_d:
                    d = new_d
                    x,y = i.x,i.y
                    link = i
        try:
            link.link_list.append(self)
        except:
            pass
        pygame.draw.line(screen,self.color,(self.x,self.y),(x,y))
    def draw_circle(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),5,0)


pygame.init()
pygame.display.set_caption("網")
W = pygame.display.Info().current_w
H = pygame.display.Info().current_h
screen = pygame.display.set_mode((W,H), pygame.FULLSCREEN)
clock = pygame.time.Clock()
point_list = []
t = 0

while True:
    t += 1
    mousex, mousey = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    point_list.append(Point(ri(10,W-11),ri(10,H-11)))
    screen.fill((0,0,0))
    for i in point_list:
        i.draw_line()
        i.draw_circle()
    pygame.display.update()
    clock.tick(10)