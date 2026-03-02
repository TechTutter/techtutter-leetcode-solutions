class Solution:
    def reverseBits(self, n: int) -> int:
        bits = str(bin(n)[2:])
        n = len(bits)
        m = 32 - n

        res = []
        for _ in range(m):
            res.append('0')
        res.extend(list(bits))

        for i in range(16):
            res[i], res[-1-i] = res[-1 -i], res[i]

        return int(''.join(res), 2)
         