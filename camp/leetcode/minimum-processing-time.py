class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        
        processorTime.sort()
        tasks.sort(reverse = True)
        res = 0
        n = len(processorTime)
        for i in range(n):
            res = max(res, processorTime[i] + tasks[4*(i)])

        return res