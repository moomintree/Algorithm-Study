N = int(input())

arr = []
level = []

for i in range(N):

    a, b = map(int, input().split())
    arr.append((a,b))

for i in range(N):
    count = 0
    for j in range(N):

        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:

            count +=1
    level.append(count+1)

for i in level:

    print(i, end=" ")
