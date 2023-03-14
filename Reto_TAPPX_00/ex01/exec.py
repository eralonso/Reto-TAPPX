import sys

def rev_alpha(arr):
    arr.pop(0)
    if (len(arr) < 1):
        print("Usage: python3 exec.py \"String\"")
        return
    print(" ".join(arr)[-1::-1].swapcase())

rev_alpha(sys.argv)
exit(0)
