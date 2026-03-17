from collections import defaultdict
from math import gcd


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        if n < 2:
            return n

        result = 0

        for i in range(n):
            slopes = defaultdict(int)
            x1, y1 = points[i]
            local_max = 0

            for j in range(i + 1, n):
                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1

                if dx == 0:
                    slope = (1, 0)  # vertical
                elif dy == 0:
                    slope = (0, 1)  # horizontal
                else:
                    g = gcd(dy, dx)
                    dy //= g
                    dx //= g

                    # normalize sign
                    if dx < 0:
                        dx *= -1
                        dy *= -1

                    slope = (dy, dx)

                slopes[slope] += 1
                local_max = max(local_max, slopes[slope])

            # +1 to include the anchor point itself
            result = max(result, local_max + 1)

        return result
