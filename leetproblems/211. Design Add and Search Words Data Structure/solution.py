from collections import deque

class TrieNode:
    def __init__(self, c: str | None = None):
        self.characters = [None] * 26
        self.is_end_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            index = self.getIndexOfCharacter(c)
            if curr.characters[index] is None:
                curr.characters[index] = TrieNode(c)
            curr = curr.characters[index]
        curr.is_end_word = True

    def search(self, word: str) -> bool:
        queue = deque([self.root])

        for c in word:
            idx = self.getIndexOfCharacter(c)
            level = len(queue)
            for _ in range(level):
                curr = queue.popleft()
                # it's a specific character, append if found
                if idx >= 0: 
                    nxt = curr.characters[idx]
                    if nxt is not None: queue.append(nxt)
                # it's a dot, append all chindren
                else: 
                    for x in [x for x in curr.characters if x is not None]:
                        queue.append(x)
        
        return any([x for x in queue if x.is_end_word])

    def getIndexOfCharacter(self, c: str) -> int:
        if c == '.':
            return -1
        return ord(c.lower()) - ord('a')