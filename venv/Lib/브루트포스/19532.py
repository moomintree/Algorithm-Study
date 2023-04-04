a, b, c, d, e, f = map(int, input().split())

for A in range(-999, 1000):

    for B in range(-999, 1000):

        if a*A+b*B==c and d*A+e*B==f:

            print(A, B)


# x항과 y항을 더해서 처리하려고 했으나 그러면 안됨.
# => 연립방정식이란 하나의 식이 아닌 두 개의 식 조건을 동시에 만족해야 하기 때문에
# 브루트포스 사용