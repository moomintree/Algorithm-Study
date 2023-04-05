import sys
N = int(sys.stdin.readline())
arr = []


for i in range(N):

    x = input()

    if x not in arr:
        arr.append(x)

arr.sort()
arr.sort(key=lambda x:len(x))

for i in range(len(arr)):

    print(arr[i])

# if x not in arr: arr.append(x) 는 중복제거
# sort에 대한 람다함수 key=lambda x:len 길이로 정렬하겠다는 의미다. x는 리스트 내 요소 뜻, 함수의 f(x) 와 비슷하다. y여도 큰상관없음
# key=lambda x:x[0] => 0번째 요소에 대한 정렬=>내림차순
# strip은 공백 제거 (sql의 trim)