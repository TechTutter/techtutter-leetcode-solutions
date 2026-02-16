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
        n = 2
        expected = ListNode(1, ListNode(2, ListNode(3, ListNode(5))))
        Solution().removeNthFromEnd(head, n)

        assert checkSolution(head, expected)

    def test_testcase2(self):
        head = ListNode(1)
        n = 1
        expected = None
        Solution().removeNthFromEnd(head, n)

        assert checkSolution(head, expected)

    def test_testcase3(self):
        head = ListNode(1, ListNode(2))
        n = 1
        expected = ListNode(1)
        Solution().removeNthFromEnd(head, n)

        assert checkSolution(head, expected)
        
            


