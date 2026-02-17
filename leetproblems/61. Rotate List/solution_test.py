from solution import Solution, ListNode

def checkSolution(head: Optional[ListNode], expected: Optional[ListNode]) -> bool:
    while head and expected:
        if head.val != expected.val:
            return False
        head = head.next
        expected = expected.next
    return head is None and expected is None

class TestExerciseName:
    def test_testcase1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        expected = ListNode(4, ListNode(5, ListNode(1, ListNode(2, ListNode(3)))))
        assert checkSolution(Solution().rotateRight(head, 2), expected) is True

    def test_testcase2(self):
        head = ListNode(0, ListNode(1, ListNode(2)))
        expected = ListNode(2, ListNode(0, ListNode(1)))
        assert checkSolution(Solution().rotateRight(head, 4), expected) is True 

