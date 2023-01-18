N = int(input())
Cnt = 0
Six = 666

while True:
    if '666' in str(Six):
        Cnt += 1

    if Cnt == N:
        print(Six)
        break
    Six += 1
