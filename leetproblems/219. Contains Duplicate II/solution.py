class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        store a map of value -> index position
        if i-th value is in te map, check if i - map[nums[i]] <= k
        if it is return True
        else update map to point to latest index for nums[i]  
        """
        val_to_idx = {}
        for i, x in enumerate(nums):
            if x in val_to_idx:
                if i - val_to_idx[x] <= k:
                    return True
            val_to_idx[x] = i
        
        return False
                      

        