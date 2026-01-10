"""
DFS uses LIFO queue, meaning a deque from collections would be ideal in the implementation.
To keep it simpler to remember togheter with BFS implementation, the name "queue" was unchanged.
The perf difference is huge, a deque is strongly suggested as it would allow to popLeft in O(1) instead of O(n)
"""
def bfs(graph, initial_node, node_callback):
    if initial_node not in graph:
        raise KeyError("Initial Node does not Exist in the Graph")

    queue = list(graph.get(initial_node))
    visited = {initial_node}
    node_callback(initial_node)

    while queue:
        next_elem = queue.pop(0)
        # Process next node on the list, if not already visited
        if next_elem not in visited:
            visited.add(next_elem)
            node_callback(next_elem)

            # Add all unvisited nodes to the processing queue
            unvisited = [x for x in graph.get(next_elem, []) if x not in visited]
            queue.extend(unvisited)


"""
Same as BFS, but keep a "level_len" counter to know when to increase distance
Raise error if target was not found in the loop.
Once level_len is 0 we knowe we have explored all possible neighbours at this lvl.
"""
def bfs_shortest_path(graph, initial_node, target):
    if initial_node not in graph:
        raise KeyError(f"InitialNode {initial_node} not in graph")
    if initial_node == target:
        return 0

    queue = list(graph.get(initial_node))
    visited = {initial_node}
    distance = 0
    level_len = 0

    while queue:
        if level_len == 0:
            level_len = len(queue)
            distance += 1

        level_len -= 1
        next_elem = queue.pop(0)

        if next_elem == target:
            return distance

        # Process next node on the list, if not already visited
        if next_elem not in visited:
            visited.add(next_elem)

            # Add all unvisited nodes to the processing queue
            unvisited = [x for x in graph.get(next_elem, []) if x not in visited]
            queue.extend(unvisited)

    return -1
