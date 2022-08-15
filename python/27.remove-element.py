#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = k = 0
        j = len(nums)
        while i < j:
            if nums[i] != val:
                k += 1
            else:
                nums[i] = nums[j-1]
                j -= 1
                i -= 1
            i += 1
        return k
        
# @lc code=end

