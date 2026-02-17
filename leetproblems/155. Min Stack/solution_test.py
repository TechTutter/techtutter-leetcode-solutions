from solution import MinStack


class TestExerciseName:
    def test_testcase1(self):
        minStack = MinStack()
        minStack.push(-2)
        minStack.push(0)
        minStack.push(-3)
        assert minStack.getMin() == -3
        minStack.pop()
        assert minStack.top() == 0
        assert minStack.getMin() == -2

