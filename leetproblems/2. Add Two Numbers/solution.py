class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        return self.val == other.val and self.next == other.next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Apply sum_reversed on each input list
        """
        num_1 = self.sum_reversed(l1)
        num_2 = self.sum_reversed(l2)

        return self.from_int(num_1 + num_2)

    def sum_reversed(self, l: ListNode) -> int:
        """
        iterate over the list element.
        Sum them taking into account of relative "weight" of each number.
        """
        curr = l
        weight = 0
        num = 0
        while curr:
            num += curr.val * (10**weight)
            weight += 1
            curr = curr.next
        return num

    def from_int(self, num: int) -> ListNode:
        text = str(num)

        node = None
        for i in range(len(text)):
            node = ListNode(int(text[i]), node)

        return node
