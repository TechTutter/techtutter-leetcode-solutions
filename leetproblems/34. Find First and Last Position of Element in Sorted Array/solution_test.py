from solution import Solution


class TestFindFirstAndLastPositionOfElementInSortedArray:
    def test_testcase1(self):
        nums = [5,7,7,8,8,10]
        target = 8
        assert Solution().searchRange(nums, target) == [3,4]

    def test_testcase2(self):
        nums = [5,7,7,8,8,10]
        target = 6
        assert Solution().searchRange(nums, target) == [-1,-1]

    def test_testcase3(self):
        nums = []
        target = 0
        assert Solution().searchRange(nums, target) == [-1,-1]

