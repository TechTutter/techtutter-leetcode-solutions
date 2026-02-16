# LinkedLists

The CORE operations include: reverse, start from n-th, search, delete, insert or sort.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

## Two Pointers (Fast and Slow)

```python
def findMiddle(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def detectCycle(head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    if slow == fast:
        return True

    return False

def twoPointersGap(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    To get n-th from end, use two pointers and move the first pointer n steps forward
    e.g. to remove n-th from end
    """
    for _ in range(n + 1):
        first = first.next

    while first:
        first = first.next
        second = second.next

    return second
```


## Dummy Node
Useful to avoid edge cases, e.g. when deleting the head node.

```python
def removeTarget(head: Optional[ListNode], target: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    prev = dummy
    curr = head

    while curr:
        if curr.val == target:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next

    return dummy.next
```

## Reversing

```python
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    set current.next as previous and move forward
    """
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
```

## Cute Trick
```python
def isPalindromeList(head: Optional[ListNode]) -> bool:
    """
    find middle
    reverse second half
    compare first and second half
    (optional: reverse second half back to restore original list)
    """
    pass
    