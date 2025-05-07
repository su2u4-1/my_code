def decode_to_utf8(original_str: str) -> str:
    t = -1
    c = ""
    oi: list[str] = []
    result: list[str] = []
    for i in original_str:
        if i == "\\":
            t = 0
        elif 0 <= t < 3 and i in "01234567":
            t += 1
            c += i
            if t == 3:
                t = -1
                oi.append(c)
                c = ""
        elif t == -1:
            result.append(bytes(int(j, 8) for j in oi).decode("utf-8"))
            result.append(i)
            oi = []
        else:
            result.append(bytes(int(j, 8) for j in oi).decode("utf-8"))
            result.append(c)
            t = -1
            c = ""
            oi = []
    if oi:
        result.append(bytes(int(j, 8) for j in oi).decode("utf-8"))
        oi = []

    return "".join(result)


print(decode_to_utf8(input(":")))
