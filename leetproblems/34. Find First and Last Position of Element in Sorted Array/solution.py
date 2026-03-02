class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        do binary search for leftmost, if found do the same for rightmost
        if target is found return res, else early return -1, -1
        '''
        n = len(nums)
        lo, hi = 0, n - 1
        res = [-1, -1]

        res[0] = self.binary_search(nums, target, 0, self.is_leftmost)
        if res[0] < 0: return res

        res[1] = self.binary_search(nums, target, n-1, self.is_rightmost)
        return res

    def binary_search(self, nums: list[int], target: int, boundary_target: int, is_boundary) -> int:
        res = -1
        n = len(nums)
        lo, hi = 0, n - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            curr = nums[mid]
            if curr == target:
                res = mid
                if is_boundary(nums, mid, boundary_target, curr): break
                else:
                    if boundary_target == 0:
                        hi = mid - 1
                    else:
                        lo = mid + 1
            elif curr < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return res

    def is_leftmost(self, nums: list[int], mid: int, boundary_target: int, curr: int):
        return mid == boundary_target or nums[mid - 1] < curr

    def is_rightmost(self, nums: list[int], mid: int, boundary_target: int, curr: int):
        return mid == boundary_target or nums[mid + 1] > curr