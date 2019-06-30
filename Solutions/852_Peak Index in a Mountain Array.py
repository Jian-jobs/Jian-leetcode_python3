'''
852. Peak Index in a Mountain Array

https://leetcode.com/problems/peak-index-in-a-mountain-array/
similar problem:"162. Find Peak Element"
https://leetcode.com/problems/find-peak-element/

Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1]
< A[i] > A[i+1] > ... > A[A.length - 1]

Given an array that is definitely a mountain, return any i such that A[0]
< A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:
Input: [0,1,0]
Output: 1

Example 2:
Input: [0,2,1,0]
Output: 1

Note:

1. 3 <= A.length <= 10000
2. 0 <= A[i] <= 10^6
3. A is a mountain, as defined above.

'''
# 和162一样可以照搬

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        lo, hi = 0, len(A) - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if A[mid] > A[mid + 1] and A[mid] > A[mid - 1]:
                return mid
            if A[mid] < A[mid + 1]:
                lo = mid + 1
            else:
                hi = mid - 1

        return hi if A[lo] <= A[hi] else lo
# reference:
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return A.index(max(A))





