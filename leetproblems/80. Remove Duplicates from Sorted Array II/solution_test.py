from solution import Solution

class TestRemoveDuplicatesII:
    def test_testcase1(self):
        nums = [1,1,1,2,2,3]
        k = Solution().removeDuplicates(nums)
        assert k == 5
        assert nums[:k] == [1,1,2,2,3]

    def test_testcase2(self):
        nums = [0,0,1,1,1,1,2,3,3]
        k = Solution().removeDuplicates(nums)
        assert k == 7
        assert nums[:k] == [0,0,1,1,2,3,3]
