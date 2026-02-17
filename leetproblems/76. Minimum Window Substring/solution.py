from collections import Counter
from math import inf

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = end = -1
        window = inf

        frequencies = Counter(t)
        n = len(frequencies)

        left = 0
        for right, c in enumerate(s):
            if c in frequencies:
                frequencies[c] -= 1
                if frequencies[c] == 0:
                    n -= 1
            # all c in t found, reduce window size until possible
            while n == 0:
                if window > right - left + 1:
                    window = right - left + 1
                    start = left
                    end = right

                if s[left] in frequencies:
                    frequencies[s[left]] += 1
                    if frequencies[s[left]] == 1:
                        n += 1
                left += 1
        
        return s[start:end+1] if start >= 0 else ""
        