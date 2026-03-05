from solution import Solution


class TestHammingWeight:
    def test_testcase1(self):
        assert Solution().hammingWeight(11) == 3

    def test_testcase2(self):
        assert Solution().hammingWeight(128) == 1

    def test_testcase3(self):
        assert Solution().hammingWeight(2147483645) == 30

