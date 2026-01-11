from solution import Solution

class TestExerciseName:
    def test_testcase1(self):
        assert Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"

    def test_testcase2(self):
        assert Solution().convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"

    def test_testcase3(self):
        assert Solution().convert("A", 1) == "A"
 