#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        xlist = [n for n in str(x)]
        if x >= 0:
            revxlist = xlist[::-1]
        else:
            revxlist = [xlist[0]] + xlist[:0:-1]
        revx = int(''.join(revxlist))
        res = revx if -2**31 <= revx <= 2**31 -1 else 0
        return res

# @lc code=end

