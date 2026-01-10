class Solution:
    """
    total_gas = 0
    total_cost = 0
    current_tank = 0
    start_index = 0
    
    for i from 0 to n-1:
        total_gas += gas[i]
        total_cost += cost[i]
        current_tank += gas[i] - cost[i]
        
        if current_tank < 0:
            current_tank = 0
            start_index = i + 1
            
    if total_gas < total_cost:
        return -1
    return start_index
    """
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        cumulative_gas = 0
        cumulative_cost = 0
        
        partial_gas = 0
        partial_cost = 0
        
        size = len(gas)
        idx = 0
        
        for i in range(size):
            cumulative_gas += gas[i]
            cumulative_cost += cost[i]
            
            partial_gas += gas[i]
            partial_cost += cost[i]
            
            if partial_gas < partial_cost:
                idx = i + 1
                print(idx)
                partial_gas = 0
                partial_cost = 0
            
        if(cumulative_cost > cumulative_gas or idx > size):
            return - 1
        
        return idx