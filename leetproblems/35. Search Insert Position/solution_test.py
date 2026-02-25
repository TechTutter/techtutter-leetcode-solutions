from solution import Solution


class TestExerciseName:
    def test_testcase1(self):
        assert Solution().searchInsert([1,3,5,6], 5) == 2
    
    def test_testcase2(self):
        assert Solution().searchInsert([1,3,5,6], 2) == 1
    
    def test_testcase3(self):
        assert Solution().searchInsert([1,3,5,6], 7) == 4
    
    def test_testcase4(self):
        assert Solution().searchInsert([1,3,5,6], 0) == 0
