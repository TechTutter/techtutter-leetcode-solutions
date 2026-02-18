# Trees
Generic trees per se are not particularly useful. In problem solving, we generally deal with Binary Trees or Binary Search Trees.

Operations like search, insertion, and deletion work in O(Log n) time for a balanced binary search tree. In the worst-case (unbalanced), these degrade to O(n). With self-balancing BSTs like AVL and Red Black Trees, we can ensure the worst case as O(Log n).

## Recursion and Early Returns

> IMPORTANT: When doing a boolean check, an OR logic allows for the full exploration (because the exploration will continue until everything is False, it needs to explore all nodes before stopping), while also allowing for early returns, because as soon as a True is found, the boolean short cirtuits

```python
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        # Se è una foglia
        if not root.left and not root.right:
            return root.val == targetSum
        
        return (
            self.hasPathSum(root.left, targetSum - root.val) or
            self.hasPathSum(root.right, targetSum - root.val)
        )
```

## Traversal

### Depth Traversal

There are 3 ways to traverse a tree in depth: Preorder, Inorder and Postorder. All 3 represent a variation of a DFS, changing only the order in which we process the current node.

<table>
<thead>
<tr>
<th>Preorder</th>
<th>Inorder</th>
<th>Postorder</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center"><b>Root</b> &rarr; Left &rarr; Right</td>
<td align="center">Left &rarr; <b>Root</b> &rarr; Right</td>
<td align="center">Left &rarr; Right &rarr; <b>Root</b></td>
</tr>
<tr>
<td>
<pre>
def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)
</pre>
</td>
<td>
<pre>
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)
</pre>
</td>
<td>
<pre>
def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)
</pre>
</td>
</tr>
</tbody>
</table>

```python
def dfs(node):
    if not node:
        return BASE_VALUE # e.g. 0

    left = dfs(node.left)
    right = dfs(node.right)

    return combine(node, left, right) # e.g 1 + left + right
```

### Width Traversal

```python
def bfs(node):
    if not node:
        return BASE_VALUE # e.g. 0

    queue = deque([node])
    while queue:
        node = queue.popleft()
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return combine(node, left, right) # e.g 1 + left + right
```

### BST Traversal

```python
def searchBST(root: Node | None, val) -> Node | None:
    if not root or root.val == val:
        return root
    
    if val < root.val:
        return searchBST(root.left, val)
    else:
        return searchBST(root.right, val)
```

## Measurements

### Height

```python
def height(node):
    if not node:
        return -1
    return 1 + max(height(node.left), height(node.right))
```

### Diameter (longest path between any two nodes)

```python
def diameterOfBinaryTree(root):
    diameter = 0

    def height(node):
        if not node: return 0

        nonlocal diameter

        l_height = height(node.left)
        r_height = height(node.right)
        diameter = max(diameter, l_height + r_height)

        return 1 + max(l_height, r_height)

    height(root)
    return diameter
```

## Revert Tree

```python
def invertTree(root):
    if not root:
        return None

    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root
```