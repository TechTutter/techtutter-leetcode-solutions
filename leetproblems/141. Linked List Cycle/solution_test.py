from solution import Solution, ListNode

class TestHasCycle:
    def test_testcase1(self):
        n1 = ListNode(3)
        n2 = ListNode(2)
        n3 = ListNode(0)
        n4 = ListNode(4)
        n1.next = n2
        n2.next = n3
        n3.next = n4
        n4.next = n2
        assert Solution().hasCycle(n1) == True

    def test_testcase2(self):
        n1 = ListNode(1)
        n2 = ListNode(2)
        n1.next = n2
        n2.next = n1
        assert Solution().hasCycle(n1) == True

    def test_testcase3(self):
        n1 = ListNode(1)
        assert Solution().hasCycle(n1) == False
        