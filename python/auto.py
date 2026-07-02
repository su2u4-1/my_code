from threading import Thread
from time import sleep
from typing import Iterable

from pynput import keyboard
import pyautogui

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = True
running = False
stop = False
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


def click(pos: tuple[int, int], button: str) -> None:
    if stop:
        raise Exception()
    x, y = pos
    pyautogui.moveTo(x, y)
    sleep(0.01)
    pyautogui.mouseDown(button=button)
    sleep(0.01)
    pyautogui.mouseUp(button=button)
    sleep(0.01)


def put(pos1: tuple[int, int], other_pos: Iterable[tuple[int, int]]) -> None:
    """put pos1 to other_pos"""
    click(pos1, "left")
    for pos2 in other_pos:
        click(pos2, "right")
    click(pos1, "left")


def take(pos: tuple[int, int]) -> None:
    """take result(r1) to pos"""
    click(r1, "left")
    click(pos, "left")


def run_script() -> None:
    global running
    try:
        print("開始執行")
        # ===== 在這裡寫你的操作 =====
        put(i1, [g1])
        put(i2, [g2, g3, g4])
        take(a1)

        put(i1, [g2])
        put(i2, [g1, g3, g4])
        take(a2)

        put(i1, [g3])
        put(i2, [g1, g2, g4])
        take(a3)

        put(i1, [g4])
        put(i2, [g1, g2, g3])
        take(a4)
        # ==========================
        put(i2, [g1])
        put(i1, [g2, g3, g4])
        take(c1)

        put(i2, [g2])
        put(i1, [g1, g3, g4])
        take(c2)

        put(i2, [g3])
        put(i1, [g1, g2, g4])
        take(c3)

        put(i2, [g4])
        put(i1, [g1, g2, g3])
        take(c4)
        # ==========================
        put(i1, [g1, g2])
        put(i2, [g3, g4])
        take(b1)

        put(i1, [g2, g4])
        put(i2, [g1, g3])
        take(b2)

        put(i1, [g3, g4])
        put(i2, [g1, g2])
        take(b3)

        put(i1, [g1, g3])
        put(i2, [g2, g4])
        take(b4)
        # ==========================
        put(i1, [g1, g4])
        put(i2, [g2, g3])
        take(b5)

        put(i1, [g2, g3])
        put(i2, [g1, g4])
        take(b6)
        # ==========================
        print("執行完成\n")
    except Exception:
        print("已停止\n")
    running = False


def start_script() -> None:
    Thread(target=run_script, daemon=True).start()


def on_press(key: keyboard.Key | keyboard.KeyCode | None) -> None:
    global running, stop
    if key == keyboard.Key.esc:
        stop = True
        return
    if running:
        return
    if isinstance(key, keyboard.KeyCode) and key.char == "p":
        stop = False
        running = True
        start_script()


print("按 P 開始")

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
