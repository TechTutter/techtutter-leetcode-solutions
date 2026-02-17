from math import inf

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        sort the intervals by starting index
        iterate over all intervals, push start, end to the response whenever current range does not fit
        """
        if not intervals:
            return []

        res = []

        intervals.sort(key=lambda x : x[0])
        start, end = intervals[0]

        for r in intervals:
            if r[0] <= end:
                end = max(end, r[1])
            else:
                res.append([start, end])
                start, end = r[0], r[1]
        res.append([start, end])

        return res