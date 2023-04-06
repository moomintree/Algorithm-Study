import sys

num = int(input())

for i in range(0, num):
    a, b = map(int, sys.stdin.readline().split())
    c, d = a, b

    q, r = 0, 0
    while True:
        if a < b:
            a, b = b, a
        q = a // b
        r = a - (q * b)
        if r == 0:
            gcd = b
            break
        a = b
        b = r
    print((c * d) // gcd)


# 최소 공배수(lcm)와 최대 공약수(gcd) 개념으로 이 문제를 보면,
# lcm 은 두 수의 곱에서 최대 공약수를 나누어 준 수인걸 알 수 있습니다. ex) lcm = (36 * 60) / 12