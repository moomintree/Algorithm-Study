N = int(input())
Con = 0
List = []

for i in range(N):

    a = int(input())
    List.append(a)


for a in range(N):
    for b in range(N-1):

        if (int(List[b]) > int(List[b+1])):

            Con = List[b]
            List[b] = List[b+1]
            List[b+1] = Con

for a in range(N):
    print(List[a])

