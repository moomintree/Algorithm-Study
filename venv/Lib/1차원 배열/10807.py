tot = int(input())
num_list = list(map(int,input().split()))
fi = int(input())
a = 0

for i in range(len(num_list)):
    if num_list[i]==fi:
        a += 1

print(a)

# 11
# 1 4 1 2 4 2 4 2 3 4 4
# 2