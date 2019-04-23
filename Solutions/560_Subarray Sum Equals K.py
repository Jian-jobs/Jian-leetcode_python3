'''
560. Subarray Sum Equals K

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


'''
- solution（1）： count of prefix sum 减少重复计算

Using a hashtable to store # of a prefix sum occurs so far
Total sum: sum = nums[0]+...+nums[i]
if:
nums[0]+ ... + nums[j] = sum - K
there exits:
K = nums[j+1] + ... + nums[n]

- solution(2): utilizing the prefixsum array of original input:

prefixSum[x] = sum of subarray (0, x): nums[0]+ .. + nums[x]

prefixSum[x] = prefixSum[x-1] + nums[x]

sum of subarray (i, j) = prefixSum[j] - prefixSum[i-1]

as: prefixSum[j] = nums[0] + ... + nums[i-1] + nums[i]+ ... + nums[j]
  prefixSum[n-1] = nums[0] + ... + nums[i-1] 

为了避免sum of subarray (i, j) = prefixSum[j] - prefixSum[i-1] 中 i= 0时， i-1=-1
prefixSum最前面加一个0： 
Input:
nums    =    [1, 1, 1]
index    =   [0, 1, 2]
prefixSum=[0, 1, 2, 3]
hashmap = [<0,1><1,1><2,1><3,1>]
count   =  0 + 0 + 1 + 1               (prefixSum[j] - prefixSum[i] == K)
问题转化成： find how many pairs <i, j>
where i < j, prefixSum[j] - prefixSum[i] == K
Using a HashMap<integer, Integer> to record:
key = prefixSum value
value = numbers of occurrence of the prefixSum value 
  
'''
from collections import defaultdict
class Solution:
    def subarraySum(self, nums, k):
        '''

        :param nums: List[int]
        :param k: int
        :return: int
        '''

        prefix = defaultdict(int)
        prefix[0] = 1
        count = 0
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]  # increment current sum
            if cur_sum - k in prefix:
                count += prefix[cur_sum - k]
            prefix[cur_sum] += 1
        return count

print(Solution().subarraySum([1,1,1], 2))