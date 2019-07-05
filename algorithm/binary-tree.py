'''
Binary Tree Preorder Traversal

https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/928/
https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/929/
https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/930/

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res

# pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。

# reference:
# https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/

# Python program to for tree traversals

# A class that represents an individual node in a
# Binary Tree

# --------------------------------------------

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                res.append(node.val)
                root = node.right
        return res
    # 先把迭代到最左边的叶子节点，把所有途中的root放进stack，当左边走不通了，
    # 开始往res里面存数，并往右边走。


# reference:
# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/929/discuss/158278/Python-Stack-or-DFS-tm

# --------------------------------------------


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    res.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return res

# 每次往Stack里面储存的顺序是，先存储当前root，然后right，最后left，这样当pop到最左边叶子节点的时候，
# 就为第一个print的数，因为我们每次pop完之后的root之后还会用到，所以这里利用flag，
# 每次及时使用完root也将root重新放回stack，在之后pop过程中再检查flag，如果visited过，则不再放回stack。

# reference:
# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/930/discuss/158289/Python-DFS-or-Stack-tm

# --------------------------------------------
'''
code:


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

        # A function to do inorder tree traversal
        
def printPreorder(root):
    if root:
        # First print the data of node
        print(root.val),

        # Then recur on left child
        printPreorder(root.left)

        # Finally recur on right child
        printPreorder(root.right)

        # Driver code


def printInorder(root):
    if root:
        # First recur on left child
        printInorder(root.left)

        # then print the data of node
        print(root.val),

        # now recur on right child
        printInorder(root.right)

        # A function to do postorder tree traversal


def printPostorder(root):
    if root:
        # First recur on left child
        printPostorder(root.left)

        # the recur on right child
        printPostorder(root.right)

        # now print the data of node
        print(root.val),

        # A function to do preorder tree traversal


'''
