from solution import Solution

class TestRemoveDuplicates:
    def test_testcase1(self):
        nums = [1,1,2]
        k = Solution().removeDuplicates(nums)
        assert k == 2
        assert nums[:k] == [1,2]

    def test_testcase2(self):
        nums = [0,0,1,1,1,2,2,3,3,4]
        k = Solution().removeDuplicates(nums)
        assert k == 5
        assert nums[:k] == [0,1,2,3,4]
