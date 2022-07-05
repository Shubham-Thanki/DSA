class Solution:

    def fib(self, n):
        if n <= 1:
            return n
        return self.fib(n-1)+self.fib(n-2)


# Time Complexity = 2^n


obj = Solution()
for i in range(7):
    k = obj.fib(i)
    # print(k, end=' ')


# To reduce the time complexity on this to O(n), we can use memoization.

memo = [-1]*9


class betterSolution:

    def fib(self, n):
        if n <= 1:
            memo[n] = n
            return n
        else:
            if memo[n-2] == -1:
                memo[n-2] = self.fib(n-2)
            if memo[n-1] == -1:
                memo[n-1] = self.fib(n-1)
            return memo[n-2]+memo[n-1]
            # The values are directly fetched from the memo list and are returned.


f = betterSolution()
for i in range(7):
    f.fib(i)

print(memo)
