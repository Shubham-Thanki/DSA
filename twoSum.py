class Solution:
    def twoSum(self, nums, target: int):
        prewmap = {}  # val:index
        for i, n in enumerate(nums):
            diff = target-n
            if diff in prewmap:
                return [prewmap[diff], i]
            prewmap[n] = i


# https://leetcode.com/problems/two-sum/
# For enumerate nums, i => index, n=>value at that index
# [2,7,11,15]
# prewmap={2:0,7:1,11:2,15:3}={val:index}
