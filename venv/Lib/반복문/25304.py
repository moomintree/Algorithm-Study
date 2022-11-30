tot = int(input())
kind = int(input())
c = 0

for i in range(kind):
    a, b = map(int,input().split())
    c += a*b

if tot==c:
    print('Yes')
else:
    print('No')

# 260000
# 4
# 20000 5
# 30000 2
# 10000 6
# 5000 8

# 250000
# 4
# 20000 5
# 30000 2
# 10000 6
# 5000 8

