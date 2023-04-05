N = int(input())
arr = []

for i in range(N):

    x, y = list(input().split())
    x = int(x)
    arr.append([i,x,y])

arr.sort(key=lambda x:(x[1],x[0]))

for i in arr:

    print(i[1], i[2])

# 출력을 정수로 해야 되는데 문자로 통째로 받아서 출력까지 하다보니까 계속 틀렸다
# 문제조건과 답을 내야하는 부분을 꼼꼼하게 확인할 것