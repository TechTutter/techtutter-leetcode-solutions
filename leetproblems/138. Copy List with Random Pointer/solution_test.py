from solution import Solution, Node
from typing import List, Optional, Any


def from_list(data: List[List[Any]]) -> Optional[Node]:
    if not data:
        return None
    
    nodes = [Node(val) for val, _ in data]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    for i, (_, rand_idx) in enumerate(data):
        if rand_idx is not None:
            nodes[i].random = nodes[rand_idx]
            
    return nodes[0]


def to_list(head: Optional[Node]) -> List[List[Any]]:
    if not head:
        return []
    
    nodes = []
    curr = head
    while curr:
        nodes.append(curr)
        curr = curr.next
    
    node_to_idx = {node: i for i, node in enumerate(nodes)}
    
    result = []
    for node in nodes:
        rand_idx = node_to_idx.get(node.random) if node.random else None
        result.append([node.val, rand_idx])
        
    return result


class TestSolution:
    def test_case1(self):
        data = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
        head = from_list(data)
        sol = Solution()
        copy = sol.copyRandomList(head)
        
        # Check deep copy: values and structure match
        assert to_list(copy) == data
        
        # Check deep copy: objects are different
        curr_orig = head
        curr_copy = copy
        while curr_orig:
            assert curr_orig is not curr_copy
            if curr_orig.random:
                assert curr_orig.random is not curr_copy.random
            curr_orig = curr_orig.next
            curr_copy = curr_copy.next

    def test_case2(self):
        data = [[1, 1], [2, 1]]
        head = from_list(data)
        sol = Solution()
        copy = sol.copyRandomList(head)
        assert to_list(copy) == data

    def test_case3(self):
        data = [[3, None], [3, 0], [3, None]]
        head = from_list(data)
        sol = Solution()
        copy = sol.copyRandomList(head)
        assert to_list(copy) == data

    def test_null(self):
        sol = Solution()
        assert sol.copyRandomList(None) is None