from solution import Solution


class TestLongestIncreasingSubsequence:
    def test_testcase1(self):
        assert Solution().lengthOfLIS([10,9,2,5,3,7,101,18]) == 4

    def test_testcase2(self):
        assert Solution().lengthOfLIS([0,1,0,3,2,3]) == 4

    def test_testcase3(self):
        assert Solution().lengthOfLIS([7,7,7,7,7,7,7]) == 1

