from solution import WordDictionary


class TestExerciseName:
    def test_testcase1(self):
        wordDictionary = WordDictionary()
        wordDictionary.addWord("bad")
        wordDictionary.addWord("dad")
        wordDictionary.addWord("mad")
        assert wordDictionary.search("pad") is False
        assert wordDictionary.search("bad") is True
        assert wordDictionary.search(".ad") is True
        assert wordDictionary.search("b..") is True

    def test_testcase2(self):
        wordDictionary = WordDictionary()
        wordDictionary.addWord("a")
        assert wordDictionary.search(".") is True
        assert wordDictionary.search("a") is True
        assert wordDictionary.search("aa") is False
        assert wordDictionary.search("a") is True
        assert wordDictionary.search(".a") is False
        assert wordDictionary.search("a.") is False

