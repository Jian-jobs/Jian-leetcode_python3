'''
445. Add Two Numbers II

https://leetcode.com/problems/add-two-numbers-ii/
similar problem: "002. Add Two Numbers"
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        '''
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        '''
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        answer = None
        carry = 0
        while stack1 and stack2:
            add = stack1.pop()+stack2.pop()+carry
            carry = add // 10
            temp = answer
            answer = ListNode(add % 10)
            answer.next = temp
        l = stack1 if stack1 else stack2
        while l:
            add = l.pop()+carry
            carry = add // 10
            temp = answer
            answer = ListNode(add % 10)
            answer.next = temp
        if carry:
            temp = answer
            answer = ListNode(1)
            answer.next = temp
        return answer

l1 = ListNode(7)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
print(Solution().addTwoNumbers(l1, l2))

'''
[]:list
(): tuple--"read-only lists"
{}: dictionary


思路：
1. l1.val， l2.val 存为 list named: stack1， stack2
2. list.pop()弹出最后一位相加为 carry
3.  cur.next 存上次的 cur值
    cur = ListNode(carry % 10)
    cur.next = nex.next
    nex.next = cur
4. 讨论： while stack1 and stack2， 
         if stack1 while stack1， 
         if stack2 while stack2， 
         if carry ==1:
5. return answer


submitted answer：

#class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        stk1 = []
        stk2 = []
        while l1:
            stk1.append(l1.val)
            l1= l1.next
        while l2:
            stk2.append(l2.val)
            l2= l2.next
        nex = ListNode(0)
        carry = 0
        while stk1 and stk2:
            carry+= stk1.pop()+stk2.pop()
            cur = ListNode(carry%10)
            carry //= 10
            cur.next = nex.next
            nex.next = cur
        if stk1:
            while stk1:
                carry += stk1.pop()
                cur = ListNode(carry % 10)
                carry //= 10
                cur.next = nex.next
                nex.next = cur
        if stk2:
            while stk2:
                carry += stk2.pop()
                cur = ListNode(carry % 10)
                carry //= 10
                cur.next = nex.next
                nex.next = cur
        if carry ==1:
            cur = ListNode(carry)

            cur.next = nex.next
            nex.next = cur

        return cur
'''