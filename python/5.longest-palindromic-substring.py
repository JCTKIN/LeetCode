#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 0
        res = ""

        return res
    
    def checkPalindrome(self, subs: str) -> bool:
        for i in range(len(subs//2)):
            if subs[i] != subs[-i-1]:
                return False
        return True
        
# @lc code=end

