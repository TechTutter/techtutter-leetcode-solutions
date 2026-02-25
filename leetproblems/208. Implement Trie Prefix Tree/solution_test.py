from solution import Trie, TrieNode

class TestExerciseName:
    def test_testcase1(self):
        trie = Trie()
        trie.insert("apple")
        assert trie.search("apple") is True
        assert trie.search("app") is False
        assert trie.startsWith("app") is True
        trie.insert("app")
        assert trie.search("app") is True

