#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_len, n_len = len(haystack), len(needle)
        if n_len == 0:
            return 0
        for i in range(h_len-n_len+1):
            if haystack[i:i+n_len] == needle:
                return i
        return -1
        
# @lc code=end

