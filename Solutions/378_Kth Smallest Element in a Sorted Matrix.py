'''
378. Kth Smallest Element in a Sorted Matrix

https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
similar problem: "668. Kth Smallest Number in Multiplication Table"
https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/

Given a n x n matrix where each of the rows and columns are sorted in ascending order,
find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.
注意：行列都是有顺序的
Example:
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],

k = 8,

return 13.

Note:
You may assume k is always valid, 1 ≤ k ≤ n2.

'''


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        L, R = matrix[0][0], matrix[n - 1][n - 1]
        while L < R:
            mid = (L + R) // 2
            temp = self.search_lower_than_mid(matrix, n, mid)
            if temp < k:
                L = mid + 1
            else:
                R = mid
        return L

    def search_lower_than_mid(self, matrix, n, x):
        i, j = n - 1, 0
        cnt = 0
        while i >= 0 and j < n:
            if matrix[i][j] <= x:
                j += 1
                cnt += i + 1
            else:
                i -= 1
        return cnt

# reference:
# https://www.youtube.com/watch?v=hc2XsrppYSU
# https://www.hrwhisper.me/leetcode-kth-smallest-element-sorted-matrix/


# practice:
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        n = len(matrix)
        l = matrix[0][0]
        r = matrix[n-1][n-1]

        while l < r:
            mid = (l+r)//2
            cnt = self.search(matrix, n ,mid) #self.function调用, "mid", not "k"
            if cnt < k:
                l = mid+1
            else:
                r = mid
        return l
    def search(self, matrix, n, x):
        i, j = n-1, 0
        cnt = 0
        while i >=0 and j < n: #"while", not "for"
            if matrix[i][j]<x:
                j += 1
                cnt += i+1 #i+1, not j+1
            else:
                i -= 1
        return cnt




