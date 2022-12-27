Con = 0
List = []

for i in range(5):

    a = int(input())
    List.append(a)


for a in range(5):
    for b in range(4):

        if (int(List[b]) > int(List[b+1])):

            Con = List[b]
            List[b] = List[b+1]
            List[b+1] = Con


print(int(sum(List)/len(List)))
print(List[2])