# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmTree(b1, b2):
            if not b1 and not b2:
                return True
            if not b1 or not b2:
                return False
            return b1.val == b2.val and symmTree(b1.left, b2.right) and symmTree(b1.right, b2.left)

        return symmTree(root.left, root.right)