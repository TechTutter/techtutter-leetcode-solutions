from solution import Solution 

class TestSolution:
    def test_case1(self):
        s = Solution()
        assert s.summaryRanges([0,1,2,4,5,7]) == ["0->2","4->5","7"]

    def test_case2(self):
        s = Solution()
        assert s.summaryRanges([0,2,3,4,6,8,9]) == ["0","2->4","6","8->9"]

    def test_case3(self):
        s = Solution()
        assert s.summaryRanges([]) == []