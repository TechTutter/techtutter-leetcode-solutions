class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        find max -> compare lo and hi. If lo > hi: hi = mid else lo = hi.
            k rotations -> max_idx + 1 % len(nums)

        now you have 2 sorted arrays. One before K, and one from K onward
            search on first subarray, then if not found on second one
        '''

        n = len(nums)
        if n == 0: return -1

        rotations = self.find_rotations(nums)
        print(rotations)
        
        left_search = self.binary_search(nums, target, 0, rotations)
        if left_search >= 0: return left_search

        right_search = self.binary_search(nums, target, rotations, n)
        return right_search

    def find_rotations(self, nums: list[int]):
        n = len(nums)
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid >= n-1 or nums[mid + 1] < nums[mid]:
                return (mid + 1) % n 
            else:
                if nums[lo] > nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
        return (hi + 1) % n

    def binary_search(self, nums: list[int], target:int, start: int, end: int) -> int:
        lo, hi = start, end - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1