from math import inf

class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        """
        1. sort by x_start, x_end -> [[1,6], [2,8], [7, 12] [10,16]]
        2. iterate over all points
            if i-th range fit, merge range_limits keeping max start and min end
            else arrow_count += 1 and reset range limits
        """
        if not points:
            return 0
            
        end = inf
        arrow_count = 1
        points.sort(key=lambda p : p[0])

        for p in points:
            a, b = p[0], p[1]
            if a <= end:
                end = min(end, b)
            else:
                arrow_count += 1
                end = p[1]
        
        return arrow_count