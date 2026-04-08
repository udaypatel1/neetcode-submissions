class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        ptr = 0

        nums_len = len(nums)

        while ptr < nums_len:

            if nums[ptr] == val:

                # delete in place
                nums.pop(ptr)

                # decrement length
                nums_len -= 1

                # we don't update ptr here, since deletion will shift array over

            else:
                ptr += 1

        return nums_len
        