from solution import Solution

class TestIntegerToRoman:
    def test_testcase1(self):
        assert Solution().intToRoman(3749) == "MMMDCCXLIX"

    def test_testcase2(self):
        assert Solution().intToRoman(58) == "LVIII"

    def test_testcase3(self):
        assert Solution().intToRoman(1994) == "MCMXCIV"
