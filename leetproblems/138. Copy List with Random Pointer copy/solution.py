from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head

        dummy = Node(0)
        id_to_node = {}
        
        curr = head
        curr_copy = dummy
        while curr:
            n = Node(curr.val)
            curr_copy.next = n

            id_to_node[id(curr)] = [curr, n]
            curr = curr.next
            curr_copy = curr_copy.next
        
        curr = head
        while curr:
            _, n_copy = id_to_node[id(curr)]

            if curr.random is not None:
                _, rand_copy = id_to_node[id(curr.random)]
                n_copy.random = rand_copy
            else:
                n_copy.random = None

            curr = curr.next
    
        return dummy.next