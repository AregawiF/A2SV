class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda lst: (lst[0] ** 2 + lst[1] ** 2))
        return points[:k]

        