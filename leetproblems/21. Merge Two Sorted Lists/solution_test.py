from solution import ListNode, Solution

class TestMergeTwoLists:
    def test_testcase1(self):
        s = Solution()
        l1 = ListNode(1, ListNode(2, ListNode(4)))
        l2 = ListNode(1, ListNode(3, ListNode(4)))
        assert s.mergeTwoLists(l1, l2) == ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))

    def test_testcase2(self):
        s = Solution()
        l1 = None
        l2 = None
        assert s.mergeTwoLists(l1, l2) == None

    def test_testcase3(self):
        s = Solution()
        l1 = ListNode(1)
        l2 = None
        assert s.mergeTwoLists(l1, l2) == ListNode(1)

