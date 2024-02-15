import pygame

# pygame初始化
pygame.init()
# 設定視窗名稱
pygame.display.set_caption("視窗名稱")
# 取得螢幕長寬,參考https://www.pygame.org/docs/ref/display.html#pygame.display.Info
W = pygame.display.Info().current_w
H = pygame.display.Info().current_h
# 建立視窗,pygame.FULLSCREEN是全螢幕,參考https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode
screen = pygame.display.set_mode((W, H), pygame.FULLSCREEN)
# 建立時間物件，讓遊戲可以更新畫面
clock = pygame.time.Clock()
# 建立文字物件，讓文字可以顯示，但無法使用中文
font = pygame.font.Font(None, 30)
# 可以使用中文的方式，字體路徑要檢查一下，但基本上不會變化
# font = pygame.font.Font('C:\\Windows\\Fonts\\kaiu.ttf',48)

# 遊戲主迴圈
while True:
    # 取得滑鼠座標
    mousex, mousey = pygame.mouse.get_pos()
    # 處理事件的迴圈
    for event in pygame.event.get():
        # 如果視窗被關閉
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # 當滑鼠被按下
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 滑鼠是否被按下,0是左鍵,1是中鍵,2是右鍵,回傳值是bool
            if pygame.mouse.get_pressed()[0]:
                pass
        # 如果鍵盤被按下
        elif event.type == pygame.KEYDOWN:
            # 如果A被按下
            if event.key == pygame.K_a:
                pass
    # 清空畫面且填滿底色
    screen.fill((255, 255, 255))
    # 導入圖片
    img = pygame.image.load("name.png")
    # 畫方形(視窗或畫布,顏色(r,g,b),座標(起點x,起點y,x軸邊長,y軸邊長),寬度(預設為0,表示填滿))
    # 其他形狀請參考https://www.pygame.org/docs/ref/draw.html
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, 20, 20), 3)
    # 定義文字物件(文字內容,我也不知道這個True是幹嘛的,顏色(r,g,b))
    text = font.render("text", True, (0, 0, 0))
    # 顯示物件(物件,[x座標,y座標])
    screen.blit(img, [30, 30])
    screen.blit(text, [30, 60])
    # 更新畫面
    pygame.display.update()
    # 設定畫面跟新率
    clock.tick(10)

# 其餘請參考https://www.pygame.org/docs/
