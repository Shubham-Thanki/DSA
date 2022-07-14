from re import I


arr = [12, 45, 23, 51, 8]
n = 5
for i in range(1, n):
    k = i
    # j=i-1
    for j in range(i-1, -1, -1):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            i -= 1
    i = k

print(arr)
