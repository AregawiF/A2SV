class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        res = len(arr)
        result = len(arr)
        arrdict = {}
        surplus = []
        for i in range(len(arr)):
            if arr[i] > res:
                surplus.append(arr[i])
        for i in range(len(arr)):
            if (arr[i] not in arrdict) and (arr[i]<=res):
                arrdict[arr[i]] = 1
            elif (arr[i] in arrdict) and (arr[i]<=res):
                surplus.append(arr[i])
        for _ in range(len(arr)):    
            if (res not in arrdict):
                if len(surplus) >0:    
                    if surplus[0] > res:
                        surplus[0] = res
                        arrdict[res] = 1
                        surplus.remove(surplus[0])
                    else:
                        curr_max = max(arrdict)
                        arrdict[curr_max] = res
                        result -= 1
                else:
                    curr_max = max(arrdict)
                    arrdict[curr_max] = res
                    result -= 1
            res -= 1
        return result

                

        
        
        
        
        # arr.sort()
        # if arr[0] != 1:
        #     arr[0] = 1
        # for i in range(1,len(arr)):
        #     if abs(arr[i] - arr[i-1]) > 1:
        #         arr[i] = arr[i-1] + 1
        # return max(arr)



        