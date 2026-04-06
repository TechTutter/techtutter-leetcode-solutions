from solution import Solution


class TestCourseScheduleII:
    def test_testcase1(self):
        numCourses = 2
        prerequisites = [[1,0]]
        assert Solution().findOrder(numCourses, prerequisites) == [0,1]

    def test_testcase2(self):
        numCourses = 4
        prerequisites = [[1,0],[2,0],[3,1],[3,2]]
        assert Solution().findOrder(numCourses, prerequisites) == [0,1,2,3] or [0,2,1,3]

    def test_testcase3(self):
        numCourses = 1
        prerequisites = []
        assert Solution().findOrder(numCourses, prerequisites) == [0]