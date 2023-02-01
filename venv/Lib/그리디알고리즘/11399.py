N = int(input())
con = 0

time = list(map(int, input().split()))

time.sort()

for i in range(N):
    for j in range(i+1):

        con += time[j]

print(con)