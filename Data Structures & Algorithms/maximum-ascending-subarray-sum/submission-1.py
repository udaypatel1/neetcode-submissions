class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        curSum = nums[0]
        maxSum = curSum

        for idx in range(1, len(nums)):

            if nums[idx] > nums[idx - 1]:
                curSum += nums[idx]
                maxSum = max(maxSum, curSum)

            else:
                curSum = nums[idx]
            
        return maxSum
                


        