class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def calc_gain(passes, total):
            return (passes + 1) / (total + 1) - passes / total

        max_heap = []
        for passes, total in classes:
            gain = calc_gain(passes, total)
            heapq.heappush(max_heap, (-gain, passes, total))
        
        for _ in range(extraStudents):
            current_gain, passes, total = heappop(max_heap)
            newgain = calc_gain(passes + 1, total + 1)
            heappush(max_heap, (-newgain, passes + 1, total + 1))

        ans = 0
        while max_heap:
            _, passes, total_students = heapq.heappop(max_heap)
            ans += passes / total_students
        return ans / len(classes)


            