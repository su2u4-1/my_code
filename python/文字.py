f = open("中文字.txt", "w+", encoding="utf8")
for i in range(19968, 40918):
    try:
        print(chr(i), "<-", i)
        f.write(f"{chr(i)} <- {i}\n")
    except:
        print("err <-", i)
        f.write(f"err <- {i}\n")
    i += 1
f.close()
f = open("utf8.txt", "w+", encoding="utf8")
for i in range(0, 4294967296):
    try:
        print(chr(i), "<-", i)
        f.write(f"{chr(i)} <- {i}\n")
    except:
        print("err <-", i)
        f.write(f"err <- {i}\n")
    i += 1
f.close()
