import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        # build the initial min heap of size k
        # top most element will the kth largest in nums

        self.k = k
        self.heap = []

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:

        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            if val > self.heap[0]:
                heapq.heapreplace(self.heap, val)
        
        return self.heap[0]

        
