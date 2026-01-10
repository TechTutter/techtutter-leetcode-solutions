from solution import Solution

class TestThreeSum:
    def test_testcase1(self):
        # We sort results because the order of triplets doesn't matter, but for comparison it's easier
        # However, the code sorts the triplets themselves internally which helps.
        result = Solution().threeSum([-1,0,1,2,-1,-4])
        # Sort each inner list and then the outer list for deterministic comparison
        sorted_result = sorted([sorted(x) for x in result])
        expected = sorted([sorted([-1,-1,2]), sorted([-1,0,1])])
        assert sorted_result == expected

    def test_testcase2(self):
        assert Solution().threeSum([0,1,1]) == []

    def test_testcase3(self):
        assert Solution().threeSum([0,0,0]) == [[0,0,0]]
