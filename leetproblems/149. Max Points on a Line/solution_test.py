import pytest
from solution import Solution


class TestMaxPointsOnALine:
    def test_testcase1(self):
        assert Solution().maxPoints([[1, 1], [2, 2], [3, 3]]) == 3

    def test_testcase2(self):
        assert (
            Solution().maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]) == 4
        )

    def test_testcase3(self):
        assert Solution().maxPoints([[1, 1], [1, 1], [1, 1]]) == 3
