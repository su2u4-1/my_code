import keyboard
import time

t = 0.5


def key_board(t, a):
    if keyboard.is_pressed(a):
        print(a)
        time.sleep(t)
        return 1
    else:
        return 0


A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a = "abcdefghijklmnopqrstuvwxyz"

caps1 = 0
caps2 = 0
while True:
    if key_board(t, "shift"):
        caps2 = 1
    else:
        caps2 = 0
    # 大寫英文
    if caps1 + caps2 == 1:
        for i in A:
            key_board(t, i)
        if key_board(t, "caps lock"):
            caps1 = 0
    # 小寫英文
    if caps1 + caps2 == 0 or caps1 + caps2 > 1:
        for i in a:
            key_board(t, i)
        if key_board(t, "caps lock"):
            caps1 = 1
