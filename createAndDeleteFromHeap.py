#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        minheap = []
        self.nums.append(val)
        minheap.append(self.nums[0])
        a = 1
        while (a < len(self.nums)):
            minheap.append(self.nums[a])
            i = a
            j = (a-1)//2
            while (minheap[i] < minheap[j]):
                minheap[i], minheap[j] = minheap[j], minheap[i]
                j = (j-1)//2
                i = (i-1)//2
                if j <= 0 and i <= 0:
                    break
            a += 1
        i = 0
        j = 0
        while(len(minheap) > self.k):
            minheap.pop(0)
            minheap.insert(0, minheap[-1])
            j = 2*i+1
            while(j < len(minheap)):
                # If the right child is lesser than the left child.
                if minheap[j+1] < minheap[j]:
                    j = j+1
                # If the parent element is greater than the child.
                if minheap[i] > minheap[j]:
                    minheap[i], minheap[j] = minheap[j], minheap[i]
                    i = j
                    j = 2*j+1
                else:
                    break

        print(minheap)
    # return minheap[0]

    # Your KthLargest object will be instantiated and called as such:
    # obj = KthLargest(k, nums)
    # param_1 = obj.add(val)
    # @lc code=end
