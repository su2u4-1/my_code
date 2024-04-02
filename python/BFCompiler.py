import os, re


class register:
    def __init__(self):
        self.r = [0, 0, 0]
        self.sp = 0
    def d(self):
        if self.sp > len(self.r):
            self.r.append(0)
        for i in range(len(self.r)):
            if self.r[i] < 0:
                self.r[i] = 255
            elif self.r[i] > 255:
                self.r[i] = 0


def listAllFiles(path: str):
    result = []
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            result.append(os.path.join(path, f))
        else:
            result += listAllFiles(os.path.join(path, f))
    return result


def preprocess(code):
    def _flatten(nested, result):
        for item in nested:
            if isinstance(item, list):
                _flatten(item, result)
            else:
                result.append(item)
        return result

    for i in range(len(code)):
        code[i] = re.sub(r"\s+", " ", code[i].split())

    return "".join(_flatten(code, []))


def run(code):
    reg = register()
    for i in code:
        if i == ">":
            reg.sp += 1
        elif i == "<":
            reg.sp -= 1
        elif i == "+":
            reg.r[reg.sp] += 1
        elif i == "-":
            reg.r[reg.sp] -= 1


def main():
    path = input("file or path:")
    if path.endswith(".jack"):
        result = [path]
    else:
        if "C:\\Users\\joey2\\桌面\\nand2tetris\\" in path:
            result = listAllFiles(path)
        else:
            result = listAllFiles("C:\\Users\\joey2\\桌面\\nand2tetris\\" + path)
    for i in result:
        if i.endswith(".bf"):
            f = open(i, "r")
            sourceCode = f.readlines()
            f.close()
            print("file:",i)
            code = preprocess(sourceCode)
            run(code)


if __name__ == "__main__":
    main()