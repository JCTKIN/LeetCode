#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        xlist = [n for n in str(x)]
        n = len(xlist) // 2
        for i in range(n):
            if xlist[i] != xlist[-i-1]:
                return False
        return True
        
# @lc code=end

