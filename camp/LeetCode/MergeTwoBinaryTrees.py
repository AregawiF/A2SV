# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # if root1 is None :
        #     return root2
        # if root2 is None:
        #     return root1
        
        def merge(node1, node2):
            if not node1 and not node2:
                return None
            
            if node1:
                val1 = node1.val
            else:
                val1 = 0
                
            if node2:
                val2 = node2.val
            else:
                val2 = 0

            merged_val = val1 + val2
            merged_node = TreeNode(merged_val)
            
            if node1:
                left_node1 = node1.left
            else:
                left_node1 = None
                
            if node2:
                left_node2 = node2.left
            else:
                left_node2 = None

            merged_node.left = merge(left_node1, left_node2)
            
            if node1:
                right_node1 = node1.right
            else:
                right_node1 = None
                
            if node2:
                right_node2 = node2.right
            else:
                right_node2 = None

            merged_node.right = merge(right_node1, right_node2)

            return merged_node
        
        return merge(root1, root2)