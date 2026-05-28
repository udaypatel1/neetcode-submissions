class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        c = collections.Counter(nums)

        m = (None, float('-inf'))

        for key, value in c.items():

            if value > len(nums) // 2 and value > m[1]:
                m = (key, value)
        
        return m[0]
        