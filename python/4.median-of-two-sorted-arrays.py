#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1Length, nums2Length = len(nums1), len(nums2)
        totalLength = nums1Length + nums2Length
        i, j = 0, 0
        marray = []
        if nums1Length == 0 or nums2Length == 0:
            marray = nums1 + nums2
        while i < nums1Length and j < nums2Length:
            if nums1[i] >= nums2[j]:
                marray.append(nums2[j])
                j += 1
                if j == nums2Length:
                    marray = marray + nums1[i:]
            else:
                marray.append(nums1[i])
                i += 1
                if i == nums1Length:
                    marray = marray + nums2[j:]
        totalLengthMedian, remainder = divmod(totalLength, 2)
        if remainder == 0:
            overallMedian = (marray[totalLengthMedian-1] + marray[totalLengthMedian]) / 2
        else:
            overallMedian = marray[totalLengthMedian]
        return overallMedian
        
# @lc code=end

