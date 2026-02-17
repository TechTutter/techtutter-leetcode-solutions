from solution import Solution


class TestExerciseName:
    def test_testcase1(self):
        s = Solution()
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        assert s.merge(intervals) == [[1,6],[8,10],[15,18]]

    def test_testcase2(self):
        s = Solution()
        intervals = [[1,4],[4,5]]
        assert s.merge(intervals) == [[1,5]]

    def test_testcase3(self):
        s = Solution()
        intervals = [[4,7],[1,4]]
        assert s.merge(intervals) == [[1,7]]

