# Insert an element from unsorted array to its correct position in sorted array.
arr = [12, 45, 23, 51, 8]
n = 5
for i in range(1, n):
    current = arr[i]  # Preserving the element which is to be compared.
    prev = i-1
    while(arr[prev] > current and prev >= 0):
        # The previous element is shifted one place ahead.
        arr[prev+1] = arr[prev]
        prev -= 1
    # The loop stops when the current element is no longer smaller than the preceeding element. It is where it is then inserted.
    arr[prev+1] = current

print(arr)
