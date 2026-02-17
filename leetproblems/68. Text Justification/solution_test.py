from solution import Solution

class TestExerciseName:
    def test_testcase1(self):
        s = Solution()
        words = ["This","is","an","example","of","text","justification."]
        maxWidth = 16
        assert s.fullJustify(words, maxWidth) == ["This    is    an","example  of text","justification.  "]

    def test_testcase2(self):
        s = Solution()
        words = ["What","must","be","acknowledgment","shall","be"]
        maxWidth = 16
        assert s.fullJustify(words, maxWidth) == ["What   must   be","acknowledgment  ","shall be        "]

