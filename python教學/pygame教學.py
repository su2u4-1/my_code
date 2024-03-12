# 記得改檔名
# 因為如果這個檔案叫pygame的話
# 以後你在別的地方使用import pygame的話
# python就會呼叫這個檔案
# 而不是正確的pygame模組
# 所以記得把這個檔案改成一個你自己取的名字

import pygame

# pygame初始化
pygame.init()
# 設定視窗名稱
pygame.display.set_caption("視窗名稱")
# 取得螢幕長寬,參考https://www.pygame.org/docs/ref/display.html#pygame.display.Info
W = pygame.display.Info().current_w
H = pygame.display.Info().current_h
# 建立視窗,pygame.FULLSCREEN是全螢幕,其他參數請參考https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
# 建立時間物件,讓遊戲可以更新畫面
clock = pygame.time.Clock()
# 建立文字物件,讓文字可以顯示,但無法使用中文
font = pygame.font.Font(None, 20)
# 可以使用中文的方式,字體路徑要檢查一下,但基本上不會變化
font = pygame.font.Font("C:\\Windows\\Fonts\\kaiu.ttf", 30)

# 遊戲主迴圈
while True:
    # 取得滑鼠座標
    mousex, mousey = pygame.mouse.get_pos()
    # 處理事件的迴圈
    for event in pygame.event.get():
        # 如果視窗被關閉
        if event.type == pygame.QUIT:
            # 關閉pygame
            pygame.quit()
            # 關閉程式
            exit()
        # 如果滑鼠被按下:MOUSEBUTTONDOWN
        # 如果滑鼠被放開:MOUSEBUTTONUP
        # 如果滑鼠滾輪向下滾動:MOUSEBUTTONDOWN
        # 如果滑鼠滾輪向上滾動:MOUSEBUTTONUP
        # 如果滑鼠移動:MOUSEMOTION
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 滑鼠是否被按下,0是左鍵,1是中鍵,2是右鍵,回傳值是True或False
            if pygame.mouse.get_pressed()[0]:
                pass
        # 如果鍵盤被按下
        elif event.type == pygame.KEYDOWN:
            # 如果按下的是esc鍵
            # 各按鍵的值請參考https://www.pygame.org/docs/ref/key.html#key-constants-label
            if event.key == pygame.K_ESCAPE:
                # 關閉遊戲
                pygame.quit()
                exit()
    # 清空畫面且填滿底色(紅(0~255),綠(0~255),藍(0~255))
    screen.fill((255, 255, 255))
    # 導入圖片(圖片路徑+檔名) (記得自己找個圖片放上去,不然他會說找不到圖片)
    img = pygame.image.load("python教學\\name.png")
    # 畫方形(視窗或畫布,顏色(r,g,b),座標(起點x,起點y,x軸邊長,y軸邊長),寬度(預設為0,表示填滿))
    # 其他形狀請參考https://www.pygame.org/docs/ref/draw.html
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, 20, 20), 3)
    # 取得此畫布的大小,回傳tuple(w, h)
    size = screen.get_size()
    # 定義文字物件(文字內容,是否要開啟抗鋸齒,文字顏色(r,g,b),背景顏色(r,g,b)(這項可以不設))
    # text0顯示螢幕長寬(紅底黑字)
    text0 = font.render(str(size), True, (0, 0, 0), (255, 0, 0))
    # text1顯示滑鼠座標(白底黑字)
    text1 = font.render(f"({mousex},{mousey})", True, (0, 0, 0))
    # 顯示物件(物件,[x座標,y座標])
    screen.blit(img, [30, 30])
    screen.blit(text0, [30, 60])
    screen.blit(text1, [30, 90])
    # 更新畫面
    pygame.display.update()
    # 設定每秒幀數上限,不給或給0代表無限制(有時候會很吃電腦效能)
    clock.tick(10)

# 其餘請參考https://www.pygame.org/docs/
