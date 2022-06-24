# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# p and q are the root nodes given of the 2 different trees
class Solution:
    def isSameTree(self, p, q) -> bool:
        if not p and not q:
            return True

        if not p or not q:  # If either of the nodes are empty that means the structure is different and hence we return False
            return False

        if p.val != q.val:
            return False

        l = self.isSameTree(p.left, q.left)
        r = self.isSameTree(p.right, q.right)

        if l and r:
            return True
        else:
            return False


# https://leetcode.com/problems/same-tree
