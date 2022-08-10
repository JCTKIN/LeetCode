#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        plist = []
        for c in p:
            if c != '*':
                plist.append(c)
            else:
                plist[-1] += '*'

        slen = len(s)
        plen = len(plist)

        dt = [[0] * (plen+1) for n in range(slen+1)]
        dt[0][0] = 1
        rsum = [0] * slen
        csum = [0] * plen
        for i, sc in enumerate(s):
            for j, pc in enumerate(plist):
                if dt[i][j] in [1, 3] or dt[i+1][j] in [2, 3] or dt[i][j+1] == 3:
                    if sc == pc or pc == '.':
                        dt[i+1][j+1] = 1
                    elif sc == pc[0] or pc[0] == '.':
                        dt[i+1][j+1] = 3
                    elif len(pc) == 2:
                        if not (i == slen-1 and j == plen-1 and dt[i+1][j] not in [1, 2, 3]):
                            dt[i+1][j+1] = 2
                elif i == slen-1 and dt[i+1][j] in [1, 4]:
                    if len(pc) == 2:
                        dt[i+1][j+1] = 4

                rsum[i] += dt[i+1][j+1]
                csum[j] += dt[i+1][j+1]

        if dt[slen][plen] != 0:
                return True
        return False

# @lc code=end

