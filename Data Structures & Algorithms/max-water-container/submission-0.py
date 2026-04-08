class Solution:

    def calculate_area(self, left_idx, right_idx, heights):

        '''
        left_height = heights[left_idx]
        right_height = heights[right_idx]

        bottom = right_idx - left_idx
        height_to_be_used = min(left_height, right_height)

        area = bottom * height_to_be_used
        return area
        '''

        return (right_idx - left_idx) * min(heights[left_idx], heights[right_idx])

    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1
        max_area = float('-inf')

        while l < r:

            cur_area = self.calculate_area(l, r, heights)

            max_area = max(max_area, cur_area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area




        