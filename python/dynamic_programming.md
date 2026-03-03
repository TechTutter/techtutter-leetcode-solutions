# Dynamic Programming

## Practical Guide
1. Define the state (e.g. dp[i] = max value ending at index i)
2. Define the base cases (e.g. -inf, 0, 1)
3. Define the transition between states (e.g. dp[i] = dp[i-1] + dp[i-2])
4. Define the final answer (e.g. max, min, sum, count, etc.)

About the state:
Can be built in two primary ways:
- Top-down (generally a recursive algorithm with memoization)
- Bottom-up (iterative, classic for loop with memoization)

About base Case: 
- If boolean, generally operation is OR.
- If integer, generally operation is min/max/sum.

## Complexity
- if dp[i] depends on all previous states, it is usually O(n^2) time and O(n) space (Fibonacci, Climbing Stairs, House Robber)
- if dp[i] depends only on a few previous steps, usually it's O(n) space -> can be often optimized to O(1) space if dp[i] depends only on last k states (Longest Increasing Subsequence, Coin Change, Word Break)

## Bottom-Up DP

Build the state iteratively. Generally it's a plane array or dict.

```python
def fibo_bottom_up(n):
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

## Top-Down DP

Build the state recursively with memoization.

```python
def fibo_top_down(n):
    memo = {}
    
    def fib(k):
        if k in memo:
            return memo[k]
        if k <= 1:
            return k
        
        memo[k] = fib(k-1) + fib(k-2)
        return memo[k]
    
    return fib(n)
```
