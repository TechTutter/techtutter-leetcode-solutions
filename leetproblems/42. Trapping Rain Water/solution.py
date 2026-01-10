class Solution:
    """
    Two-pointer approach (standard L5 optimized solution):
    left = 0, right = n - 1
    left_max = 0, right_max = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max: update left_max
            else: water += left_max - height[left]
            left++
        else:
            if height[right] >= right_max: update right_max
            else: water += right_max - height[right]
            right--
    """
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
            
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
                
        return water
