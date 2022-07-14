# It repeatedly finds the minimum element from unsorted part & puts it at the beginning.
arr = [64, 25, 12, 22, 11]
n = 5
for i in range(n-1):
    min = arr[i]
    for j in range(i+1, n):
        if arr[j] < min:
            min = arr[j]
            minindex = j
    arr[i], arr[minindex] = arr[minindex], arr[i]
print(arr)
