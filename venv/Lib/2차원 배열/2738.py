a, b = map(int, input().split())

A, B = [], []

for i in range(a):
    row = list(map(int, input().split()))
    A.append(row)

for i in range(a):
    row = list(map(int, input().split()))
    B.append(row)

for row in range(a):
    for col in range(b):
        print(A[row][col] + B[row][col], end=' ')
    print()


