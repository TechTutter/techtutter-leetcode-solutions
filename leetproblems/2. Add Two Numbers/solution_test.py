from solution import Solution, ListNode


class TestAddTwoNumbers:
    def test_testcase1(self):
        s = Solution()
        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))
        assert s.addTwoNumbers(l1, l2) == ListNode(7, ListNode(0, ListNode(8)))