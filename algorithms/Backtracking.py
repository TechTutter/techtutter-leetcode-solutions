"""
Choose → Explore → Undo

There are two mental models for backtracking:

1. Choice loop model
2. Binary decision tree (include / exclude)
"""

def find_subsets(nums):
    """
    Example (choice loop model): find all subsets of [1,2]

    []
     ├─ choose 1 → [1]
     │   └─ choose 2 → [1,2]  ← record
     │   undo 2
     │
     undo 1
     │
     └─ choose 2 → [2]
    """
    result = []
    path = []

    def backtrack(start_index):
        result.append(list(path))

        for i in range(start_index, len(nums)):
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

    backtrack(0)
    return result
    
