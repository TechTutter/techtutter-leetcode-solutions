from solution import Solution

class TestValidPalindrome:
    def test_testcase1(self):
        assert Solution().isPalindrome("A man, a plan, a canal: Panama") == True

    def test_testcase2(self):
        assert Solution().isPalindrome("race a car") == False

    def test_testcase3(self):
        assert Solution().isPalindrome(" ") == True
