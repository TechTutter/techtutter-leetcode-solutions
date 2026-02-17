class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        transform the list in a set. It is not sorted, but does not matter.
        This is because 
        """
        num_set = set(nums)
        longest = 0

        for x in num_set:
            # start of a sequence
            if x - 1 not in num_set:
                length = 1
                curr = x

                while curr + 1 in num_set:
                    curr += 1
                    length += 1

                longest = max(longest, length)

        return longest