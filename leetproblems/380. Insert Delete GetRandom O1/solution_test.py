from solution import RandomizedSet


class TestRandomizedSet:
    def test_testcase1(self):
        randomized_set = RandomizedSet()
        assert randomized_set.insert(1) is True
        assert randomized_set.remove(2) is False
        assert randomized_set.insert(2) is True
        assert randomized_set.getRandom() in [1, 2]
        assert randomized_set.remove(1) is True
        assert randomized_set.insert(2) is False
        assert randomized_set.getRandom() == 2


