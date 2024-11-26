from os import listdir, system, chdir
from os.path import isdir, join
from subprocess import getoutput
from sys import argv


def check(dir: str):
    print(f"\nChecking folder: {dir}")
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
            else:
                print("    Uncommitted changes:")
                for f in status.split("\n"):
                    print("       ", f)
        else:
            print("    Not a Git repository, skipping")
    except PermissionError:
        print("    Access denied, skipping")
    except Exception as e:
        print(f"    Error: {e}, skipping")


def main(dir: str):
    check(dir)
    for i in listdir(dir):
        if isdir(join(dir, i)):
            main(join(dir, i))


rootdir = ".\\"
if len(argv) >= 2:
    if isdir(argv[1]):
        rootdir = argv[1]

main(rootdir)
