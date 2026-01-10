class Solution:
    """
    write_index = 0
    for i from 0 to len(nums)-1:
        if nums[i] != val:
            nums[write_index] = nums[i]
            write_index++
    return write_index
    """
    def removeElement(self, nums: list[int], val: int) -> int:
        write_index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[write_index] = nums[i]
                write_index += 1
        return write_index
