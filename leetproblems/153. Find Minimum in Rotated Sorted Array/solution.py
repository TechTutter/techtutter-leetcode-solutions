class Solution:
    def findMin(self, nums: list[int]) -> int:
        rotations = self.get_rotations(nums)
        return nums[rotations]

    def get_rotations(self, nums: list[int]) -> int:
        n = len(nums)
        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2

            if nums[mid] > nums[mid + 1] or mid == n - 1:
                return mid + 1 % n

            if nums[lo] > nums[mid + 1]:
                hi = mid
            else:
                lo = mid + 1
        return (hi + 1) % n
