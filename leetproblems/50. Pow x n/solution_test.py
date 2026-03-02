from solution import Solution


class TestPowXN:
    def test_testcase1(self):
        assert Solution().myPow(2.00000, 10) == 1024.00000

    def test_testcase2(self):
        assert Solution().myPow(2.10000, 3) == 9.261000000000001

    def test_testcase3(self):
        assert Solution().myPow(2.00000, -2) == 0.25000

