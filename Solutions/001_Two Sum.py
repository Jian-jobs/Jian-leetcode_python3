
#!usr/bin/env python3
# -*- coding:utf-8 -*-
'''
1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for index in range(len(nums)):
            if target - nums[index] not in dict:
                dict[nums[index]] = index
            else:
                return [dict[target - nums[index]], index]


print(Solution().twoSum([2, 7, 11, 15], 9))

'''
enumerate() method: faster and less memory usage

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for index, value in enumerate(nums):
            if target - value not in dict:
                dict[value] = index
            else:
                return [dict[target - value], index]


print(Solution().twoSum([2, 7, 11, 15], 9))

'''

