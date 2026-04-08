import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            y = -heapq.heappop(heap)  # largest
            x = -heapq.heappop(heap)  # second largest

            if y != x:
                heapq.heappush(heap, -(y - x))
        
        return -heap[0] if heap else 0
        
        