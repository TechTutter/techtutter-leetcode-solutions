from solution import Solution, ListNode


class TestExerciseName:
    def test_testcase1(self):
        head = ListNode(1)
        head.next = ListNode(1)
        head.next.next = ListNode(2)
        s = Solution()
        res = s.deleteDuplicates(head)
        assert res and res.val == 1
        assert res.next and res.next.val == 2
        assert res.next.next is None

    def test_testcase2(self):
        head = ListNode(1)
        head.next = ListNode(1)
        head.next.next = ListNode(2)
        head.next.next.next = ListNode(3)
        head.next.next.next.next = ListNode(3)
        s = Solution()
        res = s.deleteDuplicates(head)
        assert res and res.val == 1
        assert res.next and res.next.val == 2
        assert res.next.next and res.next.next.val == 3
        assert res.next.next.next is None

