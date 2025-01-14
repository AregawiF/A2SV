class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        collA = set()
        collB = set()
        ans = [0] * n
        for i in range(n):
            collA.add(A[i])
            collB.add(B[i])
            ans[i] = len(collA.intersection(collB))
        return ans
            