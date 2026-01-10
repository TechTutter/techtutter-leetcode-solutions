from solution import Solution

class TestHIndex:
    def test_testcase1(self):
        assert Solution().hIndex([3,0,6,1,5]) == 3

    def test_testcase2(self):
        assert Solution().hIndex([1,3,1]) == 1
