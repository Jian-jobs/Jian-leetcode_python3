'''
34. Find First and Last Position of Element in Sorted Array

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
similar problem: "704. Binary Search"
https://leetcode.com/problems/binary-search/

Given an array of integers nums sorted in ascending order,
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.lowwer(nums, target)
        right = self.higher(nums, target)
        if left == right:
            return [-1, -1]
        return [left, right -1]

    def lowwer(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right-left) // 2
            if nums[mid] < target: # <注意！！
                left = mid + 1
            else:
                right = mid
        return left

    def higher(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right-left) // 2
            if nums[mid] <= target: # <=注意！！
                left = mid + 1
            else:
                right = mid
        return left

# reference: bisect模块 时间复杂度是O(logn)，空间复杂度是O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        if left == right:
            return [-1, -1]
        return [left, right -1]
