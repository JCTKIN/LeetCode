#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, qaud = [], []

        def kSum(k: int, start: int, target: int) -> None:
            if k == 2:
                twoSum(start, target)
                return
            
            for i in range(start, len(nums)-k+1):
                if i > start and nums[i] == nums[i-1]:
                    continue
                qaud.append(nums[i])
                kSum(k-1, i+1, target-nums[i])
                qaud.pop()

        def twoSum(start: int, target: int) -> None:
            l, r = start, len(nums) - 1
            while l < r:
                tSum = nums[l] + nums[r]
                if tSum > target:
                    r -= 1
                elif tSum < target:
                    l += 1
                else:
                    res.append(qaud + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        kSum(4, 0, target)
        return res
        
# @lc code=end

