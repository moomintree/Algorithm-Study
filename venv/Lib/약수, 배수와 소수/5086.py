while True:

    x, y = map(int, input().split())

    if (x==0 and y==0):
        break

    if (x%y==0 and x>y):
        print('multiple')

    elif (y%x==0 and x<y):
        print('factor')

    else:
        print('neither')

# 조건에 주의, 0,0을 입력받는 이유는 무한반복에서 break시키기 위함.
# 다중 if와 if,elif의 차이점을 정확히 알고 있어야 한다.


