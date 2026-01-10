from solution import Solution

class TestValidAnagram:
    def test_testcase1(self):
        assert Solution().isAnagram("anagram", "nagaram") == True

    def test_testcase2(self):
        assert Solution().isAnagram("rat", "car") == False
