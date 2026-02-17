import pytest
from solution import Solution


class TestExerciseName:
    def test_testcase1(self):
        s = Solution()
        a = "11"
        b = "1"
        assert s.addBinary(a, b) == "100"

    def test_testcase2(self):
        s = Solution()
        a = "1010"
        b = "1011"
        assert s.addBinary(a, b) == "10101"