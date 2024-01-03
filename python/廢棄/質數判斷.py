print("質數判斷")
a = input("請輸入要判斷的數字:")
try:
    a = int(a)
except:
    print("Error")
    exit()
if a < 0:
    print("Error")
elif a == 2:
    print(True)
elif a == 1 or a == 0:
    print(False)
else:
    for i in range(3, a, 2):
        if a % i == 0:
            print(False)
            break
    else:
        print(True)
