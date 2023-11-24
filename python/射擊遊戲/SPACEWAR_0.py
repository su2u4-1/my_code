import pygame, random, sys

# 初始化 pygame
pygame.init()
pygame.mixer.init()
score = 0

display_width = pygame.display.Info().current_w
display_height = pygame.display.Info().current_h

# 建立視窗
screen = pygame.display.set_mode((display_width, display_height))

# 視窗名稱
pygame.display.set_caption("gametest")

# 遊戲介面
startbut = pygame.image.load("python\\射擊遊戲\\startbut.png")
main_page = True
gameing = False
gameover = False


# 角色
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("python\\射擊遊戲\\plane_up.png")
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect()
        self.rect.center = (display_width / 2, display_height * 4 / 5)
        self.speed_y = 3
        self.cd = 200
        self.hp = 100

    def update(self):
        # 角色移動
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
            if self.rect.left > display_width:
                self.rect.right = 0
            if self.rect.right < 0:
                self.rect.left = display_width
            if self.rect.bottom < 0:
                self.rect.top = display_height
            if self.rect.top > display_height:
                self.rect.bottom = 0

        # 射擊
        self.cd -= 6
        if keys[pygame.K_SPACE]:
            if self.cd < 0:
                bullet = Bullet(self.rect.centerx, self.rect.y)
                all_sprites.add(bullet)
                bullets.add(bullet)
                self.cd = 200


# 子彈
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("python\\射擊遊戲\\bullet.png")
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y + 30
        self.speed_y = -15

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()


# 紅色敵人
class Red(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("python\\射擊遊戲\\redmonster_0.png")
        self.image = pygame.transform.scale(self.image, (130, 130))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, display_width - self.rect.width)
        self.rect.y = random.randrange(-1000, -400)
        self.speed_y = random.randrange(1, 6)
        self.speed_x = random.randrange(-2, 2)

    def update(self):
        # 怪物移動
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.left > display_width:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = display_width
        if self.rect.top > display_height:
            self.rect.x = random.randrange(0, display_width - self.rect.width)
            self.rect.y = random.randrange(-1000, -400)
            self.speed_y = random.randrange(1, 6)


# 眼睛敵人
class Eyes(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("python\\射擊遊戲\\eyesmonster.png")
        self.image = pygame.transform.scale(self.image, (130, 130))
        self.rect = self.image.get_rect()
        self.cd = 200
        if random.randrange(0, 2) == 0:
            self.rect.x = random.randrange(-200, -50)
            self.left = True
        else:
            self.rect.x = display_width + random.randrange(20, 500)
            self.left = False

        self.rect.y = random.randrange(20, 300)
        self.speed_x = random.randrange(2, 5)

    def update(self):
        # 怪物移動
        self.cd -= 4
        if self.left == True:
            self.rect.x += self.speed_x
            if self.rect.left > display_width:
                self.rect.right = -50
        elif self.left == False:
            self.rect.x -= self.speed_x
            if self.rect.right < 0:
                self.rect.right = display_width + 50
        if self.cd < 0:
            ball = Ball(self.rect.centerx, self.rect.y)
            all_sprites.add(ball)
            balls.add(ball)
            self.cd = 400


# 魔法球
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("python\\射擊遊戲\\ball.png")
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y + 110
        self.speed_y = random.randrange(2, 4)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > display_height:
            self.kill()


# hp條
def hpbar(surf, hp, x, y):
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


# 設定遊戲時鐘
clock = pygame.time.Clock()

# 載入圖片
background_image = pygame.image.load("python\\射擊遊戲\\space.png")

# 物件
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

# 背景音樂
background_sound = pygame.mixer.Sound("python\\射擊遊戲\\backgroundmusic.mp3")
background_sound.play()

# 建立主遊戲迴圈
while True:
    # 控制遊戲更新速度
    clock.tick(120)
    # 事件迴圈
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # startbut
            if (
                display_width / 2 - 85 <= mouse_pos[0] <= display_width / 2 + 85
                and display_height / 2 - 47 <= mouse_pos[1] <= display_height / 2 + 47
            ):
                button_state = True
                main_page = False
                gameing = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    # 背景
    background_image = pygame.transform.scale(
        background_image, (display_width, display_height)
    )
    screen.blit(background_image, (0, 0))

    # 主頁面
    if main_page:
        startbut = pygame.transform.scale(startbut, (180, 180))
        screen.blit(startbut, (display_width / 2 - 90, display_height / 2 - 100))
        font = pygame.font.Font(None, 200)
        txt = font.render("SPACEWAR", True, (255, 0, 0))
        screen.blit(txt, [display_width / 2 - 410, display_height / 2 - 250])

    # gamemode
    if gameing:
        # 遊戲更新
        all_sprites.draw(screen)

    # gameover
    if gameover:
        gameover_image = pygame.image.load("python\\射擊遊戲\\gameover.png")
        gameover_image = pygame.transform.scale(
            gameover_image, (display_width, display_height)
        )
        screen.blit(gameover_image, (0, 0))
        font = pygame.font.Font(None, 200)
        txt = font.render(f"YOUR SCORE:{score}", True, (255, 255, 255))
        screen.blit(txt, [140, 360])

    # 分數/重新生成
    if gameing:
        # 字體
        font = pygame.font.Font(None, 80)
        txt = font.render(f"SCORE:{score}", True, (255, 255, 255))
        screen.blit(txt, [0, 0])
        hpbar(screen, player.hp, display_width / 2 - 98, display_height - 20)
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
        # hp
        hurt1 = pygame.sprite.spritecollide(
            player, reds, False, pygame.sprite.collide_mask
        )
        hurt2 = pygame.sprite.spritecollide(
            player, balls, False, pygame.sprite.collide_mask
        )
        hurt3 = pygame.sprite.spritecollide(
            player, eyesll, False, pygame.sprite.collide_mask
        )
        if hurt1 or hurt2 or hurt3:
            player.hp -= 1
            if player.hp < 0:
                gameing = False
                gameover = True
    pygame.display.update()
