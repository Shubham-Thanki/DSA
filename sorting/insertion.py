from re import I


arr = [12, 45, 23, 51, 8]
n = 5
for i in range(1, n):
    current = arr[i]
    prev = i-1
    while(arr[prev] > current and prev >= 0):
        arr[prev+1] = arr[prev]
        prev -= 1
    arr[prev+1] = current

print(arr)
