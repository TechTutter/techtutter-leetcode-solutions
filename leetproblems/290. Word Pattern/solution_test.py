from solution import Solution

class TestWordPattern:
    def test_testcase1(self):
        assert Solution().wordPattern("abba", "dog cat cat dog") == True

    def test_testcase2(self):
        assert Solution().wordPattern("abba", "dog cat cat fish") == False

    def test_testcase3(self):
        assert Solution().wordPattern("aaaa", "dog cat cat dog") == False
