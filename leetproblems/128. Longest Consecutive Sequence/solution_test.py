from solution import Solution


class TestExerciseName:
    def test_testcase1(self):
        s = Solution()
        nums = [100,4,200,1,3,2]
        assert s.longestConsecutive(nums) == 4

    def test_testcase2(self):
        s = Solution()
        nums = [0,3,7,2,5,8,4,6,0,1]
        assert s.longestConsecutive(nums) == 9

    def test_testcase3(self):
        s = Solution()
        nums = [1,0,1,2]
        assert s.longestConsecutive(nums) == 3
