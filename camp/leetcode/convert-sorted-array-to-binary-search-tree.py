# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # currmid = (len(nums) / 2).ceil()
        def tobst(left, right):
            if left > right:
                return None
            currmid = ((left + right)//2)
            # root = TreeNode(currmid)
            rootleft = tobst(left, currmid-1)
            rootright = tobst(currmid+1, right)
            return TreeNode(nums[currmid], rootleft, rootright)
        return tobst(0,(len(nums)-1))