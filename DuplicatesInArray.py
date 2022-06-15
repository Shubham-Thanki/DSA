class Solution:
    def duplicates(self, arr, n):
        # code here
        temp = []
        final = []
        temp.append(arr[0])
        for i in range(1, n):
            if arr[i] not in temp:
                temp.append(arr[i])
            else:
                final.append(arr[i])

        if len(final) == 0:
            final.append(-1)
            return final
        else:
            return final.sort()


# {
#  Driver Code Starts
if(__name__ == '__main__'):
    t = 1
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        # print(res)
        for i in res:
            print(i, end=" ")
        print()


# } Driver Code Ends

# https://practice.geeksforgeeks.org/problems/find-duplicates-in-an-array/1/?page=1&category[]=Arrays&sortBy=submissions#
