from collections import deque
import heapq

# ------------------
# Queue ------------
# ------------------

"""
A FIFO (First In First Out) collection.
All can be implemented efficiently using a deque from collections.
"""
queue = deque[int]()

queue.append(1)     # enqueue
queue.popleft()     # dequeue


# ------------------
# Stack ------------
# ------------------

"""
A LIFO (Last In First Out) collection.
All can be implemented efficiently with a simple list.
"""

stack = []

stack.append(1)     # push
stack.pop()         # pop



# ------------------
# MIN / MAX Heap ---
# ------------------

"""
A Priority Based collection.
Heapq has built-in min and max heap support. 
All ops preserve their respective heap properties.
"""

min_heap = []
heapq.heappush(min_heap, 1)     # push
heapq.heappop(min_heap)         # pop

max_heap = []
heapq.heappush_max(max_heap, 1) # push
heapq.heappop_max(max_heap)     # pop
