import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []

        for num in nums:

            if k > 0:
                heapq.heappush(heap, num)
                k -= 1
            else:

                node = heapq.heappop(heap)

                if node >= num:
                    heapq.heappush(heap, node)
                else:
                    heapq.heappush(heap, num)
        
        return heapq.heappop(heap)







        
        