#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        numMap = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        prev = None
        res = 0
        for c in s[::-1]:
            if (c == "I" and prev in ["V", "X"]) \
                or (c == "X" and prev in ["L", "C"]) \
                    or (c == "C" and prev in ["D", "M"]):
                    res -= numMap[c]
            else:
                res += numMap[c]
            prev = c
        return res
        
# @lc code=end

