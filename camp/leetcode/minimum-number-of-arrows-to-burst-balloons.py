class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        
        points.sort(key=lambda x: x[1])
        
        result = 1
        arrow = points[0][1] 
        
        for i in range(1, len(points)):
            if points[i][0] > arrow:
                result += 1
                arrow = points[i][1]
            else:
                if points[i][1] < arrow:
                    arrow = points[i][1]
        return result