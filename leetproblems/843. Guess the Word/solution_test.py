from solution import Solution, Master


class TestExerciseName:
    def test_testcase1(self):
        master = Master("acckzz")
        Solution().findSecretWord(["acckzz","ccbazz","eiowzz","abcczz"], master)
        assert master.guessed


    def test_testcase2(self):
        master = Master("hamada")
        Solution().findSecretWord(["hamada","khaled"], master)
        assert master.guessed

