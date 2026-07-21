class Solution:
    def canJump(self, nums: List[int]) -> bool:

        memo = dict()

        def dp(idx):

            if idx >= len(nums) - 1:
                return True

            if idx in memo:
                return memo[idx]

            # if you're at a position that's not the end and you can't jump anymore
            if nums[idx] == 0:
                memo[idx] = False
                return False
            
            # given some idx, we can jump forward 0-(N+1) where N is nums[idx]


            for jump in range(nums[idx], 0, -1):

                if dp(idx + jump):
                    memo[idx] = True
                    return True
            
            memo[idx] = False
            return False
        
        return dp(0)



            


        