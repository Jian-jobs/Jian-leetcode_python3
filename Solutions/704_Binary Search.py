'''
704. Binary Search

https://leetcode.com/problems/binary-search/
similar problem: "35. Search Insert Position"
https://leetcode.com/problems/search-insert-position/

Given a sorted (in ascending order) integer array nums of n elements and a target value,
write a function to search target in nums. If target exists, then return its index,
otherwise return -1.


Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Note:

You may assume that all elements in nums are unique.
n will be in the range [1, 10000].
The value of each element in nums will be in the range [-9999, 9999].
'''


# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#             for i in range(len(nums)):
#                 if nums[i] == target:
#                     return i
#             else:
#                 return -1

# 自己写的

# reference：二叉树
# class Solution:
def search(nums, target):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left+right) // 2
        # // 取整除 - 返回商的整数部分（向下取整）
        # print(left,right,mid)
        if nums[mid] < target:
            left = mid+1
        elif nums[mid] > target:
            right = mid-1
        else:
            return mid
    return -1


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    print(search(nums, target))
