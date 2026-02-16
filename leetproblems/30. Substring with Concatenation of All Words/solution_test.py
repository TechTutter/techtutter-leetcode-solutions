from solution import Solution


class TestExerciseName:
    def test_testcase1(self):
        assert Solution().findSubstring("barfoothefoobarman", ["foo","bar"]) == [0,9]

    def test_testcase2(self):
        assert Solution().findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]) == []

    def test_testcase3(self):
        assert Solution().findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]) == [6,9,12]
