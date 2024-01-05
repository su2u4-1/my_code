f = open("data/name.txt", "a+", encoding="utf-8")
while True:
    a = input(":")
    if a == "exit":
        break
    f.write(", " + a)
f.close()
