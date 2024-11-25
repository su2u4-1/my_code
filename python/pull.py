from os import listdir, system, chdir
from os.path import isdir, join
from subprocess import getoutput
from sys import argv

rootdir = "D:\\"
if len(argv) >= 1:
    if isdir(argv[0]):
        rootdir = argv[0]

for i in listdir(rootdir):
    i = join(rootdir, i)
    if isdir(i):
        print(f"\nChecking folder: {i}")
        try:
            if ".git" in listdir(i):
                chdir(i)
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
