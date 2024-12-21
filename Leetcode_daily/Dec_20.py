# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        q = deque([root])
        height = -1
        while q:
            level = []
            height += 1
            if height % 2 != 0:
                for i in range(len(q)):
                    level.append(q[i].val)

                level.reverse()

            ind = 0
            for _ in range(len(q)):
                curr = q.popleft()
                if level:
                    curr.val = level[ind]
                    ind += 1

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return root