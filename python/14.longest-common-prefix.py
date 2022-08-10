#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for s in strs[1:]:
            i = 0
            temp = ""
            while i < len(res):
                if i < len(s) and res[i] == s[i]:
                    temp += res[i]
                else:
                    res = temp
                    break
                i += 1
        return res
        
# @lc code=end

