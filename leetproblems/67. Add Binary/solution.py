class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_a = self.binaryStr_to_int(a)
        int_b = self.binaryStr_to_int(b)
        tot = int_a + int_b
        return f"{tot:b}"

    def binaryStr_to_int(self, val: str) -> int:
        w = len(val) - 1
        tot = 0
        for bit in val:
            tot += int(bit) * (2 ** w)
            w -= 1
        return tot

    
        