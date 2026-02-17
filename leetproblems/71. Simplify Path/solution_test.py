from solution import Solution


class TestSolution:
    def test_case1(self):
        assert Solution().simplifyPath("/home/") == "/home"

    def test_case2(self):
        assert Solution().simplifyPath("/home//foo/") == "/home/foo"

    def test_case3(self):
        assert Solution().simplifyPath("/home/user/Documents/../Pictures") == "/home/user/Pictures"

    def test_case4(self):
        assert Solution().simplifyPath("/../") == "/"

    def test_case5(self):
        assert Solution().simplifyPath("/.../a/../b/c/../d/./") == "/.../b/d"