from solution import Solution


class TestExerciseName:
    def test_testcase1(self):
        numCourses = 2
        prerequisites = [[1,0]]
        assert Solution().canFinish(numCourses, prerequisites)

    def test_testcase2(self):
        numCourses = 2
        prerequisites = [[1,0],[0,1]]
        assert not Solution().canFinish(numCourses, prerequisites)
