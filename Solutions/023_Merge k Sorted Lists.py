'''
23. Merge k Sorted Lists

https://leetcode.com/problems/merge-k-sorted-lists/
similar problem: "21. Merge Two Sorted Lists"
https://leetcode.com/problems/merge-two-sorted-lists/

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

        dummy = ListNode(0)
        cur = dummy
        heap = []

        for i in range(len(lists)):
            heapq.heappush(heap, (lists[i].val, i, lists[i]))
            print('heap1', heap)
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            print('node', node)
            cur.next = node[2]
            cur = cur.next
            print(cur.val, cur)

            if cur.next:
                heapq.heappush(heap, (cur.next.val, idx, cur.next))
                print('cur.next:', cur.next.val)
                print('cur', cur.val)
                print('heap2', heap)
        return dummy.next

'''
Input:
[[1,4,5],[1,3,4],[2,6]]

output:
heap1 [(1, 0, <precompiled.listnode.ListNode object at 0x7f2f75dbec88>)]
heap1 [(1, 0, <precompiled.listnode.ListNode object at 0x7f2f75dbec88>), (1, 1, <precompiled.listnode.ListNode object at 0x7f2f75dbed68>)]
heap1 [(1, 0, <precompiled.listnode.ListNode object at 0x7f2f75dbec88>), (1, 1, <precompiled.listnode.ListNode object at 0x7f2f75dbed68>), (2, 2, <precompiled.listnode.ListNode object at 0x7f2f75dc6240>)]
node (1, 0, <precompiled.listnode.ListNode object at 0x7f2f75dbec88>)
1 <precompiled.listnode.ListNode object at 0x7f2f75dbec88>
cur.next: 4
cur 1
heap2 [(1, 1, <precompiled.listnode.ListNode object at 0x7f2f75dbed68>), (2, 2, <precompiled.listnode.ListNode object at 0x7f2f75dc6240>), (4, 0, <precompiled.listnode.ListNode object at 0x7f2f75dbecf8>)]
node (1, 1, <precompiled.listnode.ListNode object at 0x7f2f75dbed68>)
1 <precompiled.listnode.ListNode object at 0x7f2f75dbed68>
cur.next: 3
cur 1
heap2 [(2, 2, <precompiled.listnode.ListNode object at 0x7f2f75dc6240>), (4, 0, <precompiled.listnode.ListNode object at 0x7f2f75dbecf8>), (3, 1, <precompiled.listnode.ListNode object at 0x7f2f75dbeda0>)]
node (2, 2, <precompiled.listnode.ListNode object at 0x7f2f75dc6240>)
2 <precompiled.listnode.ListNode object at 0x7f2f75dc6240>
cur.next: 6
cur 2
heap2 [(3, 1, <precompiled.listnode.ListNode object at 0x7f2f75dbeda0>), (4, 0, <precompiled.listnode.ListNode object at 0x7f2f75dbecf8>), (6, 2, <precompiled.listnode.ListNode object at 0x7f2f75dc6320>)]
node (3, 1, <precompiled.listnode.ListNode object at 0x7f2f75dbeda0>)
3 <precompiled.listnode.ListNode object at 0x7f2f75dbeda0>
cur.next: 4
cur 3
heap2 [(4, 0, <precompiled.listnode.ListNode object at 0x7f2f75dbecf8>), (6, 2, <precompiled.listnode.ListNode object at 0x7f2f75dc6320>), (4, 1, <precompiled.listnode.ListNode object at 0x7f2f75dbedd8>)]
node (4, 0, <precompiled.listnode.ListNode object at 0x7f2f75dbecf8>)
4 <precompiled.listnode.ListNode object at 0x7f2f75dbecf8>
cur.next: 5
cur 4
heap2 [(4, 1, <precompiled.listnode.ListNode object at 0x7f2f75dbedd8>), (6, 2, <precompiled.listnode.ListNode object at 0x7f2f75dc6320>), (5, 0, <precompiled.listnode.ListNode object at 0x7f2f75dbed30>)]
node (4, 1, <precompiled.listnode.ListNode object at 0x7f2f75dbedd8>)
4 <precompiled.listnode.ListNode object at 0x7f2f75dbedd8>
node (5, 0, <precompiled.listnode.ListNode object at 0x7f2f75dbed30>)
5 <precompiled.listnode.ListNode object at 0x7f2f75dbed30>
node (6, 2, <precompiled.listnode.ListNode object at 0x7f2f75dc6320>)
6 <precompiled.listnode.ListNode object at 0x7f2f75dc6320>
'''

'''

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
heapq.heapreplace(heap.item)
注：删除最小元素值，添加新的元素值

>> list
[1, 2, 3, 5, 6, 5, 8, 9]
>> heapq.heapreplace(list,99)
1
>> list
[2, 5, 3, 9, 6, 5, 8, 99]
-------------------------------------------------
heapq.heappop(heap)
注：删除最小值，因为堆的特征是heap[0]永远是最小的元素，所以一般都是删除第一个元素。

>> list
[1, 1, 3, 5, 2, 5, 8, 9, 6]
>> heapq.heappop(list)
1
>> list
[1, 2, 3, 5, 6, 5, 8, 9]
-------------------------------------------------

'''



