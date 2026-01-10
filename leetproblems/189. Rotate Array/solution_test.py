from solution import Solution

class TestRotateArray:
    def test_testcase1(self):
        nums = [1,2,3,4,5,6,7]
        Solution().rotate(nums, 3)
        assert nums == [5,6,7,1,2,3,4]

    def test_testcase2(self):
        nums = [-1,-100,3,99]
        Solution().rotate(nums, 2)
        assert nums == [3,99,-1,-100]
