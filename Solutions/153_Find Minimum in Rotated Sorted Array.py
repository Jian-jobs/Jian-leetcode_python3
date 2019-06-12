'''
153. Find Minimum in Rotated Sorted Array

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
similar problem: "154. Find Minimum in Rotated Sorted Array II"
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
You may assume no duplicate exists in the array.

Example 1:
Input: [3,4,5,1,2]
Output: 1

Example 2:
Input: [4,5,6,7,0,1,2]
Output: 0
'''


class Solution:
    def findMin(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:

            if nums[lo]<nums[hi]:
                return nums[lo]
            else:
                mid = lo + (hi - lo) // 2
                if nums[mid]<nums[hi]:
                    hi = mid
                else:
                    lo = mid+1
        return nums[lo]


