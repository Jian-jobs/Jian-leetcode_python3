'''
2. Add Two Numbers

https://leetcode.com/problems/add-two-numbers/
similar problem: "445. Add Two Numbers II"
https://leetcode.com/problems/add-two-numbers-ii/

You are given two non-empty linked lists representing two non-negative integers.

The digits are stored in reverse order and each of their nodes contain a single digit.

Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

分类考虑：
1 没有 l1
2.没有 l2
3. while l1 and l2
4. 位数不同， l1有剩
5. 位数不同， l2有剩
6. carry多出一位

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None




class Solution:
    def addTwoNumbers(self, l1, l2):
        '''

        :param l1:  ListNode
        :param l2:  ListNode
        :return:   ListNode
        '''
        dummy = ListNode(0)
        res = dummy
        carry = 0
        if l1 ==None:
            return l2

        if l2 ==None:
            return l1

        while l1 and l2:
            res.next = ListNode((l1.val +l2.val +carry) %10)
            carry = (l1.val +l2.val +carry) // 10
            l1 = l1.next
            l2 = l2.next
            res = res.next

        if l1:
            while l1:
                res.next = ListNode((l1.val +carry) %10)
                carry = (l1.val +carry) // 10
                l1 = l1.next
                res = res.next

        if l2:
            while l2:
                res.next = ListNode((l2.val + carry) % 10)
                carry = (l2.val + carry) // 10
                l2 = l2.next
                res = res.next

        if carry ==1:
            res.next = ListNode(1)

        return res.val
#       return dummy.next in LeetCode



# l1 = ListNode(2)
# l1.next = ListNode(4)
# # l1.next.next = ListNode(3)
#
# l2 = ListNode(5)
# l2.next = ListNode(6)
# # l2.next.next = ListNode(4)
# print(Solution().addTwoNumbers(l1, l2))




l1 = ListNode(2)
l2 = ListNode(5)
print(Solution().addTwoNumbers(l1, l2))

l1.next = ListNode(4)
l2.next = ListNode(6)
print(Solution().addTwoNumbers(l1, l2))

l1.next.next = ListNode(3)
l2.next.next = ListNode(4)
print(Solution().addTwoNumbers(l1, l2))










'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):

        dummy = ListNode(0)
        res = dummy
        carry = 0
        while l1 or l2 or carry > 0:
            carry += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            print('carry:', carry)
            l1 = l1.next if l1 else None
            # print('new l1', l1.val if l1 else None)
            l2 = l2. next if l2 else None
            # print('new l2', l2.val if l2 else None)
            res.next = ListNode(carry % 10)
            print('res:', res.val)
            print('res.next', res.next.val)
            # print('res.next.next:', res.next.next.val if res.next.val else None)
            # print('res.next.next.next:', res.next.next.next.val if res.next.next.val else None)
            carry //= 10
            print('"carry":',carry)
            print('dummy:', dummy.val)
            print('dummy.next:', dummy.next.val)
            # print('dummy.next.next:', dummy.next.next.val if dummy.next.val else None)
            # print('dummy.next.next.next:', dummy.next.next.next.val if dummy.next.next.val else None)
            res = res.next
        return res.val


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
print(Solution().addTwoNumbers(l1, l2))


>>>carry: 7
    res: 0
    res.next 7
    "carry": 0
    dummy: 0
    dummy.next: 7
    carry: 10
    res: 7
    res.next 0
    "carry": 1
    dummy: 0
    dummy.next: 7
    carry: 8
    res: 0
    res.next 8
    "carry": 0
    dummy: 0
    dummy.next: 7
    8
res keep moving forward
dummy didn't

'''



'''  
"""
Author: Huahua
Running time: 112 ms
"""
class Solution:
  def addTwoNumbers(self, l1, l2):
    s = 0
    dummy = ListNode(0)
    tail = dummy
    while l1 or l2 or s > 0:
      s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
      l1 = l1.next if l1 else None
      l2 = l2.next if l2 else None
      tail.next = ListNode(s % 10)
      s //= 10
      tail = tail.next
    return tail.val

'''
