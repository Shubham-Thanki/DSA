class Solution:
    p = 1
    f = 1
    r = 0

    def taylor(self, x, n):
        if n > 0:
            Solution.r = self.taylor(x, n-1)
            Solution.p *= x
            Solution.f *= n
            return Solution.r+Solution.p/Solution.f
        else:
            return 1


obj = Solution()
k = obj.taylor(1, 10)
print(k)
