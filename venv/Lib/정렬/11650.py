N = int(input())
arr = []

for i in range(N):

    x, y = list(map(int, input().split()))
    arr.append([x, y])

arr.sort(key=lambda x:(x[0], x[1]))

for i in arr:

    print(i[0], i[1])


# lambda 함수 숙지 필요
# 리스트의 출력법 => for i in arr 형태의 리스트 직접 for문은 i[0], [1] 로 출력 가능하며 i는 리스트, []에 행번호를 넣어서 출력한다.