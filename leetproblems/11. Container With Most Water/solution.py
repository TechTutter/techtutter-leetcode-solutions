class Solution:
    """
    Move only index of shorter height until they meet
    """
    def maxArea(self, height: list[int]) -> int:
        i, j = 0, len(height) - 1
        max_area = 0

        while i < j:
            h = min(height[i], height[j])
            max_area = max(max_area, h * (j - i))

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area