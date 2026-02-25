import pytest
from solution import Solution


class TestExerciseName:
    def test_testcase1(self):
        assert Solution().findPeakElement([1,2,3,1]) == 2

    def test_testcase2(self):
        assert Solution().findPeakElement([1,2,1,3,5,6,4]) == 5
