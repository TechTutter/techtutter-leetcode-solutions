from solution import Solution


class TestSingleNumberII:
    def test_testcase1(self):       
        assert Solution().singleNumber([2,2,3,2]) == 3

    def test_testcase2(self):       
        assert Solution().singleNumber([0,1,0,1,0,1,99]) == 99

    def test_testcase3(self):       
        assert Solution().singleNumber([1]) == 1

