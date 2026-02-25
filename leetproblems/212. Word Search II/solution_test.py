from solution import Solution


class TestSolution:
    def test_testcase1(self):
        board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
        words = ["oath","pea","eat","rain"]
        assert Solution().findWords(board, words) == ["oath","eat"]

