from os import listdir, system, chdir, getcwd
from os.path import isdir, join
from subprocess import getoutput
from sys import argv


def check(dir: str) -> bool:
    print(f"\nChecking folder: {dir}")
    state = True
    try:
        if ".git" in listdir(dir):
            chdir(dir)
            status = getoutput("git status --porcelain")
            if len(status) == 0:
                status = getoutput("git show-branch --remote")
                if status == "No revs to be shown.":
                    print("    No remote repository, skipping")
                else:
                    print("    No uncommitted changes, running git pull...")
                    system("git pull --all")
                    state = False
            else:
                print("    Uncommitted changes:")
                for f in status.split("\n"):
                    print("       ", f)
                state = False
        else:
            print("    Not a Git repository, skipping")
    except PermissionError:
        print("    Access denied, skipping")
        state = False
    except Exception as e:
        print(f"    Error: {e}, skipping")
        state = False
    return state


def recursion(dir: str) -> None:
    state = check(dir)
    if state:
        for i in listdir(dir):
            if isdir(join(dir, i)):
                recursion(join(dir, i))


def norecursion(dir: str) -> None:
    for i in listdir(dir):
        if i != ".git" and isdir(join(dir, i)):
            check(join(dir, i))


rootdir = getcwd()
if len(argv) >= 2 and isdir(argv[1]) and "def" not in argv[1]:
    rootdir = argv[1]

if len(argv) >= 3 and "-r" in argv[2]:
    recursion(rootdir)
else:
    norecursion(rootdir)
