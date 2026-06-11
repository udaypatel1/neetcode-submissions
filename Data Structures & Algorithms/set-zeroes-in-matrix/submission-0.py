class Solution:

    def _update_cols(self, row, col, matrix, change_set):

        for cur_col in range(len(matrix[row])):

            change_set.add((row, cur_col))
        
    def _update_rows(self, row, col, matrix, change_set):

        for cur_row in range(len(matrix)):

            change_set.add((cur_row, col))
            
    def setZeroes(self, matrix: List[List[int]]) -> None:

        change_set = set()

        for row in range(len(matrix)):

            for col in range(len(matrix[row])):

                if matrix[row][col] == 0:
                    self._update_cols(row, col, matrix, change_set)
                    self._update_rows(row, col, matrix, change_set)
        
        for row, col in change_set:

            matrix[row][col] = 0
        
        