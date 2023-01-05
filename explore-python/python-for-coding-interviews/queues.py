# Queues are double ended in python
from collections import deque

queue = deque()
# Adding values to the right side is as easy as appending them
queue.append(1)
queue.append(2)
print(queue)
# We can pop from the left of the queue in O(1)
queue.popleft()
print(queue)

# Since it is double ended we can also add values to the left side of the queue
queue.appendleft(1)
print(queue)
# Since it is double ended we can also pop values from the right side of the queue
queue.pop()
print(queue)
