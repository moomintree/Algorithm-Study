import sys

N = int(sys.stdin.readline())
arr = []

for i in range(N):

    a = int(sys.stdin.readline())
    arr.append(a)

for i in sorted(arr):

    print(i)
