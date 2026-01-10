from solution import Solution

class TestCandy:
    def test_testcase1(self):
        assert Solution().candy([1,0,2]) == 5

    def test_testcase2(self):
        assert Solution().candy([1,2,2]) == 4
