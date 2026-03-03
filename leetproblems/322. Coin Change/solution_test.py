from solution import Solution


class TestCoinChange:
    def test_testcase1(self):
        assert Solution().coinChange([1,2,5], 11) == 3
    
    def test_testcase2(self):
        assert Solution().coinChange([2], 3) == -1
    
    def test_testcase3(self):
        assert Solution().coinChange([1], 0) == 0

