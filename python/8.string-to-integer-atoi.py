#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
from itertools import count


class Solution:
    def myAtoi(self, s: str) -> int:
        res = ""
        for c in s:
            if res == "" and c == ' ':
                continue
            elif c == '-' or c == '+':
                if res == "":
                    res = c
                else:
                    break
            elif '0' <= c <= '9':
                res += c
            else:
                break

        if res == '-' or res == '+' or res == "":
            res = 0
        else:
            res = int(''.join(res))

        if res > 2**31 - 1:
            res = 2**31 - 1
        if res < -2**31:
            res = -2**31

        return res

        
# @lc code=end

