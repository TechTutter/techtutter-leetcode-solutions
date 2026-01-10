"""
DFS uses LIFO queue, meaning a stack would be ideal in the implementation.
Since python lists implement pop and append in O(1), no changes are needed except for naming conventions.
To keep it simpler to remember togheter with BFS implementation, the name "queue" was unchanged.
"""
def dfs(graph, initial_node, node_callback):
    if initial_node not in graph:
        raise KeyError("Initial Node does not Exist in the Graph")

    queue = list(graph.get(initial_node))
    visited = {initial_node}
    node_callback(initial_node)

    while queue:
        next_elem = queue.pop()
        # Process next node on the list, if not already visited
        if next_elem not in visited:
            visited.add(next_elem)
            node_callback(next_elem)

            # Add all unvisited nodes to the processing queue
            unvisited = [x for x in graph.get(next_elem, []) if x not in visited]
            queue.extend(unvisited)
