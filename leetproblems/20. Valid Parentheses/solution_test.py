from solution import Solution

class TestValidParentheses:
    def test_testcase1(self):
        assert Solution().isValid("()") == True

    def test_testcase2(self):
        assert Solution().isValid("()[]{}") == True

    def test_testcase3(self):
        assert Solution().isValid("(]") == False

    def test_testcase4(self):
        assert Solution().isValid("([])") == True

    def test_testcase5(self):
        assert Solution().isValid("([)]") == False
