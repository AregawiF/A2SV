# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        q = deque([root])
        count = 0
        while q:
            level = []
            current = defaultdict(int)
            i = 0
            for _ in range(len(q)):
                curr = q.popleft()
                level.append(curr.val)
                current[curr.val] = i
                i += 1
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            sortedlevel = sorted(level)
            for i in range(len(level)):
                if level[i] != sortedlevel[i]:
                    ind1, ind2 = i, current[sortedlevel[i]]

                    level[ind1], level[ind2] = level[ind2], level[ind1]
                    current[level[ind1]] = ind1
                    current[level[ind2]] = ind2
                    count += 1

        return count
                    
            
            