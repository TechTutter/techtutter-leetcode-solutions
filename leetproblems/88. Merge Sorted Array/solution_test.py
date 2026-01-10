from solution import Solution

class TestMergeSortedArray:
    def test_testcase1(self):
        nums1 = [1,2,3,0,0,0]
        Solution().merge(nums1, 3, [2,5,6], 3)
        assert nums1 == [1,2,2,3,5,6]

    def test_testcase2(self):
        nums1 = [1]
        Solution().merge(nums1, 1, [], 0)
        assert nums1 == [1]

    def test_testcase3(self):
        nums1 = [0]
        Solution().merge(nums1, 0, [1], 1)
        assert nums1 == [1]