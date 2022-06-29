#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= (-1)
            # Here we multiply the elements with (-1) so that we can use the minheap data structure, since python doesen't
            # support max heap
        heapq.heapify(stones)
        while(len(stones) > 1):
            print(stones)
            # This value will be greater in magnitude and less in value.
            st1 = heapq.heappop(stones)
            # This value will be lower in magnitude and more in value.
            st2 = heapq.heappop(stones)
            # -st1-(-st2)
            if st1 < st2:
                diff = st1-st2
                heapq.heappush(stones, diff)
        # We append 0, in case the heap might be empty
        stones.append(0)
        return abs(stones[0])
# @lc code=end

# https://leetcode.com/problems/last-stone-weight/
