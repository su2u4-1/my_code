import tkinter, time
from PIL import Image, ImageTk


def game_start():
    global c
    gametitle["text"] = "遊戲開始中"
    c = 1


def rotate():
    global image, c
    while c == 1:
        for _ in range(1, 50):
            time.sleep(0.1)
            newimage = image.rotate(-5)
            img2 = ImageTk.PhotoImage(newimage)
            canvas.create_image(155, 155, image=img2)  # type: ignore
            image = newimage
        gametitle["text"] = "歡迎遊玩[遊戲名]"
        c = 0
    root.after(1000, rotate)


def game_set_up():
    gametitle["text"] = "設定介面"


c = 0
root = tkinter.Tk()
root.title("遊戲")
a = root.winfo_screenwidth()
b = root.winfo_screenheight()
root.state("zoomed")
print(a, b)
gametitle = tkinter.Label(root, text="歡迎遊玩[遊戲名]", font=("Adobe 仿宋 Std R", 24))
gamestart = tkinter.Button(root, text="遊戲開始", font=("Adobe 仿宋 Std R", 24), command=game_start)
gamesetup = tkinter.Button(root, text="遊戲設定", font=("Adobe 仿宋 Std R", 24), command=game_set_up)
canvas = tkinter.Canvas(root, width="310", height="310")
img = tkinter.PhotoImage(file="五行.png")
image = Image.open("太極.png")
img2 = ImageTk.PhotoImage(image)
TaiChi = tkinter.Button(root, text="太極", command=exit, image=img2)
gametitle.pack(side="top", pady="100")
canvas.pack()
canvas.create_image(155, 155, image=img)  # type: ignore
canvas.create_image(155, 155, image=img2)  # type: ignore
TaiChi.pack(side="bottom", padx="250")
gamesetup.pack(side="right", padx="250")
gamestart.pack(side="left", padx="250")
root.after(1000, rotate)
root.mainloop()
