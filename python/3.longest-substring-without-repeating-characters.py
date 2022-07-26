#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, i = 0, 0
        prevChar = {}
        for j, c in enumerate(s):
            if c in prevChar:
                i = max(i, prevChar[c] + 1)
            res = max(res, j - i + 1)
            prevChar[c] = j
        return res

        
# @lc code=end

