# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root, subRoot) -> bool:

        # A null subRoot is a subtree of the root.
        if not subRoot:
            return True

        # But a not null subRoot is not a subtree of a null root.
        if not root:
            return False

        # Then we call the function to check if these are equal
        if self.sameTree(root, subRoot):
            return True

        # Then we call this same function recursively to make sure we traverse through all the nodes of the root.
        l = self.isSubtree(root.left, subRoot)
        r = self.isSubtree(root.right, subRoot)

        if l or r:
            return True
        else:
            return False

    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True

        if not root or not subRoot:
            return False

        if root.val == subRoot.val and self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right):
            return True

        return False

# https://leetcode.com/problems/subtree-of-another-tree/submissions/

# Wrong Solution
# l=self.isSubtree(root.left,subRoot)
# r=self.isSubtree(root.right,subRoot)
# k=sameTree(l,r)
# if k:
#     return True
# else:
#     return False
