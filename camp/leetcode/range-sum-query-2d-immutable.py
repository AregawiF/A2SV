class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.prefix_sum = [[0 for _ in range((len(matrix[0]))+1)] for _ in range((len(matrix))+1)]
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                self.prefix_sum[i][j] =  self.prefix_sum[i-1][j] + self.prefix_sum[i][j-1] - self.prefix_sum[i-1][j-1] + matrix[i-1][j-1]   

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        submatrix_sum = self.prefix_sum[row2+1][col2+1] - self.prefix_sum[row2+1][col1+1 - 1] - self.prefix_sum[row1+1 - 1][col2+1 ] + self.prefix_sum[row1+1 - 1][col1+1 - 1]
        return submatrix_sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)