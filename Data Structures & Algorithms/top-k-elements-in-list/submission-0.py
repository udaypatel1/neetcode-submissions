# fool around with Heap, then do bucket sort

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # get freq map
        freq = Counter(nums)

        n = len(nums)

        bucket = [[] for _ in range(n + 1)]

        for key, frequency in freq.items():
            bucket[frequency].append(key)

        result = []

        while n > -1 and k > 0:

            if bucket[n]:
                result.append(bucket[n].pop())
                k -= 1
            else:
                n -= 1
        
        return result
            

                






        