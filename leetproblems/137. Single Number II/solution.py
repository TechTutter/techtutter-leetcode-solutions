class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for i in range(32):
            bit_sum = 0
            for n in nums:
                bit_sum += (n >> i) & 1

            if bit_sum % 3:
                result |= (1 << i)

        if result >= 2**31:
            result -= 2**32

        return result