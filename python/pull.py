from os import listdir, system, chdir, getcwd
from os.path import isdir, join, abspath
from subprocess import getoutput
from sys import argv


def main(dir: str) -> None:
    print(f"\nChecking folder: {dir}")
    if not isdir(dir):
        print(f"    {dir} is not a directory, skipping")
        return
    try:
        if ".git" in listdir(dir):
            chdir(dir)
            result = getoutput("git status --porcelain")
            if len(result) == 0:
                result = getoutput("git show-branch --remote")
                if result == "No revs to be shown.":
                    print("    No remote repository, skipping")
                else:
                    print("    No uncommitted changes, running git pull...")
                    system("git pull --all")
            else:
                print("    Uncommitted changes:")
                for f in result.split("\n"):
                    print("       ", f)
                system("git fetch --all")
        else:
            print("    Not a Git repository, skipping")
    except PermissionError:
        print("    Access denied, skipping")
    except Exception as e:
        print(f"    Error: {e}, skipping")


now_dir = getcwd()
flag = False
github_user_name = "su2u4-1"
for i in argv[1:]:
    if isdir(i):
        flag = True
        i = abspath(i)
        main(i)
        for j in listdir(i):
            if j != ".git" and isdir(join(i, j)):
                main(join(i, j))
    else:
        print("Checking name:", i)
        result = getoutput("git clone https://github.com/" + github_user_name + "/" + i + ".git")
        if result == f"Cloning into '{i}'...\nremote: Repository not found.\nfatal: repository 'https://github.com/{github_user_name}/{i}.git/' not found":
            print(f"    Repository {i} not found, skipping")
        else:
            print(f"    Cloned {i} repository")
            flag = True

if not flag:
    main(now_dir)
