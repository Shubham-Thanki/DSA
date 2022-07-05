class Solution:
    r = 1

    def horner(self, x, n):
        # if n > 0:
        #     Solution.r = 1+(x/n)*Solution.r
        #     self.horner(x, n-1)
        # else:
        #     return 1
        # return Solution.r
        if n == 0:
            return Solution.r
        Solution.r = 1+(x/n)*Solution.r
        return self.horner(x, n-1)


obj = Solution()
k = obj.horner(1, 4)
print(k)
