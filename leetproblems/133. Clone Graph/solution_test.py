from solution import Solution, Node


class TestCloneGraph:
    def test_testcase1(self):
        s = Solution()

        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)

        n1.neighbors = [n2, n4]
        n2.neighbors = [n1, n3]
        n3.neighbors = [n2, n4]
        n4.neighbors = [n1, n3]

        clone = s.cloneGraph(n1)
        assert clone is not None
        assert n1.val == clone.val
        assert n1.neighbors[0].val == clone.neighbors[0].val
        assert n1.neighbors[1].val == clone.neighbors[1].val

