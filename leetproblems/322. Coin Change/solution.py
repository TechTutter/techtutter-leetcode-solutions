from math import inf

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0

        state = [0] + [inf] * amount
        for x in range(1, amount + 1):
            for c in coins:
                if c <= x:
                    state[x] = min(1 + state[x - c], state[x])
                    
        return -1 if state[-1] == inf else state[-1]


        