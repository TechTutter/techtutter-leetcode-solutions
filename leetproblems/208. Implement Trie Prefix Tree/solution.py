class TrieNode:
    def __init__(self):
        self.characters = [None] * 26
        self.is_end_word = 0

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            index = ord(c.lower()) - ord('a')
            if curr.characters[index] is None:
                curr.characters[index] = TrieNode()
            curr = curr.characters[index]
        curr.is_end_word += 1

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            index = ord(c.lower()) - ord('a')
            if curr.characters[index] is None:
                return False
            curr = curr.characters[index]
        if curr is not None and curr.is_end_word > 0:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            index = ord(c.lower()) - ord('a')
            if curr.characters[index] is None:
                return False
            curr = curr.characters[index]
        return True   