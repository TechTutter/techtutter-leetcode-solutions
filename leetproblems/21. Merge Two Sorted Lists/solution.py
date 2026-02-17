class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        return self.val == other.val and self.next == other.next
        
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode | None:

        head = ListNode(0)
        tail = head

        l1, l2 = list1, list2

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # attach remaining nodes
        tail.next = l1 if l1 else l2

        return head.next
            
a = ListNode(5)
b = ListNode(3, a)
c = ListNode(1, b)
d = None

x = ListNode(5)
y = ListNode(3, a)
z = ListNode(0, None)

s = Solution()
res = s.mergeTwoLists(d, z)
print(res)
while res:
    print(res.val)
    res = res.next if res.next else None


            
                
                
        