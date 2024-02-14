class Solution(object):
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        """
        :type numOnes: int
        :type numZeros: int
        :type numNegOnes: int
        :type k: int
        :rtype: int
        """
        if k <= numOnes:
            return k
        else:
            if (numOnes + numZeros) >= k:
                return numOnes
            else:
                diff = k - (numOnes + numZeros)
                res = numOnes - diff
                return res