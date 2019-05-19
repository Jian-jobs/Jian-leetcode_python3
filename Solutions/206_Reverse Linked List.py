'''
206. Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/
similar problem: "24. Swap Nodes in Pairs"
https://leetcode.com/problems/swap-nodes-in-pairs/discuss/171788/Python-or-Dummynode-tm

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively.
Could you implement both?
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# Iterative(保持Head位置)
# 底下这种写法，保证了Head的位置不被移动，这种操作对于该题的定义毫无意义，
# 因为最终不需要head的reference，但如果API定义需要head的话，是个好的practice.
# 还有就是对prev和next两个指针的命名，提高了code的可读性。
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, cur =None, head
        while cur:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        return prev
# classical solution
class Solution:
    def reverseList(self, head):
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return prev
# recursive

'''
Step 1: Base Case:
if not head or not head.next:
    return head
Base Case的返回条件是当head或者head.next为空，则开始返回


Step 2: Recurse到底
new_head = self.reverseList(head.next)
在做任何处理之前，我们需要不断的递归，直到触及到Base Case,。当我们移动到最后一个Node以后, 将这个Node定义为我们新的head, 取名new_head. 我们从new_head开始重复性的往前更改指针的方向


Step 3: 返回并且更改指针方向
next_node = head.next    #        head -> next_node 
next_node.next = head    #        head <- next_node 
head.next = None         # [x] <- head <- next_node 

'''
class Solution:
    def reverseList(self, head):
        if not head or not head.next: return head
        new_head = self.reverseList(head.next)
        next_node = head.next
        next_node.next = head
        head.next =None

        return new_head

''''
思路：
https://leetcode.com/problems/reverse-linked-list/discuss/140916/Python-Iterative-and-Recursive-(206)

Iterative:
设置一个Prev的参数方便之后的操作。

Step 1: 保存head reference
在While循环中，cur指针用来保留当前Head的位置，因为如果我们操作 head = head.next这一步并且没有对head的位置进行保留， 
我们会失去对head的reference，导致我们之后不能进行反转操作。

Step 2: 保存head.next的reference
head的reference存好以后，我们还需要保存head.next的reference，原因是我们如果对第一个node进行了反转操作，
node就指向我们之前定义好的prev上，而失去了对原先head.next这个位置的拥有权。

head.next这个reference，我们直接用head来保存即可，所以有了head = head.next这么一个操作。
当然你要是想写的更加易懂，你也可以直接新创建一个函数，取名next，然后指向next = head.next。

Step 3: 反转
万事俱备，可以对cur指针进行反转了，指向之前定义的prev。

Step 4: Reference转移
最后不要忘记移动prev到cur的位置，不然prev的位置永远不变

'''



'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode, tail=None) -> ListNode:
        ''''''
        recursion
        :param head: ListNode
        :return: ListNode
        ''''''
        if head: head.next, tail, head = tail, head, head.next
        return self.reverseList(head, tail) if head else tail

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ''''''
        loop
        :param head: ListNode
        :return: ListNode
        ''''''
        # create tail, tail.next = None
        # start from node.val = 1
        # tail.next, head.next, head = head, tail.next, head.next
        # tail -> 1 -> Null
        tail = ListNode(0)
        # or None or 无论什么情况都存在的一个值： ListNode(float(-inf)
        while head: tail.next, head.next, head = head, tail.next, head.next
        return tail.next
# reverse order:
# tail = None
# --loop--
# tail = head
# head.next = tail
# head = head.next

'''
