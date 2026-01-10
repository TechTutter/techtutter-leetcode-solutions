from solution import Solution

class TestGasStation:
    def test_testcase1(self):
        assert Solution().canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]) == 3

    def test_testcase2(self):
        assert Solution().canCompleteCircuit([2,3,4], [3,4,3]) == -1
