from solution import Solution

class TestLongestCommonPrefix:
    def test_testcase1(self):
        assert Solution().longestCommonPrefix(["flower","flow","flight"]) == "fl"

    def test_testcase2(self):
        assert Solution().longestCommonPrefix(["dog","racecar","car"]) == ""
