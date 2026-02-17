class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """
        two pointers i, j = 0, n
        the complementary to find is target - numbers[i]
        while i < j
        check numbers[j]
            if equal, return (i+1, j+1)
            if lower, increase i
            else decrease j  
        """
        i, j = 0, len(numbers) - 1

        while i < j:
            print(j)
            complementary = target - numbers[i]
            curr = numbers[j]

            if curr == complementary:
                return [i + 1, j + 1]
            elif curr < complementary:
                i += 1
            else:
                j -= 1