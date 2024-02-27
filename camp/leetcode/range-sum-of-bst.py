# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def traverse(root):
            if not root:
                return 0
            ans = 0
            if low <= root.val <= high:
                ans+=root.val
            # print("ojij",ans)
            if root.val > low:
                ans+=traverse(root.left)
            if root.val < high:
                ans+=traverse(root.right)
            print(ans)
            return ans
        return traverse(root)