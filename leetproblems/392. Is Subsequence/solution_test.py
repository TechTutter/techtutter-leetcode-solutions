from solution import Solution

class TestIsSubsequence:
    def test_testcase1(self):
        assert Solution().isSubsequence("abc", "ahbgdc") == True

    def test_testcase2(self):
        assert Solution().isSubsequence("axc", "ahbgdc") == False
