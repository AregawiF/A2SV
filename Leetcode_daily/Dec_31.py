class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        n = len(days)
        memo = {}
        def bt(idx, day, price):
            
            while idx < n:
                if days[idx] > day:
                    break
                idx += 1
            if idx >= n:
                return price
            
            state = (idx, day, price)
            if state not in memo:
                memo[state] = min(bt(idx, days[idx], price + costs[0]),
                                bt(idx, days[idx] + 6, price + costs[1]), 
                                bt(idx, days[idx] + 29, price + costs[2])) 

            return memo[state]

        return bt(0, 0, 0)