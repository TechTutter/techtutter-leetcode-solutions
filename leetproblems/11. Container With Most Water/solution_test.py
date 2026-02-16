from solution import Solution


class TestExerciseName:
    def test_testcase1(self):
        assert Solution().maxArea([1,8,6,2,5,4,8,3,7]) == 49
    
    def test_testcase2(self):
        assert Solution().maxArea([1,1]) == 1

