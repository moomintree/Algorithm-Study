N, K = map(int,input().split())
arr = []
Cnt = 0

for i in range(N):

    num = int(input())
    arr.append(num)

arr.sort(reverse=True)

for i in arr:

    Cnt += (K // i)
    K = K%i

print(Cnt)