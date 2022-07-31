#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = s[0]
        maxlen = 1
        dtable = [[0] * n for i in range(n)]
        for j in range(n):
            dtable[j][j] = 1
            if j-1 >= 0:
                if s[j] == s[j-1]:
                    dtable[j-1][j] = 2
                    if dtable[j-1][j] > maxlen:
                        maxlen = 2
                        res = s[j-1:j+1]
                else:
                    dtable[j-1][j] = 0
            for i in range(j-2, -1, -1):
                if dtable[i+1][j-1] != 0 and s[i] == s[j]:
                    dtable[i][j] = dtable[i+1][j-1] + 2
                    if dtable[i][j] > maxlen:
                        maxlen = dtable[i][j]
                        res = s[i:j+1]
        return res
        
# @lc code=end

