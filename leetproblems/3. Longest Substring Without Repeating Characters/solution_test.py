from solution import Solution

class TestLongestSubstring:
    def test_testcase1(self):
        assert Solution().lengthOfLongestSubstring("abcabcbb") == 3

    def test_testcase2(self):
        assert Solution().lengthOfLongestSubstring("bbbbb") == 1

    def test_testcase3(self):
        assert Solution().lengthOfLongestSubstring("pwwkew") == 3
