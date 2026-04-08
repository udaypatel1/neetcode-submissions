class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        target_row_idx = None

        for idx, row in enumerate(matrix):

            if row[0] <= target <= row[-1]:
                target_row_idx = idx
                break
        
        if target_row_idx == None:
            return False
        
        # now perform bsearch as usual on this target row for our target

        target_row = matrix[target_row_idx]

        l = 0
        r = len(target_row)

        while l < r:

            mid = (l + r) // 2

            if target_row[mid] == target:
                return True
            
            if target < target_row[mid]:
                r = mid
            else:
                l = mid + 1
        
        return False
