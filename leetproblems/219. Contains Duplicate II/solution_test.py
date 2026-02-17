from solution import Solution

class TestExerciseName:
    def test_testcase1(self):
        s = Solution()
        nums = [1,2,3,1]
        k = 3
        assert s.containsNearbyDuplicate(nums, k) == True

    def test_testcase2(self):
        s = Solution()
        nums = [1,0,1,1]
        k = 1
        assert s.containsNearbyDuplicate(nums, k) == True

    def test_testcase3(self):
        s = Solution()
        nums = [1,2,3,1,2,3]
        k = 2
        assert s.containsNearbyDuplicate(nums, k) == False

