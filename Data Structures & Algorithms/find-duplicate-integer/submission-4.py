class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for idx, num in enumerate(nums):
            
            # get the idx of the abs(num) - 1, and negate it (marked as seen)

            if nums[abs(nums[idx]) - 1] < 0:
                return num if num > 0 else -num
            else:
                # mark it as seen
                nums[abs(nums[idx]) - 1] *= -1





        