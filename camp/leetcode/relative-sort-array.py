class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        result = []
        arr1.sort()
        for num2 in arr2:   
            for i in range(len(arr1)):
                if arr1[i] == num2:
                    result.append(arr1[i])
        for i in range(len(arr1)):
            if arr1[i] not in arr2:
                result.append(arr1[i])
        return result
