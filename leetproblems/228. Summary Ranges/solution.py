class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        n = len(nums)
        if n == 0: return []
        if n == 1: return [str(nums[0])]

        start = end = nums[0]
        res = []

        for i in range(1, n): 
            if nums[i] - end != 1:
                self.push_range(start, end, res)
                start = end = nums[i]
            else:
                end = nums[i]

        self.push_range(start, end, res)
        start = end = nums[i]

        return res
                
    def push_range(self, start, end, res):
        if end != start:
            res.append(f"{start}->{end}")
        else:
            res.append(f"{start}")