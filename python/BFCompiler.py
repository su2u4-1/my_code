import os, Preprocessor, Parser, Compiler


def listAllFiles(path: str):
    result = []
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            result.append(os.path.join(path, f))
        else:
            result += listAllFiles(os.path.join(path, f))
    return result


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
            preprocess(sourceCode)


def preprocess(code):
    pass


if __name__ == "__main__":
    main()