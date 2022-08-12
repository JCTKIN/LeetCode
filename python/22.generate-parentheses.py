#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        o = c = n
        res = []
        def genPar(s: str, o: int, c: int) -> None:
            if o > c or o < 0 or c < 0:
                return
            if o == 0 and c == 0:
                res.append(s)
                return
            genPar(s+'(', o-1, c)
            genPar(s+')', o, c-1)
            return
        genPar("", o, c)
        return res
        
# @lc code=end

