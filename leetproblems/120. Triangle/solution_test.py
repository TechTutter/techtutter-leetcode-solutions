from solution import Solution


class TestTriangle:
    def test_testcase1(self):
        assert Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]) == 11

    def test_testcase2(self):
        assert Solution().minimumTotal([[-10]]) == -10

