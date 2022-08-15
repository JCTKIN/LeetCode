#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, k = 1, 1
        while i < len(nums):
            if nums[i] > nums[i-1]:
                nums[k] = nums[i]
                k += 1
            i += 1
        return k
        
# @lc code=end

