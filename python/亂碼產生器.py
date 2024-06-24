from random import randrange as rr
from time import sleep as sl

B = ["1234567890", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz", " ,./'[]=-`~!@#$%^&*()_+}{:?><\"|\\"]
A = [10, 26, 26, 32]

while True:
    for _ in range(rr(1, 48)):
        d = rr(0, 4)
        if d == 0:
            a = rr(19968, 40917)
            print(chr(a), end="")
        else:
            print(B[d - 1][rr(0, A[d - 1])], end="")
    print()
    sl(rr(1, 51) / 100)
