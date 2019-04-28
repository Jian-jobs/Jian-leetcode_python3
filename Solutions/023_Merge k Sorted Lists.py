'''
23. Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

解题思路：
归并k个已经排好序的链表。使用堆这一数据结构，首先将每条链表的头节点进入堆中，
然后将最小的弹出，并将最小的节点这条链表的下一个节点入堆，依次类推，
最终形成的链表就是归并好的链表。

-------------------------------------------------
reference：
入门堆（heapq）
https://blog.csdn.net/u013206202/article/details/78968438

heapq.heappush(heap,item)
注：heap为定义堆，item增加的元素

>> import heapq
>> h = []
>> heapq.heappush(h,2)
>> h
[2]
-------------------------------------------------
heapq.heapify(list)
注：将列表转换为堆

>> list = [1,2,3,5,1,5,8,9,6]
>> heapq.heapify(list)
>> list
[1, 1, 3, 5, 2, 5, 8, 9, 6]
-------------------------------------------------
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        '''

        :param lists: : List[ListNode]
        :return: ListNode
        '''
        import heapq
        result = ListNode(-1)
        cur = result
        p = list()
        x = 0
        for i in lists:
            if i:
                heapq.heappush(p, (i.val, i))

        while len(p)>0:
            cur.next = heapq.heappop(p)[1]
            cur = cur.next
            if cur.next:
                heapq.heappush(p, (cur.next.val, cur.next))

        return result.next




