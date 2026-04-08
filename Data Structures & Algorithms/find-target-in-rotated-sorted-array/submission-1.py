class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1


        while l <= r:

            mid = (l + r) // 2

            cur = nums[mid]
            l_val = nums[l]
            r_val = nums[r]

            if cur == target:
                return mid
            
            # check which side is sorted

            if l_val <= cur:
                
                if l_val <= target <= cur:
                    r = mid - 1                
                else:
                    l = mid + 1
                    
            elif cur < target <= r_val:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1
                
            


        