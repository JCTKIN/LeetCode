#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        for idx, n in enumerate(nums):
            if idx > 0 and n == nums[idx-1]:
                continue
            l, r = idx + 1, len(nums) - 1
            while l < r:
                threeSum = n + nums[l] + nums[r]
                if abs(threeSum - target) < abs(res - target):
                    res = threeSum
                if threeSum > target:
                    r -= 1
                elif threeSum < target:
                    l += 1
                else:
                    return res
        return res
        
# @lc code=end

