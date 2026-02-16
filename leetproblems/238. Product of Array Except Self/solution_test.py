from solution import Solution

class TestSolution:
    def test_testcase1(self):
        assert Solution().productExceptSelf([1,2,3,4]) == [24,12,8,6]

    def test_testcase2(self):
        assert Solution().productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]