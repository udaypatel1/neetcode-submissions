class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        return [item[0] for item in collections.Counter(nums).most_common(k)]