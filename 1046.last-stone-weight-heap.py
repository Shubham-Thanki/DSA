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
        heapq.heapify(stones)
        while(len(stones) > 1):
            print(stones)
            st1 = heapq.heappop(stones)
            st2 = heapq.heappop(stones)
            # -st1-(-st2)
            if st1 < st2:
                diff = st1-st2
                heapq.heappush(stones, diff)
        stones.append(0)
        return abs(stones[0])
# @lc code=end

# https://leetcode.com/problems/last-stone-weight/
