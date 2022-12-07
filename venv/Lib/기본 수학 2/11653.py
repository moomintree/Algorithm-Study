N = int(input())
A = 2

for i in range(2, N+1):

    if(N%A==0):
        N = N/A
        print(A)
        if(N==1):
            break
    else:
        A+=1