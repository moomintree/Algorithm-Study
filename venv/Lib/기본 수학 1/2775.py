N = int(input())
Result=[]

for i in range(N):
    k = int(input())
    n = int(input())

    People = [i for i in range(1,n+1)]

    for a in range(k):

        for b in range(1, n):
            People[b] += People[b-1]
    print(People[-1])
