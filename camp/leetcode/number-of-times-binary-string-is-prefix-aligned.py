class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        n = len(flips)
        curr = 0 
        count = 0  
        
        for i in range(n):
            curr = max(curr, flips[i]) 
            if curr == i + 1:
                count += 1
        
        return count
