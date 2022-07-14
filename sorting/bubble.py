arr = [7, 3, 1, 4, 2]
n = 5
for i in range(n-1, -1, -1):
    for j in range(0, i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)
# Here the idea to start the loop of i in reverse comes from the fact that the upper limit loop
# of j needs to be reduced by 1 after every successful pass. So, on takinf the loop in reverse we can set
# its upper limit equal to i.
