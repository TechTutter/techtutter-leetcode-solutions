from solution import Solution


class TestSurroundedRegions:
    def test_testcase1(self):
        board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
        expected = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
        Solution().solve(board)
        assert board == expected

    def test_testcase2(self):
        board = [["X"]]
        expected = [["X"]]
        Solution().solve(board)
        assert board == expected