hour, minute = map(int,input().split())
need = int(input())

hour += need // 60
minute += need % 60

if minute >= 60:
    hour += 1
    minute -= 60
if hour >= 24:
    hour -= 24

print(hour,minute)
