from solution import Solution


class TestExerciseName:
    def test_testcase1(self):
        assert Solution().calculate("1 + 1") == 2
    
    def test_testcase2(self):
        assert Solution().calculate(" 2-1 + 2 ") == 3
    
    def test_testcase3(self):
        assert Solution().calculate("(1+(4+5+2)-3)+(6+8)") == 23
        
    