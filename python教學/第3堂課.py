# 載入模組
import pygame

# 載入math模組的floor函式且命名為fl
from math import floor as fl


# 確認是否有人獲勝
def checking():
    # 宣告全域變數
    global gameContinue, winner
    # 八個方向
    a = [1, 1, 1, 0, 0, -1, -1, -1]
    b = [-1, 0, 1, -1, 1, -1, 0, 1]
    # 計算空白格的數量
    n = 0
    # 讓每個方塊都執行到
    for x in range(sl):
        for y in range(sl):
            # 判斷是黑棋還是白棋
            if chessBoard[x][y] == 1:
                # 讓八個方向都跑過一次
                for i in range(8):
                    # 定義座標
                    x1 = x
                    y1 = y
                    # 總共要連五個棋子，所以要跑四次
                    for _ in range(4):
                        # 如過下一格會超出棋盤範圍就退出
                        if x1 + a[i] < 0 or x1 + a[i] > 14 or y1 + b[i] < 0 or y1 + b[i] > 14:
                            break
                        # 如果下一格不是同色的棋子就退出
                        elif chessBoard[x1 + a[i]][y1 + b[i]] != 1:
                            break
                        # 把座標往方向移動一格
                        x1 += a[i]
                        y1 += b[i]
                    # 如果完整跑完for迴圈沒有退出就執行
                    else:
                        # 讓雙方無法繼續下棋
                        gameContinue = False
                        # 輸出獲勝訊息
                        winner = "Black wins"
                        print("黑方獲勝")
                        print(f"({x},{y})-({x1},{y1})\n")
                        # 回傳獲勝的座標並退出函式
                        return [
                            (x * 44 + 28, y * 44 + 28),
                            (x1 * 44 + 28, y1 * 44 + 28),
                        ]
            # 跟上面一樣
            elif chessBoard[x][y] == 2:
                for i in range(8):
                    x1 = x
                    y1 = y
                    for _ in range(4):
                        if x1 + a[i] < 0 or x1 + a[i] > 14 or y1 + b[i] < 0 or y1 + b[i] > 14:
                            break
                        elif chessBoard[x1 + a[i]][y1 + b[i]] != 2:
                            break
                        x1 += a[i]
                        y1 += b[i]
                    else:
                        gameContinue = False
                        winner = "White wins"
                        print("白方獲勝")
                        print(f"({x},{y})-({x1},{y1})\n")
                        return [
                            (x * 44 + 28, y * 44 + 28),
                            (x1 * 44 + 28, y1 * 44 + 28),
                        ]
            # 如果是空格n就加一
            else:
                n += 1
    # 如果沒有空格且沒有人獲勝
    if n == 0:
        # 讓雙方無法繼續下棋
        gameContinue = False
        # 輸出平手消息
        winner = "draw"
        print("平手")
        # 退出函式
        return


# 遊戲主程式
def main():
    # 宣告全域變數
    global chessBoard, gameContinue, winner, sl
    # 設定變數
    winner = ""
    mx = 0
    my = 0
    first = 0
    gameContinue = True
    sl = 15
    # pygame初始化(使用pygame時一定要記的先初始化)
    pygame.init()
    # 設定視窗名稱
    pygame.display.set_caption("五子棋")
    # 設定視窗大小、模式
    screen = pygame.display.set_mode((670, 700), pygame.RESIZABLE)
    # 設定時間物件(等一下設定畫面更新速度會用到)
    clock = pygame.time.Clock()
    # 設定字體(如果要顯示文字就要)
    font = pygame.font.Font(None, 30)
    # 建立棋盤
    chessBoard = []
    for _ in range(sl):
        a = []
        for _ in range(sl):
            a.append(0)
        chessBoard.append(a)

    # 主迴圈
    while True:
        # 取得滑鼠座標
        mousex, mousey = pygame.mouse.get_pos()
        mx = fl(mousex / 44)
        my = fl(mousey / 44)
        # 事件迴圈
        for event in pygame.event.get():
            # 如果視窗被關閉
            if event.type == pygame.QUIT:
                # 關閉pygame
                pygame.quit()
                # 關閉此程式
                exit()
            # 如果滑鼠被按下且左鍵是被按下的狀態
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                # 判斷遊戲是否正在進行中
                if gameContinue:
                    # 如過出錯
                    try:
                        # 如果選中的格子沒有棋子
                        if chessBoard[mx][my] == 0:
                            first += 1
                            # 判斷是黑下還是白下
                            if first % 2 == 1:
                                # 下棋
                                chessBoard[mx][my] = 1
                            else:
                                # 下棋
                                chessBoard[mx][my] = 2
                    # 就跳過
                    except:
                        pass
                # 如果游標接觸到離開遊戲按鈕
                if 60 < mousex < 120 and 670 < mousey:
                    # 離開遊戲
                    print("exit game")
                    exit()
                # 如果游標接觸到重開遊戲按鈕
                if mousex < 60 and 670 < mousey:
                    # 重開遊戲
                    print("reset game\n")
                    main()
        # 填畫面的底色
        screen.fill((238, 154, 73))
        # 繪製格線
        for i in range(sl):
            if i == 0 or i == sl - 1:
                pygame.draw.line(screen, (0, 0, 0), [i * 44 + 27, 27], [i * 44 + 27, 670 - 27], 4)
                pygame.draw.line(screen, (0, 0, 0), [27, i * 44 + 27], [670 - 27, i * 44 + 27], 4)
            else:
                pygame.draw.line(screen, (0, 0, 0), [i * 44 + 27, 27], [i * 44 + 27, 670 - 27], 2)
                pygame.draw.line(screen, (0, 0, 0), [27, i * 44 + 27], [670 - 27, i * 44 + 27], 2)
        # 繪製棋子
        for i in range(sl):
            for j in range(sl):
                # 黑方
                if chessBoard[i][j] == 1:
                    pygame.draw.circle(screen, (0, 0, 0), (i * 44 + 28, j * 44 + 28), 13)
                # 白方
                elif chessBoard[i][j] == 2:
                    pygame.draw.circle(screen, (255, 255, 255), (i * 44 + 28, j * 44 + 28), 13)
        # 判斷遊戲是否正在進行中
        if gameContinue:
            # 確認是否有人獲勝
            winner_line = checking()
        # 判斷是誰要下棋
        if first % 2 == 0:
            turn = "Black"
            # 繪製跟隨游標的框
            pygame.draw.circle(screen, (0, 0, 0), (mx * 44 + 28, my * 44 + 28), 15, width=3)
        else:
            turn = "White"
            # 繪製跟隨游標的框
            pygame.draw.circle(screen, (255, 255, 255), (mx * 44 + 28, my * 44 + 28), 15, width=3)
        # 如果遊戲已結束中且有人勝利
        if not gameContinue and type(winner_line) == list:
            # 繪製勝利方獲勝的位置
            pygame.draw.line(screen, (255, 0, 0), winner_line[0], winner_line[1], width=3)
        # 繪製重開遊戲的按鈕框
        pygame.draw.rect(screen, (0, 0, 0), (0, 670, 60, 30), 5)
        # 重開遊戲按鈕的文字
        screen.blit(font.render("reset", True, (0, 0, 0)), [5, 675])
        # 繪製離開遊戲的按鈕框
        pygame.draw.rect(screen, (0, 0, 0), (60, 670, 60, 30), 5)
        # 離開遊戲按鈕的文字
        screen.blit(font.render("exit", True, (0, 0, 0)), [70, 675])
        # 如果游標接觸到離開遊戲按鈕
        if 60 < mousex < 120 and 670 < mousey:
            # 把按鈕框變成白色的
            pygame.draw.rect(screen, (255, 255, 255), (60, 670, 60, 30), 5)
        # 如果游標接觸到重開遊戲按鈕
        if mousex < 60 and 670 < mousey:
            # 把按鈕框變成白色的
            pygame.draw.rect(screen, (255, 255, 255), (0, 670, 60, 30), 5)
        # 判斷遊戲是否正在進行中
        if gameContinue:
            # 設定下方顯示滑鼠座標和換誰下棋
            text = font.render(f"({mx},{my})  {turn}", True, (0, 0, 0))
        else:
            # 設定下方顯示滑鼠座標和誰贏了
            text = font.render(f"({mx},{my})  {winner}", True, (0, 0, 0))
        # 展示文字
        screen.blit(text, [125, 675])
        # 更新畫面
        pygame.display.update()
        # 畫面更新速度
        clock.tick(100)


# 當程式開始執行
if __name__ == "__main__":
    # 遊戲主程式
    main()
