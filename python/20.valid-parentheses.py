#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')', '{':'}', '[':']'}
        stack = []
        for b in s:
            if b in brackets:
                stack.append(b)
            elif not stack or brackets[stack.pop()] != b:
                return False
        return not stack
        
# @lc code=end

