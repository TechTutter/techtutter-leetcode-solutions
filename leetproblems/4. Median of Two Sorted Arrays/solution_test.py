from solution import Solution


class TestExerciseName:
    def test_testcase1(self):
        assert Solution().findMedianSortedArrays([1, 3], [2]) == 2

    def test_testcase2(self):
        assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5

