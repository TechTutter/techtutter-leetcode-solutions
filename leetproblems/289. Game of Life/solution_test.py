from solution import Solution


class TestGameOfLife:
    def test_testcase1(self):
        board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
        Solution().gameOfLife(board)
        assert board == [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

    def test_testcase2(self):
        board = [[1,1],[1,0]]
        Solution().gameOfLife(board)
        assert board == [[1,1],[1,1]]

