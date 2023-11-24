import keyboard
import time

b = 0
t = 0.75


def key_board(t, a):
    while True:
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_DOWN and event.name == a:
            print(a)
            time.sleep(t)
            break


while b == 0:
    # 大寫英文
    key_board(t, a="A")
    key_board(t, a="B")
    key_board(t, a="C")
    key_board(t, a="D")
    key_board(t, a="E")
    key_board(t, a="F")
    key_board(t, a="G")
    key_board(t, a="H")
    key_board(t, a="I")
    key_board(t, a="J")
    key_board(t, a="K")
    key_board(t, a="L")
    key_board(t, a="M")
    key_board(t, a="N")
    key_board(t, a="O")
    key_board(t, a="P")
    key_board(t, a="Q")
    key_board(t, a="R")
    key_board(t, a="S")
    key_board(t, a="T")
    key_board(t, a="U")
    key_board(t, a="V")
    key_board(t, a="W")
    key_board(t, a="X")
    key_board(t, a="Y")
    key_board(t, a="Z")
    # 小寫英文
    key_board(t, a="a")
    key_board(t, a="b")
    key_board(t, a="c")
    key_board(t, a="d")
    key_board(t, a="e")
    key_board(t, a="f")
    key_board(t, a="g")
    key_board(t, a="h")
    key_board(t, a="i")
    key_board(t, a="j")
    key_board(t, a="k")
    key_board(t, a="l")
    key_board(t, a="m")
    key_board(t, a="n")
    key_board(t, a="o")
    key_board(t, a="p")
    key_board(t, a="q")
    key_board(t, a="r")
    key_board(t, a="s")
    key_board(t, a="t")
    key_board(t, a="u")
    key_board(t, a="v")
    key_board(t, a="w")
    key_board(t, a="x")
    key_board(t, a="y")
    key_board(t, a="z")
