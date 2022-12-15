M = int(input())
N = int(input())
Sum = 0
List = []

for i in range(M,N+1):

    a = 2
    if (i==1):
        continue

    while(True):
        if(a<i):
            if((i%a)==0):

                break

            else:
                a+=1

        else:
            Sum += i
            List.append(i)
            break



if len(List) == 0:
    print(-1)
else:
    print(Sum)
    print(min(List))
# print(min(List))

