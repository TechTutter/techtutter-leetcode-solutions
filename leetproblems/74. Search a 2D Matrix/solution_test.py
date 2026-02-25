from solution import Solution


class TestExerciseName:
    def test_testcase1(self):
        assert Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3) is True

    def test_testcase2(self):
        assert Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13) is False
