from solution import Solution


class TestExerciseName:
    def test_testcase1(self):
        assert Solution().minWindow("ADOBECODEBANC", "ABC") == "BANC"

    def test_testcase2(self):
        assert Solution().minWindow("a", "a") == "a"

    def test_testcase3(self):
        assert Solution().minWindow("a", "aa") == ""

