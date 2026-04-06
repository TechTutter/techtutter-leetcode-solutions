from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for u, v in prerequisites:
            graph[v].append(u)
            in_degree[u] += 1
        
        queue = deque([x for x in range(numCourses) if in_degree[x] == 0])
        order = []
        while queue:
            curr = queue.popleft()
            order.append(curr)

            for nei in graph[curr]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)

        return order if len(order) == numCourses else []
        