N = int(input()) # 입력받는 수
Cross = 1 # 칸의 갯수
CrossSum = 0 # 직전 칸까지 총합

while True:

    if (N<=Cross + CrossSum):

        if (Cross%2==0):
            print(str((N - CrossSum)) + "/" + str(Cross - (N - CrossSum - 1)))
            break
        else:
            print((str(Cross - (N - CrossSum - 1)) + "/" + str(N - CrossSum)))
            break

    else:
        CrossSum += Cross
        Cross += 1