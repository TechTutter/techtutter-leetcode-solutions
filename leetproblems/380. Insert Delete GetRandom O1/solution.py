from random import randint

class RandomizedSet:
    """
    list with all values
    map with index -> value

    insert(val) -> if not exist push, update map
    delete(val) -> if exist on map, swap it with last and pop, update map
    getRandom() -> randInt(len(values))

    """

    def __init__(self):
        self.size = 0
        self.values = []
        self.val_to_index = {}

    def exists(self, val: int) -> bool:
        """
            check for val existence in the list
        """
        return val in self.val_to_index

    def insert(self, val: int) -> bool:
        """
           append the value to the list if it doesn't exist, then update the indexes map
        """
        exists = self.exists(val)
        if not exists:
            self.values.append(val)
            self.val_to_index[val] = self.size
            self.size += 1
        return not exists

    def remove(self, val: int) -> bool:
        """
            removes the val from the list if it exists, then update the map
        """
        exists = self.exists(val)
        if exists:
            idx = self.val_to_index.get(val)
            self._swap(idx, self.size - 1)
            self.values.pop()
            del self.val_to_index[val]
            self.size -= 1
        return exists

    def getRandom(self) -> int:
        i = randint(0, self.size - 1)
        return self.values[i]

    def _swap(self, i, j):
        a = self.values[i]
        b = self.values[j]

        self.val_to_index[b] = self.val_to_index[a]

        self.values[i] = b
        self.values[j] = a
