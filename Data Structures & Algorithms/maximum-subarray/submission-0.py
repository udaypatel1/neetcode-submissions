class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        '''
        kadanes algo

        2 choices:
            - should we extend the current subarray?
            - should we start a new subarray and kill the running one?
        '''

        if len(nums) == 1:
            return nums[0]

        cur_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)
        
        return max_sum

