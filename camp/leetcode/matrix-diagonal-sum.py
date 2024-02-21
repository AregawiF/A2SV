class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        s = 0
        m = []
        myset = set()
        j = cols-1
        for i in range(rows):
            myset.add((i,i))
            myset.add((i,j))
            j -= 1
        ans = 0
        for ind in myset:
            ans += mat[ind[0]][ind[1]]
        return ans
        