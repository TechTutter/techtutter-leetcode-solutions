from solution import Solution

class TestInterleavingString:
    def test_testcase1(self):
        assert Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac") is True

    def test_testcase2(self):
        assert Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc") is False

    def test_testcase3(self):
        assert Solution().isInterleave("", "", "") is True

