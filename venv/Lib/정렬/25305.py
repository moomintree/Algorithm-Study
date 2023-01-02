x, y = map(int, input().split())
List = list(map(int, input().split()))
con = 0

for i in range(x):

    for a in range(x-1):

       if int(List[a])>int(List[a+1]):

           con = List[a]
           List[a] = List[a+1]
           List[a+1] = con

print(List[-y])