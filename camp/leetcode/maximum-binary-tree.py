# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:


        def construct(nums):
            if nums:
                maxim = max(nums)
                maxind = nums.index(maxim)
                root = TreeNode(maxim)
                
                root.left = construct(nums[:maxind])
                root.right = construct(nums[maxind+1:])
            else: return
            return root
        


        return construct(nums)