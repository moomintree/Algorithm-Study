arr = list(map(int, input()))
con = 0
for i in range(len(arr)):

    for a in range((len(arr))-1):

        if (int(arr[a]) < int(arr[a+1])):

            con = arr[a]
            arr[a] = arr[a+1]
            arr[a+1] = con


for i in arr:
    print(i, end="")