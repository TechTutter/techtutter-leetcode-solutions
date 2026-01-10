from solution import Solution

class TestJumpGameII:
    def test_testcase1(self):
        assert Solution().jump([2,3,1,1,4]) == 2

    def test_testcase2(self):
        assert Solution().jump([2,3,0,1,4]) == 2
