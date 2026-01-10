from solution import Solution

class TestRomanToInteger:
    def test_testcase1(self):
        assert Solution().romanToInt("III") == 3

    def test_testcase2(self):
        assert Solution().romanToInt("LVIII") == 58

    def test_testcase3(self):
        assert Solution().romanToInt("MCMXCIV") == 1994
