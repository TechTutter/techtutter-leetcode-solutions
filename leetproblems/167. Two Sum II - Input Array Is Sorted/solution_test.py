from solution import Solution


class TestTwoSumII:
    def test_testcase1(self):
        assert Solution().twoSum([2,7,11,15], 9) == [1,2]
    
    def test_testcase2(self):
        assert Solution().twoSum([2,3,4], 6) == [1,3]
    
    def test_testcase3(self):
        assert Solution().twoSum([-1,0], -1) == [1,2]

