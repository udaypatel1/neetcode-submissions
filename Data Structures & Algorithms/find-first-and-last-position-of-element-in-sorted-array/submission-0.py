class Solution:

    def _find_first(self, nums, target):

        l, r = 0, len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            if nums[mid] == target:
                # is there a target before it? but is before indexable?
                if mid == 0:
                    # we're at first index, return this
                    return 0
                
                # we have an elem behind it, check that its less than target
                if nums[mid - 1] < nums[mid]:
                    # found first!
                    return mid
                else:
                    # found target, but its not the first. search bottom half
                    r = mid - 1
            elif nums[mid] < target:
                # search up
                l = mid + 1
            else:
                # search down
                r = mid - 1
        
        return -1

    def _find_last(self, nums, target):

        l, r = 0, len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            if nums[mid] == target:
                # is there a target after it? but is after indexable?
                if mid == len(nums) - 1:
                    # we're at last index, return this
                    return mid
                
                # we have an elem after it, check that its greater than target
                if nums[mid + 1] > nums[mid]:
                    # found last!
                    return mid
                else:
                    # found target, but its not the last. search top half
                    l = mid + 1
            elif nums[mid] < target:
                # search up
                l = mid + 1
            else:
                # search down
                r = mid - 1
        
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        first_idx = self._find_first(nums, target)
        last_idx = self._find_last(nums, target)

        return [first_idx, last_idx]