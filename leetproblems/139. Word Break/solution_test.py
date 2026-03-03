from solution import Solution


class TestWordBreak:
    def test_testcase1(self):
        assert Solution().wordBreak("leetcode", ["leet","code"]) is True
    
    def test_testcase2(self):
        assert Solution().wordBreak("applepenapple", ["apple","pen"]) is True
    
    def test_testcase3(self):
        assert Solution().wordBreak("catsandog", ["cats","dog","sand","and","cat"]) is False

