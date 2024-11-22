from os import listdir, system, chdir
from os.path import isdir, join
from subprocess import getoutput

rootdir = "D:\\"

for i in listdir(rootdir):
    i = join(rootdir, i)
    if isdir(i):
        print(f"\n檢查資料夾：{i}")
        try:
            if ".git" in listdir(i):
                chdir(i)
                status = getoutput("git status --porcelain")
                if len(status) == 0:
                    status = getoutput("git show-branch --remote")
                    if status == "No revs to be shown.":
                        print("    無遠端儲存庫，略過")
                    else:
                        print("    無未提交的更改，執行 git pull...")
                        system("git pull --all")
                else:
                    print("    未提交的變更:")
                    for f in status.split("\n"):
                        print("       ", f)
            else:
                print("    這不是一個 Git 資料夾，略過")
        except PermissionError:
            print("    存取被拒，略過")
