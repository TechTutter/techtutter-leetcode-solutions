from solution import BSTIterator, TreeNode

class TestSolution():
    n1 = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))
    iterator = BSTIterator(n1)
    assert iterator.next() == 3
    assert iterator.next() == 7
    assert iterator.hasNext() == True
    assert iterator.next() == 9
    assert iterator.hasNext() == True
    assert iterator.next() == 15
    assert iterator.hasNext() == True
    assert iterator.next() == 20
    assert iterator.hasNext() == False