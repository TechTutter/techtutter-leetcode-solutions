from solution import Solution

class TestExerciseName:
    def test_testcase1(self):
        assert Solution().evalRPN(["2","1","+","3","*"]) == 9
    
    def test_testcase2(self):
        assert Solution().evalRPN(["4","13","5","/","+"]) == 6
    
    def test_testcase3(self):
        assert Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22
