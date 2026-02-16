class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]

        res = []
        start, end = None, None
        i, n = 0, len(intervals)

        # find starting position of newInterval
        while i < n:
            if intervals[i][1] >= newInterval[0]:
                if newInterval[1] < intervals[i][0]:
                    start = newInterval[0]
                    end = newInterval[1]
                else:
                    start = min(intervals[i][0], newInterval[0])
                    end = max(intervals[i][1], newInterval[1])
                break
            else:
                res.append(intervals[i])
            i += 1
        
        # merge until possible and append
        while i < n and intervals[i][0] <= end:
            end = max(intervals[i][1], end)
            i += 1

        if end is None:
            res.append(newInterval)
        else:
            res.append([start, end]) 

        # append remaining values
        if i < n: res.extend(intervals[i:])

        return res