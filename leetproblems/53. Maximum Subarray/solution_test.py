from solution import Solution


class TestMaxSubArray:
    def test_testcase1(self):
        assert Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6

    def test_testcase2(self):
        assert Solution().maxSubArray([1]) == 1

    def test_testcase3(self):
        assert Solution().maxSubArray([5,4,-1,7,8]) == 23
