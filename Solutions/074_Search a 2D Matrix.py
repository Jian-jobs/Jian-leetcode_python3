'''
74. Search a 2D Matrix

https://leetcode.com/problems/search-a-2d-matrix/
treat 2d as 1d "binary search"

Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

Example 2:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false

'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = len(matrix) - 1
        j = 0
        while i > -1 and j < len(matrix[0]):
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                j = j + 1
            else:
                i = i - 1
        return False


# reference:
# https://leetcode.com/problems/search-a-2d-matrix/discuss/289393/Beat-100-python-time-max-o(n)space-o(1)
'''
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
len(matrix) row
3
len(matrix[0]) col
4
'''