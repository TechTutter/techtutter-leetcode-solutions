from solution import Solution

class TestSolution:
    def test_testcase1(self):
        assert Solution().canConstruct("a", "b") is False

    def test_testcase2(self):
        assert Solution().canConstruct("aa", "ab") is False

    def test_testcase3(self):
        assert Solution().canConstruct("aa", "aab") is True

