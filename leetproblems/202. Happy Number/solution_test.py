from solution import Solution

class TestHappyNumber:
    def test_testcase1(self):
        assert Solution().isHappy(19) == True

    def test_testcase2(self):
        assert Solution().isHappy(2) == False
