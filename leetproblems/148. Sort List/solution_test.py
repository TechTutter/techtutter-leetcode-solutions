from solution import ListNode, Solution


class TestExerciseName:
    def test_testcase1(self):
        head = ListNode(4)
        head.next = ListNode(2)
        head.next.next = ListNode(1)
        head.next.next.next = ListNode(3)

        s = Solution()
        res = s.sortList(head)
        assert res and res.val == 1
        assert res.next and res.next.val == 2
        assert res.next.next and res.next.next.val == 3
        assert res.next.next.next and res.next.next.next.val == 4

    def test_testcase2(self):
        head = ListNode(-1)
        head.next = ListNode(5)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(0)

        s = Solution()
        res = s.sortList(head)
        assert res and res.val == -1
        assert res.next and res.next.val == 0
        assert res.next.next and res.next.next.val == 3
        assert res.next.next.next and res.next.next.next.val == 4
        assert res.next.next.next.next and res.next.next.next.next.val == 5

