#!usr/bin/env python3
# -*- coding:utf-8 -*-
'''
560. Subarray Sum Equals K

https://leetcode.com/problems/subarray-sum-equals-k/
similar problem: "001. Two Sum"
https://leetcode.com/problems/two-sum/

Given an array of integers and an integer k, you need to find the total number
of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2

Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and
the range of the integer k is [-1e7, 1e7].

'''


class Solution:
    def subarraySum(self, nums, k):
        '''

        :param nums: List[int]
        :param k: int
        :return: int
        '''
        from collections import defaultdict
        prefix = defaultdict(int)
        prefix[0] = 1
        count = 0
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            prefix[cur_sum] += 1 #hashmap<cur_sum, occur times>
            if cur_sum - k in prefix:
                count += prefix[cur_sum - k]

        return count

print(Solution().subarraySum([1,1,1], 2))

'''
思路：
Example 1:
Input:nums = [1,1,1], k = 2
Output: 2

count of prefix sum 减少重复计算

prefixSum[x] = nums[0]+ .. + nums[x]
prefixSum[x] = prefixSum[x-1] + nums[x]

sum of subarray (i, j) = prefixSum[j] - prefixSum[i-1]

as: prefixSum[j] = nums[0] + ... + nums[i-1] + nums[i]+ ... + nums[j]
  prefixSum[i-1] = nums[0] + ... + nums[i-1] 

为了避免sum of subarray (i, j) = prefixSum[j] - prefixSum[i-1] 中 i= 0时， i-1=-1
prefixSum最前面加一个0： 
Input:
nums    =    [1, 1, 1]
index    =   [0, 1, 2]
prefixSum=[0, 1, 2, 3]
hashmap = [<0,1><1,1><2,1><3,1>]
Using a HashMap<key, value> to record:
key = prefixSum value
value = numbers of occurrence of the prefixSum value 
count   =  0 + 0 + 1 + 1               (prefixSum[j] - K == prefixSum=[0, 1, 2, 3])
          -2， -1， 0， 1
问题转化成： find how many pairs <i, j>
where i < j, prefixSum[j] - prefixSum[i] == K
'''

'''
defaultdict(function_factory): 构建一个是类似factory的对象，其中key的值，自行赋值，
但value的类型，是function——factory的类实例，且有默认值
defaultdict(int)：创建类似dictionary的对象，之中value都是int实例，
对不存在的的key，默认value 是 int()的默认值0

s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1
print(list(d.items())) 
>>[('m', 1), ('i', 4), ('s', 4), ('p', 2)]
'''