from DFS import dfs
from BFS import bfs, bfs_shortest_path

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [8, 9],
    5: [9],
}

bfs(graph, 1, print)
dfs(graph, 1, print)
print(bfs_shortest_path(graph, 1, 99))