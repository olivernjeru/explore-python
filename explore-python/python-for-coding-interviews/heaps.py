# Used to find the min and max of a set of values frequently
import heapq

# under the hood are arrays
minHeap = []
# To push to a heap, we do as below
heapq.heappush(minHeap, 3)
# By default heaps in python are min heap
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)
#Minimum value is always at index 0
print(minHeap[0])

# To loop through a heap while the length of the heap is non zero
while len(minHeap):
    print(heapq.heappop(minHeap))


# No max heap by default but the work around is to use minHeap and multiply it by -1 when we push & pop that value
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)
# Max is always at index 0
print(-1 * maxHeap[0])
# By popping each value and multiplying it by negative 1, we can confirm that the values are printed from greatest to smallest
while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))

# Build heap from initial set of values
arr = [2, 1, 8, 4, 5]
# We can do it in O(n), linear time
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))