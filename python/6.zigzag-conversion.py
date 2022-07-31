#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ""
        interval = (numRows - 1) * 2 if numRows > 1 else 1
        for i in range(numRows):
            for j in range(i, len(s), interval):
                res += s[j]
                if i != 0 and i != numRows-1:
                    if j+interval-i*2 < len(s):
                        res += s[j+interval-i*2]
        return res
            
        
# @lc code=end

