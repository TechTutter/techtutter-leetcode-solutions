from solution import Solution

class TestStrStr:
    def test_testcase1(self):
        assert Solution().strStr("sadbutsad", "sad") == 0

    def test_testcase2(self):
        assert Solution().strStr("leetcode", "leeto") == -1
