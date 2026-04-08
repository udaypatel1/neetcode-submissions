import math
import heapq

class Solution:

    def calculate_distance_to_origin(self, point: List[int]) -> float:

        x1, y1 = point

        return math.sqrt((x1 ** 2) + (y1 ** 2))


    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []

        for point in points:

            dist = self.calculate_distance_to_origin(point)

            heapq.heappush(heap, (dist, point))

        result = []

        for _ in range(k):

            dist, point = heapq.heappop(heap)

            result.append(point)

        return result


        