from solution import Solution

class TestSpiralMatrix:
    def test_testcase1(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        assert Solution().spiralOrder(matrix) == [1,2,3,6,9,8,7,4,5]

    def test_testcase2(self):
        matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        assert Solution().spiralOrder(matrix) == [1,2,3,4,8,12,11,10,9,5,6,7]
