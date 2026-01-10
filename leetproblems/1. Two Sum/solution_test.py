from solution import Solution

class TestTwoSum:
    def test_testcase1(self):
        assert Solution().twoSum([2,7,11,15], 9) == [0,1]

    def test_testcase2(self):
        assert Solution().twoSum([3,2,4], 6) == [1,2]

    def test_testcase3(self):
        assert Solution().twoSum([3,3], 6) == [0,1]
