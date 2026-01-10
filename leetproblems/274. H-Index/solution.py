class Solution:
    """
    citations.sort()
    n = len(citations)
    for i from 0 to n-1:
        potential_h = n - i
        if citations[i] >= potential_h:
            return potential_h
    return 0
    """
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        citations.sort()
        
        for i in range(n):
            curr_h_index = n - i
            if citations[i] >= curr_h_index:
                return curr_h_index
        
        return 0