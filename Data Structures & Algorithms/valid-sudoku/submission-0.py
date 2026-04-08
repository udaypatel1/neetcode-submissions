from collections import Counter

class Solution:

    def within_range(self, digit: int) -> bool:
        return 1 <= digit <= 9

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row_idx in range(len(board)):

            digits = set()
            
            for val in board[row_idx]:
                if val == '.':
                    continue
                if val.isdigit() and val not in digits and self.within_range(int(val)):
                    digits.add(val)
                else:
                    return False
            
        for col in range(len(board[0])):

            digits = set()

            for row in range(len(board)):
                
                val = board[row][col]

                if val == '.':
                    continue
                
                if val.isdigit() and val not in digits and self.within_range(int(val)):
                    digits.add(val)
                else:
                    return False

        dirs = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]

        for row in range(0, len(board), 3):
            for col in range(0, len(board[row]), 3):

                visited = set()

                for dr, dc in dirs:
                    nr = row + dr
                    nc = col + dc

                    val = board[nr][nc]

                    if val == '.':
                        continue

                    if val.isdigit() and val not in visited and self.within_range(int(val)):
                        visited.add(val)
                    else:
                        return False

        return True



            
            
        
    
        


        