#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
from re import I


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxVol = 0
        i, j = 0, len(height)-1
        while i != j:
            w = j - i
            if height[i] > height[j]:
                h = height[j]
                j -= 1
            else:
                h = height[i]
                i += 1
            vol = w * h
            maxVol = maxVol if maxVol > vol else vol
        return maxVol

        
# @lc code=end

