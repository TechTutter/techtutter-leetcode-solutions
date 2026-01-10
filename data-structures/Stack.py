# A simple list can be used, it is O(1) for append / pop from end.
# A Stack implementation would just wrap the list built-in class.
class Stack:
    def __init__(self):
        self._data = []

    def push(self, val):
        self._data.append(val)

    def pop(self):
        return self._data.pop()

    def __str__(self) -> str:
        return str(self._data)

    def __len__(self) -> int:
        return len(self._data)
