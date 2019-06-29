'''
162. Find Peak Element

https://leetcode.com/problems/find-peak-element/
similar problem:"852. Peak Index in a Mountain Array"
https://leetcode.com/problems/peak-index-in-a-mountain-array/


A peak element is an element that is greater than its neighbors.
Given an input array nums, where nums[i] ≠ nums[i+1],
find a peak element and return its index.
The array may contain multiple peaks,
in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5

Explanation: Your function can return either index number 1 where the peak element is 2,
             or index number 5 where the peak element is 6.

Note:
Your solution should be in logarithmic complexity.

'''

# Conditions:
#      1. array length is 1  -> return the only index
#      2. array length is 2  -> return the bigger number's index
#      3. array length is bigger than 2 ->
#            (1) find mid, compare it with its left and right neighbors
#            (2) return mid if nums[mid] greater than both neighbors
#            (3) take the right half array if nums[mid] smaller than right neighbor
#            (4) otherwise, take the left half

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1

        # handle condition 3
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid

            if nums[mid] < nums[mid + 1]:
                lo = mid +1

            else:

                hi = mid - 1
        # handle condition 1 and 2
        return hi if nums[lo] >= nums[hi] else lo