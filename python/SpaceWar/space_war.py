from __future__ import annotations

from os.path import dirname, abspath
from random import randrange
from typing import Any

import pygame

pygame.init()
score = 0
W = pygame.display.Info().current_w
H = pygame.display.Info().current_h
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("game test")
clock = pygame.time.Clock()
path = dirname(abspath(__file__))


class GameSprite(pygame.sprite.Sprite):
    image: pygame.Surface
    rect: pygame.Rect


class Player(GameSprite):
    def __init__(self, *args: pygame.sprite.AbstractGroup[Any]):
        super().__init__(*args)
        self.image = pygame.image.load(path + "\\plane_up.png")
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect()
        self.rect.center = (W // 2, H * 4 // 5)
        self.speed_y = 3
        self.cd = 200
        self.hp = 100

    def update(self):
        keys = pygame.key.get_pressed()
        if gaming:
            if keys[pygame.K_w]:
                self.rect.y -= self.speed_y
            if keys[pygame.K_s]:
                self.rect.y += self.speed_y
            if keys[pygame.K_a]:
                self.rect.x -= self.speed_y
            if keys[pygame.K_d]:
                self.rect.x += self.speed_y
            if self.rect.left > W:
                self.rect.right = 0
            if self.rect.right < 0:
                self.rect.left = W
            if self.rect.bottom < 0:
                self.rect.top = H
            if self.rect.top > H:
                self.rect.bottom = 0

        self.cd -= 6
        if keys[pygame.K_SPACE]:
            if self.cd < 0:
                bullet = Bullet.spawn(self.rect.centerx, self.rect.y)
                all_sprites.add(bullet)
                bullets.add(bullet)
                self.cd = 200


class Bullet(GameSprite):
    def __init__(self, *args: pygame.sprite.AbstractGroup[Any]):
        super().__init__(*args)
        self.image = pygame.image.load(path + "\\bullet.png")
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.speed_y = -15

    @classmethod
    def spawn(cls, x: int, y: int, *args: pygame.sprite.AbstractGroup[Any]) -> "Bullet":
        bullet = cls(*args)
        bullet.rect.centerx = x
        bullet.rect.bottom = y + 30
        return bullet

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()


class Red(GameSprite):
    def __init__(self, *args: pygame.sprite.AbstractGroup[Any]):
        super().__init__(*args)
        self.image = pygame.image.load(path + "\\red_monster_0.png")
        self.image = pygame.transform.scale(self.image, (130, 130))
        self.rect = self.image.get_rect()
        self.rect.x = randrange(0, W - self.rect.width)
        self.rect.y = randrange(-1000, -400)
        self.speed_y = randrange(1, 6)
        self.speed_x = randrange(-2, 2)

    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.left > W:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = W
        if self.rect.top > H:
            self.rect.x = randrange(0, W - self.rect.width)
            self.rect.y = randrange(-1000, -400)
            self.speed_y = randrange(1, 6)


class Eyes(GameSprite):
    def __init__(self, *args: pygame.sprite.AbstractGroup[Any]):
        super().__init__(*args)
        self.image = pygame.image.load(path + "\\eyes_monster.png")
        self.image = pygame.transform.scale(self.image, (130, 130))
        self.rect = self.image.get_rect()
        self.cd = 200
        if randrange(0, 2) == 0:
            self.rect.x = randrange(-200, -50)
            self.left = True
        else:
            self.rect.x = W + randrange(20, 500)
            self.left = False

        self.rect.y = randrange(20, 300)
        self.speed_x = randrange(2, 5)

    def update(self):
        self.cd -= 4
        if self.left == True:
            self.rect.x += self.speed_x
            if self.rect.left > W:
                self.rect.right = -50
        elif self.left == False:
            self.rect.x -= self.speed_x
            if self.rect.right < 0:
                self.rect.right = W + 50
        if self.cd < 0:
            ball = Ball.spawn(self.rect.centerx, self.rect.y)
            all_sprites.add(ball)
            balls.add(ball)
            self.cd = 400


class Ball(GameSprite):
    def __init__(self, *args: pygame.sprite.AbstractGroup[Any]):
        super().__init__(*args)
        self.image = pygame.image.load(path + "\\ball.png")
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.speed_y = randrange(2, 4)

    @classmethod
    def spawn(cls, x: int, y: int, *args: pygame.sprite.AbstractGroup[Any]) -> "Ball":
        ball = cls(*args)
        ball.rect.centerx = x
        ball.rect.bottom = y + 110
        return ball

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > H:
            self.kill()


def hp_bar(surf: pygame.Surface, hp: int, x: int, y: int):
    if hp < 0:
        hp = 0
    bar_length = 200
    bar_height = 20
    fill = (hp / 100) * bar_length
    hp_box = pygame.Rect(x, y, bar_length, bar_height)
    h_pin = pygame.Rect(x, y, fill, bar_height)
    if hp > 30:
        pygame.draw.rect(surf, (0, 255, 0), h_pin)
    elif hp <= 30:
        pygame.draw.rect(surf, (255, 0, 0), h_pin)
    pygame.draw.rect(surf, (255, 255, 255), hp_box, 2)


background_sound = pygame.mixer.Sound(path + "\\background_music.mp3")
background_sound.play()
start_but = pygame.image.load(path + "\\start_but.png")
main_page = True
gaming = False
game_over = False
background_image = pygame.image.load(path + "\\space.png")
all_sprites: pygame.sprite.Group[GameSprite] = pygame.sprite.Group()
reds: pygame.sprite.Group[Red] = pygame.sprite.Group()
bullets: pygame.sprite.Group[Bullet] = pygame.sprite.Group()
eye_sll: pygame.sprite.Group[Eyes] = pygame.sprite.Group()
balls: pygame.sprite.Group[Ball] = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(15):
    red_monster = Red()
    all_sprites.add(red_monster)
    reds.add(red_monster)
for i in range(10):
    eyes = Eyes()
    all_sprites.add(eyes)
    eye_sll.add(eyes)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if W / 2 - 85 <= mouse_pos[0] <= W / 2 + 85 and H / 2 - 47 <= mouse_pos[1] <= H / 2 + 47:
                button_state = True
                main_page = False
                gaming = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
    background_image = pygame.transform.scale(background_image, (W, H))
    screen.blit(background_image, (0, 0))
    if main_page:
        start_but = pygame.transform.scale(start_but, (180, 180))
        screen.blit(start_but, (W / 2 - 90, H / 2 - 100))
        font = pygame.font.Font(None, 200)
        txt = font.render("space war", True, (255, 0, 0))
        screen.blit(txt, [W / 2 - 410, H / 2 - 250])
    if gaming:
        all_sprites.draw(screen)
    if game_over:
        game_over_image = pygame.image.load(path + "\\game_over.png")
        game_over_image = pygame.transform.scale(game_over_image, (W, H))
        screen.blit(game_over_image, (0, 0))
        font = pygame.font.Font(None, 200)
        txt = font.render(f"YOUR SCORE:{score}", True, (255, 255, 255))
        screen.blit(txt, [140, 360])
    if gaming:
        font = pygame.font.Font(None, 80)
        txt = font.render(f"SCORE:{score}", True, (255, 255, 255))
        screen.blit(txt, [0, 0])
        hp_bar(screen, player.hp, W // 2 - 98, H - 20)
        all_sprites.update()
        shot_down_red = pygame.sprite.groupcollide(reds, bullets, True, True)
        for shots in shot_down_red:
            score += 3
            red_monster = Red()
            all_sprites.add(red_monster)
            reds.add(red_monster)
        shot_down_eye = pygame.sprite.groupcollide(eye_sll, bullets, True, True)
        for shots in shot_down_eye:
            score += 5
            eyes = Eyes()
            all_sprites.add(eyes)
            eye_sll.add(eyes)
        hurt1 = pygame.sprite.spritecollide(player, reds, False, pygame.sprite.collide_mask)
        hurt2 = pygame.sprite.spritecollide(player, balls, False, pygame.sprite.collide_mask)
        hurt3 = pygame.sprite.spritecollide(player, eye_sll, False, pygame.sprite.collide_mask)
        if hurt1 or hurt2 or hurt3:
            player.hp -= 1
            if player.hp < 0:
                gaming = False
                game_over = True
    pygame.display.update()
    clock.tick(120)
