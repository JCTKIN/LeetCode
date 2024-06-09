#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        q = 0
        d, dv = abs(dividend), abs(divisor)

        while d >= dv:
            temp = dv
            mul = 1
            while d >= temp:
                d -= temp
                q += mul
                mul += mul
                temp += temp

        if (dividend < 0 < divisor) or (divisor < 0 < dividend):
            q = -q

        return min(2147483647, max(-2147483648, q))

# @lc code=end
