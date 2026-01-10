class Solution:
    """
    candies = [1] * n
    # Left-to-right: ensure higher rating has more candies than left neighbor
    for i from 1 to n-1:
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1
            
    # Right-to-left: ensure higher rating has more candies than right neighbor
    for i from n-2 to 0:
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)
            
    return sum(candies)
    """
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        
        # left -> right
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        # right -> left
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
                
        return sum(candies)
