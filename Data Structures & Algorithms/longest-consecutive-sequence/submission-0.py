class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        if len(nums) == 1:
            return 1

        s = set(nums)
        longest = -1

        for num in nums:
            
            if num - 1 not in s:
                # this is a starter
                cur_longest = 1
                cur = num
                while cur + 1 in s:
                    cur_longest += 1
                    cur = cur + 1
                
                longest = max(longest, cur_longest)
        
        return longest

                    

        