from solution import Solution

def test_isIsomorphic():
    s = "egg"
    t = "add"
    expected = True
    result = Solution().isIsomorphic(s, t)
    assert result == expected

    s = "foo"
    t = "bar"
    expected = False
    result = Solution().isIsomorphic(s, t)
    assert result == expected