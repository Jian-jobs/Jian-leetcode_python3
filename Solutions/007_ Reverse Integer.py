'''
7. Reverse Integer

https://leetcode.com/problems/reverse-integer/

Given a 32-bit signed integer, reverse digits of an integer.
slicing list

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
of this problem, assume that your function returns 0 when the reversed integer overflows.

'''


class Solution:
    def reverse(self, x: int) -> int:
        a = str(x)
        res = int("-"+a[1:][::-1]) if x<0 else int(a[::-1])
        # or res = int("-"+a[:0:-1]) if x<0 else int(a[::-1])
        return res if -2**31 < res < 2**31-1 else 0

'''
1. power "^" in python: "**"

2. slicing: 
    list[<start_index>:<stop_index>:<step>]
    start： 包括
    stop：不包括
    例子：
    a = '1234'
    
    a[:1]
    '1'
    
    a[1:]
    '234
    
    a[:0:-1]
    '432'
'''
# reference:
# https://leetcode.com/problems/reverse-integer/discuss/4220/Simple-Python-solution-56ms

# reference:
# "the meaning of int(a[::-1])"
# https://stackoverflow.com/questions/31633635/what-is-the-meaning-of-inta-1-in-python
#
# list[<start_index>:<stop_index>:<step>]
#
# In case the start index or stop index is missing, it takes up the default value as the start index
# and stop index of the given string/list/tuple.
# Example -
#
# a = '1234'
# print(a[::2])
# 13
# a = '1234'
# print(a[::1])
# 1234
# a = '1234'
# print(a[::-1])
# 4321