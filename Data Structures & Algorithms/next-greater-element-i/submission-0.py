class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        mapping = dict()
        result = list()

        for idx, num in enumerate(nums2):
            mapping[num] = idx
        
        for num in nums1:
            
            starting_idx_nums2 = mapping[num]

            found = False

            for j in nums2[starting_idx_nums2:]:

                if j > num:
                    found = True
                    result.append(j)
                    break
            
            if not found:
                result.append(-1)
        
        return result