import pygame, random, os.path

pygame.init()
pygame.mixer.init()
score = 0
W = pygame.display.Info().current_w
H = pygame.display.Info().current_h
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("gametest")
clock = pygame.time.Clock()
path = os.path.dirname(os.path.abspath(__file__))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path + "\\plane_up.png")
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect()
        self.rect.center = (W // 2, H * 4 // 5)
        self.speed_y = 3
        self.cd = 200
        self.hp = 100

    def update(self):
        keys = pygame.key.get_pressed()
        if gameing:
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
                bullet = Bullet(self.rect.centerx, self.rect.y)
                all_sprites.add(bullet)
                bullets.add(bullet)
                self.cd = 200


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path + "\\bullet.png")
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y + 30
        self.speed_y = -15

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()


class Red(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path + "\\redmonster_0.png")
        self.image = pygame.transform.scale(self.image, (130, 130))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, W - self.rect.width)
        self.rect.y = random.randrange(-1000, -400)
        self.speed_y = random.randrange(1, 6)
        self.speed_x = random.randrange(-2, 2)

    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.left > W:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = W
        if self.rect.top > H:
            self.rect.x = random.randrange(0, W - self.rect.width)
            self.rect.y = random.randrange(-1000, -400)
            self.speed_y = random.randrange(1, 6)


class Eyes(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path + "\\eyesmonster.png")
        self.image = pygame.transform.scale(self.image, (130, 130))
        self.rect = self.image.get_rect()
        self.cd = 200
        if random.randrange(0, 2) == 0:
            self.rect.x = random.randrange(-200, -50)
            self.left = True
        else:
            self.rect.x = W + random.randrange(20, 500)
            self.left = False

        self.rect.y = random.randrange(20, 300)
        self.speed_x = random.randrange(2, 5)

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
            ball = Ball(self.rect.centerx, self.rect.y)
            all_sprites.add(ball)
            balls.add(ball)
            self.cd = 400


class Ball(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path + "\\ball.png")
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y + 110
        self.speed_y = random.randrange(2, 4)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > H:
            self.kill()


def hpbar(surf: pygame.Surface, hp: int, x: int, y: int):
    if hp < 0:
        hp = 0
    bar_length = 200
    bar_height = 20
    fill = (hp / 100) * bar_length
    hpbox = pygame.Rect(x, y, bar_length, bar_height)
    hpin = pygame.Rect(x, y, fill, bar_height)
    if hp > 30:
        pygame.draw.rect(surf, (0, 255, 0), hpin)
    elif hp <= 30:
        pygame.draw.rect(surf, (255, 0, 0), hpin)
    pygame.draw.rect(surf, (255, 255, 255), hpbox, 2)


background_sound = pygame.mixer.Sound(path + "\\backgroundmusic.mp3")
background_sound.play()
startbut = pygame.image.load(path + "\\startbut.png")
main_page = True
gameing = False
gameover = False
background_image = pygame.image.load(path + "\\space.png")
all_sprites = pygame.sprite.Group()
reds = pygame.sprite.Group()
bullets = pygame.sprite.Group()
eyesll = pygame.sprite.Group()
balls = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(15):
    redmonster = Red()
    all_sprites.add(redmonster)
    reds.add(redmonster)
for i in range(10):
    eyes = Eyes()
    all_sprites.add(eyes)
    eyesll.add(eyes)

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
                gameing = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
    background_image = pygame.transform.scale(background_image, (W, H))
    screen.blit(background_image, (0, 0))
    if main_page:
        startbut = pygame.transform.scale(startbut, (180, 180))
        screen.blit(startbut, (W / 2 - 90, H / 2 - 100))
        font = pygame.font.Font(None, 200)
        txt = font.render("SPACEWAR", True, (255, 0, 0))
        screen.blit(txt, [W / 2 - 410, H / 2 - 250])
    if gameing:
        all_sprites.draw(screen)
    if gameover:
        gameover_image = pygame.image.load(path + "\\gameover.png")
        gameover_image = pygame.transform.scale(gameover_image, (W, H))
        screen.blit(gameover_image, (0, 0))
        font = pygame.font.Font(None, 200)
        txt = font.render(f"YOUR SCORE:{score}", True, (255, 255, 255))
        screen.blit(txt, [140, 360])
    if gameing:
        font = pygame.font.Font(None, 80)
        txt = font.render(f"SCORE:{score}", True, (255, 255, 255))
        screen.blit(txt, [0, 0])
        hpbar(screen, player.hp, W / 2 - 98, H - 20)
        all_sprites.update()
        shotdown_red = pygame.sprite.groupcollide(reds, bullets, True, True)
        for shots in shotdown_red:
            score += 3
            redmonster = Red()
            all_sprites.add(redmonster)
            reds.add(redmonster)
        shotdown_eye = pygame.sprite.groupcollide(eyesll, bullets, True, True)
        for shots in shotdown_eye:
            score += 5
            eyes = Eyes()
            all_sprites.add(eyes)
            eyesll.add(eyes)
        hurt1 = pygame.sprite.spritecollide(player, reds, False, pygame.sprite.collide_mask)
        hurt2 = pygame.sprite.spritecollide(player, balls, False, pygame.sprite.collide_mask)
        hurt3 = pygame.sprite.spritecollide(player, eyesll, False, pygame.sprite.collide_mask)
        if hurt1 or hurt2 or hurt3:
            player.hp -= 1
            if player.hp < 0:
                gameing = False
                gameover = True
    pygame.display.update()
    clock.tick(120)
