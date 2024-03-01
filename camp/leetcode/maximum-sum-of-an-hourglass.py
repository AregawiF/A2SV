class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = float('-inf')

        for r in range(m - 2):
            for c in range(n - 2):
                currmax = 0  
                for i in range(3):
                    for j in range(3):
                        if i == 1 and (j == 0 or j == 2): 
                            continue
                        # if i == 1: 
                        #     j = 1
                        currmax += grid[r + i][c + j]
                
                res = max(res, currmax)
        
        return res