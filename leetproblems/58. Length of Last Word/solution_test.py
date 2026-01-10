from solution import Solution

class TestLengthOfLastWord:
    def test_testcase1(self):
        assert Solution().lengthOfLastWord("Hello World") == 5

    def test_testcase2(self):
        assert Solution().lengthOfLastWord("   fly me   to   the moon  ") == 4

    def test_testcase3(self):
        assert Solution().lengthOfLastWord("luffy is still joyboy") == 6
