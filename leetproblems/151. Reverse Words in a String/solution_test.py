from solution import Solution

class TestExerciseName:
    def test_testcase1(self):
        assert Solution().reverseWords("the sky is blue") == "blue is sky the"

    def test_testcase2(self):
        assert Solution().reverseWords("  hello world  ") == "world hello"

    def test_testcase3(self):
        assert Solution().reverseWords("a good   example") == "example good a"

