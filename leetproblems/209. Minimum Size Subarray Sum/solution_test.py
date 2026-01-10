from solution import Solution

class TestMinSizeSubarraySum:
    def test_testcase1(self):
        assert Solution().minSubArrayLen(7, [2,3,1,2,4,3]) == 2

    def test_testcase2(self):
        assert Solution().minSubArrayLen(4, [1,4,4]) == 1

    def test_testcase3(self):
        assert Solution().minSubArrayLen(11, [1,1,1,1,1,1,1,1]) == 0
