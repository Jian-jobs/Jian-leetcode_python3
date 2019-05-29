'''
35. Search Insert Position

https://leetcode.com/problems/search-insert-position/
similar problem: "34. Find First and Last Position of Element in Sorted Array"
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Example 3:
Input: [1,3,5,6], 7
Output: 4

Example 4:
Input: [1,3,5,6], 0
Output: 0

'''



class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            else:
                if nums[0] > target:
                    return 0
                if nums[len(nums) - 1] < target:
                    return len(nums)
                if nums[i] < target and nums[i + 1] > target: #放在最后哦～
                    return i + 1
# 第一次全自己写的！！

# reference：
class Solution:
 def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in nums:
            if i >= target:
                return nums.index(i)
        return len(nums)