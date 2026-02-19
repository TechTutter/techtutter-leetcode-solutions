from solution import Solution


class TestExerciseName:
    def test_testcase1(self):
        assert Solution().plusOne([1,2,3]) == [1,2,4]
    
    def test_testcase2(self):
        assert Solution().plusOne([4,3,2,1]) == [4,3,2,2]
    
    def test_testcase3(self):
        assert Solution().plusOne([9]) == [1,0]

