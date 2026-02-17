from solution import Solution

class TestSolution:
    def test_testcase1(self):
        solution = Solution()
        points = [[10,16],[2,8],[1,6],[7,12]]
        assert solution.findMinArrowShots(points) == 2

    def test_testcase2(self):
        solution = Solution()
        points = [[1,2],[3,4],[5,6],[7,8]]
        assert solution.findMinArrowShots(points) == 4

    def test_testcase3(self):
        solution = Solution()
        points = [[1,2],[2,3],[3,4],[4,5]]
        assert solution.findMinArrowShots(points) == 2