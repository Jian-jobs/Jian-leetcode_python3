#!usr/bin/env python3
# -*- coding:utf-8 -*-
'''
1. Two Sum

https://leetcode.com/problems/two-sum/
similar problem: "560. Subarray Sum Equals K"
https://leetcode.com/problems/subarray-sum-equals-k/

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

'''
思路：
[2, 7, 11, 15], target: 17
历遍index：
if target-nums[index] not in dict：
    dict[nums[index]] = index
else：
    return[dict[target - nums[index]], index]
----------
index = 0：
    target-nums[index]=15
    dict[2] = 0
index = 1：
    target-nums[index]=10
    dict[7] = 1
index = 2：
    target-nums[index]=6
    dict[11] = 2
index = 3：
    target-nums[index]=2！！
    return [dict[target - nums[index]，index]
    即[dict[2]的value 0, 3]
    
----------   print dictionary： 
for k, v in dict.items():
    print(k, '=>', v)
'''