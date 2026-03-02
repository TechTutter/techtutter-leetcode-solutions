from solution import Solution


class TestClimbingStairs:
    def test_testcase1(self):
        s = Solution()
        assert s.climbStairs(2) == 2

    def test_testcase2(self):
        s = Solution()
        assert s.climbStairs(3) == 3

    def test_testcase3(self):
        s = Solution()
        assert s.climbStairs(25) == 121393

