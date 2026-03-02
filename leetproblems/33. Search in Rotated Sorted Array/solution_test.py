from solution import Solution

class TestSearchInRotatedSortedArray:
    def test_testcase1(self):
        nums = [4,5,6,7,0,1,2]
        target = 0
        assert Solution().search(nums, target) == 4

    def test_testcase2(self):
        nums = [4,5,6,7,0,1,2]
        target = 3
        assert Solution().search(nums, target) == -1

    def test_testcase3(self):
        nums = [1]
        target = 0
        assert Solution().search(nums, target) == -1

