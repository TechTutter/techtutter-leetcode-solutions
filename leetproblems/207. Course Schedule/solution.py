from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for u, v in prerequisites:
            graph[v].append(u)
            in_degree[u] += 1

        queue: deque[int] = deque([x for x in range(numCourses) if in_degree[x] == 0])
        scheduled: int = 0
        while queue:
            curr = queue.popleft()
            scheduled += 1
            for nei in graph[curr]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)
        
        return numCourses == scheduled

        