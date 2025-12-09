from solution import Solution

def test_majorityElement():
    nums = [3,2,3]
    expected = 3
    result = Solution().majorityElement(nums)
    assert result == expected


def test_testcase2():
    nums = [2, 2, 1, 1, 1, 2, 2]
    expected = 2
    assert Solution().majorityElement(nums) == expected