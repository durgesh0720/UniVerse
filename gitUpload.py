import sys
import os

n = len(sys.argv)

def pushCode(n):
    os.system("git add .")
    os.system(f"git commit -m {n}")
    os.system("git push")

pushCode(n)
