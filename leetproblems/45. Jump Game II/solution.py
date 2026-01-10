class Solution:
    """
    jumps = 0, current_jump_end = 0, farthest = 0
    for i from 0 to n - 2:
        farthest = max(farthest, i + nums[i])
        if i == current_jump_end:
            jumps++
            current_jump_end = farthest
    return jumps
    """
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
            
        jumps = 0
        current_jump_end = 0
        farthest = 0
        
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest
                
        return jumps
    