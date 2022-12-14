N = int(input())
List = list(map(int,input().split()))
Count = 0


for i in List:

    a = 2

    if (i==1):
        continue

    while(True):

        if(a<i):

            if((i%a)==0):
                break

            else:
                a += 1

        else:

            Count += 1
            break;


print(Count)