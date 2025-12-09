from solution import Solution

class TestExerciseName:
    def test_testcase1(self):
        assert Solution().maxProfit([7,1,5,3,6,4]) == 7

    def test_testcase2(self):
        assert Solution().maxProfit([1,2,3,4,5]) == 4

    def test_testcase3(self):
        assert Solution().maxProfit([7,6,4,3,1]) == 0