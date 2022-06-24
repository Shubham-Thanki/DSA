# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0

        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))

    def diameterOfBinaryTree(self, root) -> int:
        if not root:
            return 0
        d1 = self.diameterOfBinaryTree(root.left)
        d2 = self.diameterOfBinaryTree(root.right)
        cur = self.maxDepth(root.left)+self.maxDepth(root.right)
        return max(cur, d1, d2)

# Here, a bigger binary tree can have large number of subtrees where in it might be possible that in some cases
# we will have the diameter of a Btree excluding the root node. This algorithm will recursively check for the diameter
# in every possible subtree of a subtree. O(n^2)

# https://leetcode.com/problems/diameter-of-binary-tree/

# To further reduce the time complexity to O(n)

# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         diameter=0
#         def dfs(root):  This Function returns the max height
#             nonlocal diameter  --> nonlocal keyword is used to work with variables inside nested functions. It declares
#.                                    the variable to be not local.
#             if not root:
#                 return 0

#             left=dfs(root.left)
#             right=dfs(root.right)
#             diameter=max(diameter,left+right) <--- Checking for the larger diameter while calculating the max height
#                                                    so that we have to visit each node only once.

#             return 1+max(left,right) <---- This is the max height

#         dfs(root)
#         return diameter
