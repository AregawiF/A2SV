class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        maxim = max(arr)
        mind = arr.index(maxim)
        if mind == 0 or mind == len(arr) -1:
            return False
        print(maxim)
        print(mind)
        for i in range(mind):
            if arr[i] >= maxim or arr[i] >= arr[i+1]:
                return False
        for i in range(mind+1,len(arr)):
            if arr[i] >= maxim:
                return False
            if i+1 > len(arr)-1:
                break
            else:
                if arr[i] <= arr[i+1]:
                    return False
        return True

