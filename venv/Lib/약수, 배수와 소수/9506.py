while True:
    n = int(input())
    arr = []
    result = 0
    list = ''
    if n==-1:
        break

    for i in range(1, n):

        if (n%i==0):
            arr.append(i)
            result += i

    if sum(arr) == n:

        print(n, "=", end=" ")
        print(*arr,sep=" + ") # *배열의 형태는 배열을 순차적으로 출력하는 효과가 있다.

    else:
        print(n,'is NOT perfect.')

# 아이디어는 구상했으나 출력부문에서 막힘. 브루트포스 참고
# 합계가 n과 같을 때 출력부분에 유의하고 익힐 것
# print end=" " => 말그대로 프린트문 끝단에 넣을 것. for문 사용 시 응용될 수 있을 것 같다.
# print sep=" " => 출력되는 프린트 구문별로 사이에 들어가는 부분