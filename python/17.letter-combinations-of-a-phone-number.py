#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitsMap = {
            '2':['a', 'b', 'c'],
            '3':['d', 'e', 'f'],
            '4':['g', 'h', 'i'],
            '5':['j', 'k', 'l'],
            '6':['m', 'n', 'o'],
            '7':['p', 'q', 'r', 's'],
            '8':['t', 'u', 'v'],
            '9':['w', 'x', 'y', 'z']
        }
        res = []
        while len(digits) > 0:
            if res == []:
                res = digitsMap[digits[0]]
                digits = digits[1:]
                continue
            temp = []
            for r in res:
                for d in digitsMap[digits[0]]:
                    temp.append(r+d)
            res = temp
            digits = digits[1:]
        return res
        
# @lc code=end

