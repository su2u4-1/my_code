from random import randint as ri
from time import sleep as sl

b1 = "1234567890"
b2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
b3 = "abcdefghijklmnopqrstuvwxyz"
b4 = " ,./'[]=-`~!@#$%^&*()_+}{:?><\"|\\"

while True:
    for _ in range(ri(1, 48)):
        d = ri(0, 4)
        if d == 0:
            a = ri(19968, 40917)
            print(chr(a), end="")
        elif d == 1:
            c = ri(0, 9)
            print(b1[c], end="")
        elif d == 2:
            c = ri(0, 25)
            print(b2[c], end="")
        elif d == 3:
            c = ri(0, 25)
            print(b3[c], end="")
        elif d == 4:
            c = ri(0, 31)
            print(b4[c], end="")
    print()
    sl(ri(1, 50) / 100)
