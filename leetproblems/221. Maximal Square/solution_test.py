from solution import Solution


class TestMaximalSquare:
    def test_testcase1(self):
        s = Solution()
        res = s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
        assert res == 4

    def test_testcase2(self):
        s = Solution()
        res = s.maximalSquare([["0","1"],["1","0"]])
        assert res == 1
    
    def test_testcase3(self):
        s = Solution()
        res = s.maximalSquare([["0"]])
        assert res == 0
