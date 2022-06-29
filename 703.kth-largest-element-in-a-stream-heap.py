#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start
import heapq
# We create a minheap of size k, so that the 3rd largest element is always the minimum in
# a minheap of size 3.


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = nums
        heapq.heapify(self.minheap)
        while(len(self.minheap) > self.k):
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
        # Your KthLargest object will be instantiated and called as such:
        # obj = KthLargest(k, nums)
        # param_1 = obj.add(val)
        # @lc code=end

        # https://leetcode.com/problems/kth-largest-element-in-a-stream/
