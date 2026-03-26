from solution import Solution


class TestMaxSubarraySumCircular:
    def test_testcase1(self):
        s = Solution()
        assert s.maxSubarraySumCircular([1, -2, 3, -2]) == 3

    def test_testcase2(self):
        s = Solution()
        assert s.maxSubarraySumCircular([5, -3, 5]) == 10

    def test_testcase3(self):
        s = Solution()
        assert s.maxSubarraySumCircular([-3, -2, -3]) == -2
        

