import sys

N = int(sys.stdin.readline())
List = [0]*10001


for i in range(N):

    a = int(sys.stdin.readline())
    List[a] += 1

for i in range(10001):

    if List[i] != 0:

        for a in range(List[i]):
            print(i)