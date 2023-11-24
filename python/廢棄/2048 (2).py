import tkinter, random

root = tkinter.Tk()
root.title("2048")
a = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


def randomplace():
    global a
    x = random.randint(0, 3)
    y = random.randint(0, 3)
    a[x][y] = 1


def layout():
    global a, Up, Down, Left, Right
    i = 0
    for x in range(4):
        for y in range(4):
            globals()["la" + str(i)] = tkinter.Label(
                root,
                text=f"{2**(a[x][y])}",
                width=6,
                height=3,
                font=("Arial", 32),
                borderwidth=2,
                relief="ridge",
            )
            globals()["la" + str(i)].grid(row=x, column=y)
            i += 1
    Up = tkinter.Button(
        root, text="上", command=up, width=2, height=1, font=("Arial", 32)
    ).grid(row=0, column=4)
    Down = tkinter.Button(
        root, text="下", command=down, width=2, height=1, font=("Arial", 32)
    ).grid(row=1, column=4)
    Left = tkinter.Button(
        root, text="左", command=left, width=2, height=1, font=("Arial", 32)
    ).grid(row=2, column=4)
    Right = tkinter.Button(
        root, text="右", command=right, width=2, height=1, font=("Arial", 32)
    ).grid(row=3, column=4)


def left():
    print("左")
    global a
    try:
        for _ in range(3):
            for x in range(4):
                for y in range(1, 4):
                    if a[x][y - 1] == 0:
                        a[x][y - 1] = a[x][y]
                        a[x][y] == 0
                    elif a[x][y] == a[x][y - 1]:
                        a[x][y - 1] += 1
                        a[x][y] = 0
    except:
        print(x, y)
    detection()
    randomplace()
    layout()


def right():
    print("右")
    global a
    try:
        for _ in range(3):
            for x in range(4):
                for y in range(3):
                    if a[x][y + 1] == 0:
                        a[x][y + 1] = a[x][y]
                        a[x][y] == 0
                    elif a[x][y] == a[x][y + 1]:
                        a[x][y + 1] += 1
                        a[x][y] = 0
    except:
        print(x, y)
    detection()
    randomplace()
    layout()


def up():
    print("上")
    global a
    try:
        for _ in range(3):
            for x in range(1, 4):
                for y in range(4):
                    if a[x - 1][y] == 0:
                        a[x - 1][y] = a[x][y]
                        a[x][y] == 0
                    elif a[x][y] == a[x - 1][y]:
                        a[x - 1][y] += 1
                        a[x][y] = 0
    except:
        print(x, y)
    detection()
    randomplace()
    layout()


def down():
    print("下")
    global a
    try:
        for _ in range(3):
            for x in range(3):
                for y in range(4):
                    if a[x + 1][y] == 0:
                        a[x + 1][y] = a[x][y]
                        a[x][y] == 0
                    elif a[x][y] == a[x + 1][y]:
                        a[x + 1][y] += 1
                        a[x][y] = 0
    except:
        print(x, y)
    detection()
    randomplace()
    layout()


def detection():
    print("偵測")


randomplace()
randomplace()
layout()
detection()
root.mainloop()
