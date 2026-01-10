from solution import Solution

class TestJumpGame:
    def test_testcase1(self):
        assert Solution().canJump([2,3,1,1,4]) == True

    def test_testcase2(self):
        assert Solution().canJump([3,2,1,0,4]) == False
