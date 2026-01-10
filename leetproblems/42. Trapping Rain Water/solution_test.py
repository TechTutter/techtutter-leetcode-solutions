from solution import Solution

class TestTrappingRainWater:
    def test_testcase1(self):
        assert Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6

    def test_testcase2(self):
        assert Solution().trap([4,2,0,3,2,5]) == 9
