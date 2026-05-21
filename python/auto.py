from time import sleep
from threading import Thread
import pyautogui
from pynput import keyboard

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = True
running: bool = False
i1 = (675, 557)
i2 = (742, 556)
g1 = (822, 435)
g2 = (756, 371)
g3 = (897, 360)
g4 = (815, 300)
a1 = (1242, 560)
a2 = (1183, 566)
a3 = (1099, 566)
a4 = (1042, 566)
c1 = (1234, 700)
c2 = (1148, 693)
c3 = (1112, 705)
c4 = (1035, 707)
b1 = (1235, 634)
b2 = (1173, 637)
b3 = (1088, 637)
b4 = (1011, 634)
b5 = (975, 633)
b6 = (893, 633)
r1 = (1138, 374)


def left(pos: tuple[int, int]) -> None:
    x, y = pos
    pyautogui.moveTo(x, y)
    sleep(0.03)
    pyautogui.mouseDown(button="left")
    sleep(0.02)
    pyautogui.mouseUp(button="left")
    sleep(0.08)


def right(pos: tuple[int, int]) -> None:
    x, y = pos
    pyautogui.moveTo(x, y)
    sleep(0.03)
    pyautogui.mouseDown(button="right")
    sleep(0.02)
    pyautogui.mouseUp(button="right")
    sleep(0.08)


def run_script() -> None:
    global running
    print("開始執行")
    # ===== 在這裡寫你的操作 =====
    left(i1)
    right(g1)
    left(i1)
    left(i2)
    right(g2)
    right(g3)
    right(g4)
    left(i2)
    left(r1)
    left(a1)

    left(i1)
    right(g2)
    left(i1)
    left(i2)
    right(g1)
    right(g3)
    right(g4)
    left(i2)
    left(r1)
    left(a2)

    left(i1)
    right(g3)
    left(i1)
    left(i2)
    right(g1)
    right(g2)
    right(g4)
    left(i2)
    left(r1)
    left(a3)

    left(i1)
    right(g4)
    left(i1)
    left(i2)
    right(g1)
    right(g2)
    right(g3)
    left(i2)
    left(r1)
    left(a4)
    # ==========================
    left(i2)
    right(g1)
    left(i2)
    left(i1)
    right(g2)
    right(g3)
    right(g4)
    left(i1)
    left(r1)
    left(c1)

    left(i2)
    right(g2)
    left(i2)
    left(i1)
    right(g1)
    right(g3)
    right(g4)
    left(i1)
    left(r1)
    left(c2)

    left(i2)
    right(g3)
    left(i2)
    left(i1)
    right(g1)
    right(g2)
    right(g4)
    left(i1)
    left(r1)
    left(c3)

    left(i2)
    right(g4)
    left(i2)
    left(i1)
    right(g1)
    right(g2)
    right(g3)
    left(i1)
    left(r1)
    left(c4)
    # ==========================
    left(i1)
    right(g1)
    right(g2)
    left(i1)
    left(i2)
    right(g3)
    right(g4)
    left(i2)
    left(r1)
    left(b1)

    left(i1)
    right(g2)
    right(g4)
    left(i1)
    left(i2)
    right(g1)
    right(g3)
    left(i2)
    left(r1)
    left(b2)

    left(i1)
    right(g3)
    right(g4)
    left(i1)
    left(i2)
    right(g1)
    right(g2)
    left(i2)
    left(r1)
    left(b3)

    left(i1)
    right(g1)
    right(g3)
    left(i1)
    left(i2)
    right(g2)
    right(g4)
    left(i2)
    left(r1)
    left(b4)
    # ==========================
    left(i1)
    right(g1)
    right(g4)
    left(i1)
    left(i2)
    right(g2)
    right(g3)
    left(i2)
    left(r1)
    left(b5)

    left(i1)
    right(g2)
    right(g3)
    left(i1)
    left(i2)
    right(g1)
    right(g4)
    left(i2)
    left(r1)
    left(b6)
    # ==========================
    print("執行完成")
    running = False


def start_script() -> None:
    Thread(target=run_script, daemon=True).start()


def on_press(key: keyboard.Key | keyboard.KeyCode | None) -> None:
    global running
    if running:
        return
    if isinstance(key, keyboard.KeyCode):
        if key.char == "p":
            running = True
            start_script()


print("按 P 開始")

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
