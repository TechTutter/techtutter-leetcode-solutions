class Solution:
    """
    if not nums: return 0
    write_index = 1
    for i from 1 to len(nums)-1:
        if nums[i] != nums[i-1]:
            nums[write_index] = nums[i]
            write_index++
    return write_index
    """
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        write_index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[write_index] = nums[i]
                write_index += 1
                
        return write_index
