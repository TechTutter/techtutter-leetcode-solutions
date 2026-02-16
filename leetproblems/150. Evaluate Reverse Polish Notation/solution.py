class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = set(['+', '-', '*', '/'])
        numbers = []
        latest_num = int(tokens[0])

        for i in range (1, len(tokens)):
            next_char = tokens[i]
            if next_char in operations: 
                b = numbers.pop()
                if next_char == "+":
                    latest_num = b + latest_num
                elif next_char == "-":
                    latest_num = b - latest_num
                elif next_char == "*":
                    latest_num = b * latest_num
                else:
                    latest_num = int(b / latest_num)
            else:
                numbers.append(latest_num)
                latest_num = int(next_char)

        return latest_num
