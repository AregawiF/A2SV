class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        temp = [0] * 1001
        for passengers, start, end in trips:
            temp[start] += passengers
            temp[end] -= passengers
        
        curr = 0
        for count in temp:
            curr += count
            if curr > capacity:
                return False
        
        return True
