from solution import Solution, ListNode

def checkSolution(head: Optional[ListNode], expected: Optional[ListNode]) -> bool:
    while head and expected:
        assert head.val == expected.val
        head = head.next
        expected = expected.next

    return True  

class TestExerciseName:
    def test_testcase1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        left = 2
        right = 4
        expected = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5)))))
        Solution().reverseBetween(head, left, right)

        assert checkSolution(head, expected)

    def test_testcase2(self):
        head = ListNode(5)
        left = 1
        right = 1
        expected = ListNode(5)
        Solution().reverseBetween(head, left, right)

        assert checkSolution(head, expected)

