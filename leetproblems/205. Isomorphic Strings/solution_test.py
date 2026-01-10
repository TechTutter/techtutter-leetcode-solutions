from solution import Solution

class TestIsomorphicStrings:
    def test_testcase1(self):
        assert Solution().isIsomorphic("egg", "add") == True

    def test_testcase2(self):
        assert Solution().isIsomorphic("foo", "bar") == False

    def test_testcase3(self):
        assert Solution().isIsomorphic("paper", "title") == True