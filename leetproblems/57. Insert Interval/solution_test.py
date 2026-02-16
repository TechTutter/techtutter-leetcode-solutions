from solution import Solution

class TestExerciseName:
    def test_testcase1(self):
        s = Solution()
        intervals = [[1,3],[6,9]]
        newInterval = [2,5]
        assert s.insert(intervals, newInterval) == [[1,5],[6,9]]

    def test_testcase2(self):
        s = Solution()
        intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
        newInterval = [4,8]
        assert s.insert(intervals, newInterval) == [[1,2],[3,10],[12,16]]

