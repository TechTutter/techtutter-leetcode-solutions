from solution import Solution

class TestMajorityElement:
    def test_testcase1(self):
        assert Solution().majorityElement([3,2,3]) == 3

    def test_testcase2(self):
        assert Solution().majorityElement([2,2,1,1,1,2,2]) == 2