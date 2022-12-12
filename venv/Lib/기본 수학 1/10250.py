N = int(input())
Y = 0
X = 1
Result = []

for i in range(N):
    a, b, c = map(int, input().split())

    for i in range(c):
        Y += 1

        if(Y>a):

            X += 1
            Y = 1

    if (X>=10):
        Result.append(str(Y)+str(X))

    else:
        Result.append(str(Y) + '0' + str(X))

    Y = 0
    X = 1
for i in range(len(Result)):
    print(Result[i])