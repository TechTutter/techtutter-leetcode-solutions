from solution import Solution, ListNode
from typing import List, Optional


def to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def from_list(vals: List[int]) -> Optional[ListNode]:
    if not vals:
        return None
    head = ListNode(vals[0])
    curr = head
    for i in range(1, len(vals)):
        curr.next = ListNode(vals[i])
        curr = curr.next
    return head


class TestSolution:
    def test_reverseKGroup_example1(self):
        sol = Solution()
        head = from_list([1, 2, 3, 4, 5])
        k = 2
        result = sol.reverseKGroup(head, k)
        assert to_list(result) == [2, 1, 4, 3, 5]

    def test_reverseKGroup_example2(self):
        sol = Solution()
        head = from_list([1, 2, 3, 4, 5])
        k = 3
        result = sol.reverseKGroup(head, k)
        assert to_list(result) == [3, 2, 1, 4, 5]

    def test_reverseKGroup_k1(self):
        sol = Solution()
        head = from_list([1, 2, 3])
        k = 1
        result = sol.reverseKGroup(head, k)
        assert to_list(result) == [1, 2, 3]

    def test_reverseKGroup_empty(self):
        sol = Solution()
        head = from_list([])
        k = 1
        result = sol.reverseKGroup(head, k)
        assert to_list(result) == []