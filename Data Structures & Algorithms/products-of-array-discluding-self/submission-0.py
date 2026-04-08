class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        '''

        example [1,2,4,6]

        left to right
        [1,1,2,8]

        right to left
        [48,24,6,1]

        [48,24,12,8]
        '''

        left_to_right = [1 for _ in range(len(nums))]
        right_to_left = [1 for _ in range(len(nums))]

        for idx in range(1, len(nums)):
            left_to_right[idx] = nums[idx - 1] * left_to_right[idx - 1]
        
        for idx in range(len(nums) - 2, -1, -1):
            right_to_left[idx] = nums[idx + 1] * right_to_left[idx + 1]
        
        result = []
        for idx in range(len(nums)):
            result.append(left_to_right[idx] * right_to_left[idx])

        return result


        

            
            



        