from solution import Solution, ListNode 
class TestSolution():
    def test_partition(self):
        sol = Solution()
        l = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
        sol.partition(l, 3)

        curr = l
        assert curr.val == 1
        curr = curr.next
        assert curr.val == 2
        curr = curr.next
        assert curr.val == 2
        curr = curr.next
        assert curr.val == 4
        curr = curr.next
        assert curr.val == 3
        curr = curr.next
        assert curr.val == 5
        