class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        i = 0
        srtarr = False
        def flip(right):
            left = 0
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        def issorted(arr):
            if len(arr) == 1:
                return True
            for i in range(len(arr)-1):
                if arr[i] > arr[i+1]:
                    return False
            return True
        while not srtarr and arr:
            if len(arr) == 1:
                break
            maxim = max(arr)
            srtarr = issorted(arr)
            if not srtarr:
                maxind = arr.index(maxim) 
                if maxind == 0:
                    flip(len(arr)-1)
                    res.append(len(arr))
                else:
                    flip(maxind)
                    res.append(maxind+1)
                    flip(len(arr)-1)
                    res.append(len(arr))
                arr = arr[:len(arr)-1]
                i += 1
        
        return res