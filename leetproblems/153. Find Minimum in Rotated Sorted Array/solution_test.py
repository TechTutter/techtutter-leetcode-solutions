from solution import Solution


class TestSolution:
    def test_testcase1(self):
        s = Solution()
        assert s.findMin([3,4,5,1,2]) == 1

    def test_testcase2(self):
        s = Solution()
        assert s.findMin([4,5,6,7,0,1,2]) == 0

    def test_testcase3(self):
        s = Solution()
        assert s.findMin([11,13,15,17]) == 11
