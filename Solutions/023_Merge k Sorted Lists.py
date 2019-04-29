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
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
                print('heap1', heap)
        while heap:
            node = heapq.heappop(heap)
            print('node', node)
            index = node[1]
            cur.next = node[2]
            cur = cur.next

            if cur.next:
                heapq.heappush(heap, (cur.next.val, index, cur.next))

                print('cur', cur.val)
                print('heap2', heap)
        return dummy.next

'''
output:

heap1 [(1, 0, <precompiled.listnode.ListNode object at 0x7fb7276edcc0>)]
heap1 [(1, 0, <precompiled.listnode.ListNode object at 0x7fb7276edcc0>), (1, 1, <precompiled.listnode.ListNode object at 0x7fb7276edda0>)]
heap1 [(1, 0, <precompiled.listnode.ListNode object at 0x7fb7276edcc0>), (1, 1, <precompiled.listnode.ListNode object at 0x7fb7276edda0>), (2, 2, <precompiled.listnode.ListNode object at 0x7fb7276f5278>)]
node (1, 0, <precompiled.listnode.ListNode object at 0x7fb7276edcc0>)
cur 1
heap2 [(1, 1, <precompiled.listnode.ListNode object at 0x7fb7276edda0>), (2, 2, <precompiled.listnode.ListNode object at 0x7fb7276f5278>), (4, 0, <precompiled.listnode.ListNode object at 0x7fb7276edd30>)]
node (1, 1, <precompiled.listnode.ListNode object at 0x7fb7276edda0>)
cur 1
heap2 [(2, 2, <precompiled.listnode.ListNode object at 0x7fb7276f5278>), (4, 0, <precompiled.listnode.ListNode object at 0x7fb7276edd30>), (3, 1, <precompiled.listnode.ListNode object at 0x7fb7276eddd8>)]
node (2, 2, <precompiled.listnode.ListNode object at 0x7fb7276f5278>)
cur 2
heap2 [(3, 1, <precompiled.listnode.ListNode object at 0x7fb7276eddd8>), (4, 0, <precompiled.listnode.ListNode object at 0x7fb7276edd30>), (6, 2, <precompiled.listnode.ListNode object at 0x7fb7276f5358>)]
node (3, 1, <precompiled.listnode.ListNode object at 0x7fb7276eddd8>)
cur 3
heap2 [(4, 0, <precompiled.listnode.ListNode object at 0x7fb7276edd30>), (6, 2, <precompiled.listnode.ListNode object at 0x7fb7276f5358>), (4, 1, <precompiled.listnode.ListNode object at 0x7fb7276ede10>)]
node (4, 0, <precompiled.listnode.ListNode object at 0x7fb7276edd30>)
cur 4
heap2 [(4, 1, <precompiled.listnode.ListNode object at 0x7fb7276ede10>), (6, 2, <precompiled.listnode.ListNode object at 0x7fb7276f5358>), (5, 0, <precompiled.listnode.ListNode object at 0x7fb7276edd68>)]
node (4, 1, <precompiled.listnode.ListNode object at 0x7fb7276ede10>)
node (5, 0, <precompiled.listnode.ListNode object at 0x7fb7276edd68>)
node (6, 2, <precompiled.listnode.ListNode object at 0x7fb7276f5358>)
'''




