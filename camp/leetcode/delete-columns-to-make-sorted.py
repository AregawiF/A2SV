class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        col = len(strs[0])
        ans = 0
        for c in range(col):
            for i in range(len(strs)-1):
                if strs[i][c] > strs[i+1][c]:
                    ans += 1
                    break
        return ans

        