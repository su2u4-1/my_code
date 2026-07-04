from threading import Thread
from time import sleep
from typing import Iterable

from pynput import keyboard
import pyautogui

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = True
running = False
stop = False
# table
t1 = (760, 290)
t2 = (830, 290)
t3 = (900, 290)
t4 = (760, 360)
t5 = (830, 360)
t6 = (900, 360)
t7 = (760, 430)
t8 = (830, 430)
t9 = (900, 430)
# bag line 1
b1 = (670, 560)
b2 = (740, 560)
b3 = (810, 560)
b4 = (880, 560)
b5 = (950, 560)
b6 = (1030, 560)
b7 = (1100, 560)
b8 = (1170, 560)
b9 = (1240, 560)
# bag line 2
b10 = (670, 630)
b11 = (740, 630)
b12 = (810, 630)
b13 = (880, 630)
b14 = (950, 630)
b15 = (1030, 630)
b16 = (1100, 630)
b17 = (1170, 630)
b18 = (1240, 630)
# bag line 3
b19 = (670, 700)
b20 = (740, 700)
b21 = (810, 700)
b22 = (880, 700)
b23 = (950, 700)
b24 = (1030, 700)
b25 = (1100, 700)
b26 = (1170, 700)
b27 = (1240, 700)
# hot bar
h1 = (670, 800)
h2 = (740, 800)
h3 = (810, 800)
h4 = (880, 800)
h5 = (950, 800)
h6 = (1030, 800)
h7 = (1100, 800)
h8 = (1170, 800)
h9 = (1240, 800)
# result
result = (1135, 360)


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
    click(result, "left")
    click(pos, "left")


def run_script() -> None:
    global running
    try:
        print("開始執行")
        # ==========================
        for i in (b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21):
            put(b25, [t2])
            put(b26, [t4])
            put(b27, [t6])
            put(i, [t8])
            take(i)
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
