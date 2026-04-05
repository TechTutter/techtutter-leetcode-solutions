from collections import deque

class Node:
    def __init__(self, val: int = 0, neighbors: list["Node"] | None = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Node | None) -> Node | None:
        if node is None:
            return None

        dummy = Node(node.val)
        cloned = { node.val: dummy }
        queue = deque([node])

        while queue:
            curr = queue.popleft()
            for n in curr.neighbors:
                val = n.val
                if val not in cloned:
                    clone = Node(val)
                    cloned[val] = clone

                    queue.append(n)
                cloned[curr.val].neighbors.append(cloned[val])
        return dummy
    
s = Solution()

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

clone = s.cloneGraph(n1)
print(clone.val if clone is not None else 0)