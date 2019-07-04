'''
668. Kth Smallest Number in Multiplication Table

https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/
similar problem: "378. Kth Smallest Element in a Sorted Matrix" "hard"
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

Nearly every one have used the Multiplication Table.
But could you find out the k-th smallest number quickly from the multiplication table?

Given the height m and the length n of a m * n Multiplication Table,
and a positive integer k, you need to return the k-th smallest number in this table.

Example 1:
Input: m = 3, n = 3, k = 5
Output:

Explanation:
The Multiplication Table:
1	2	3
2	4	6
3	6	9

The 5-th smallest number is 3 (1, 2, 2, 3, 3).
---------------------------------
Example 2:
Input: m = 2, n = 3, k = 6
Output:

Explanation:
The Multiplication Table:
1	2	3
2	4	6

The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).
---------------------------------

Note:
1. The m and n will be in the range [1, 30000].
2. The k will be in the range [1, m * n]

'''

class Solution:
    def findKthNumber(self, m, n, k):
        l, r = 1, m * n
        while l < r:
            mid = (l + r) // 2
            if sum(min(mid // i, n) for i in range(1, m + 1)) < k:
                l = mid + 1
            else:
                r = mid
        return l

# reference:
# https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/discuss/106984/Python-Straightforward-with-Explanation

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        low, high = 1, m * n
        while low < high:
            mid = (low + high) // 2
            # find n - smaller
            curr = 0
            j = 1
            for r in range(m, 0, -1):
                while j <= n and r * j <= mid:
                    j += 1
                curr += j - 1
            if curr < k:
                low = mid + 1
            else:
                high = mid
        return low