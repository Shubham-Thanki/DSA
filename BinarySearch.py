class Solution:
    def search(self, nums, target: int) -> int:
        l, r = 0, len(nums)-1
        while(l <= r):
            pivot = l+(r-l)//2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                r = pivot-1
            else:
                l = pivot+1
        return -1

# https://leetcode.com/problems/binary-search/
