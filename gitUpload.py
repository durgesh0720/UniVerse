import sys
import os
import datetime
try:
    dt = datetime.datetime.now()
    n = len(sys.argv)
    n=f'{n} {dt}'
    if not n:
        n=f"Push code: {dt}"

    def pushCode(n):
        os.system("git add .")
        os.system(f""" git commit -m '{n}' """)
        os.system("git push")

        print(f"Code is pushed on github at: {dt}, N: {n}")

    pushCode(n)
except Exception as e:
    print(f"Exception Occured by: {e}")


