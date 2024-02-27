# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        mydict = {}
        
        def traverse(node):
            if not node:
                return 
            
            if node.val not in mydict:
                mydict[node.val] = 1
            else:
                mydict[node.val] += 1
            
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        maxval = max(mydict.values())
        # print(mydict)
        # print(maxval)
        result = []
        for key,val in mydict.items():
            if val == maxval:
                result.append(key)
        return result