from solution import Solution, Node

class TestSolution():
    root = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(7)))
    s = Solution()
    s.connect(root)
    
    assert root.next == None
    assert root.left.next == root.right
    assert root.right.next == None
    assert root.left.left.next == root.left.right
    assert root.left.right.next == root.right.right
    assert root.right.right.next == None