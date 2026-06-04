from concurrent.futures import ThreadPoolExecutor

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def check_row(board: list[list[str]], row_idx: int) -> bool:
            """Validates that a single row contains no duplicate numbers."""
            seen = set()
            for val in board[row_idx]:
                if val != '.' and val != '0':
                    if val in seen:
                        return False
                    seen.add(val)
            return True

        def check_col(board: list[list[str]], col_idx: int) -> bool:
            """Validates that a single column contains no duplicate numbers."""
            seen = set()
            for row_idx in range(9):
                val = board[row_idx][col_idx]
                if val != '.' and val != '0':
                    if val in seen:
                        return False
                    seen.add(val)
            return True

        def check_subgrid(board: list[list[str]], start_row: int, start_col: int) -> bool:
            """Validates that a single 3x3 box contains no duplicate numbers."""
            seen = set()
            for r in range(start_row, start_row + 3):
                for c in range(start_col, start_col + 3):
                    val = board[r][c]
                    if val != '.' and val != '0':
                        if val in seen:
                            return False
                        seen.add(val)
            return True

        def is_valid_sudoku_multithreaded(board: list[list[str]]) -> bool:
            tasks = []
            
            # Generate the 27 validation tasks
            with ThreadPoolExecutor(max_workers=4) as executor:
                # 1. Row tasks
                for i in range(9):
                    tasks.append(executor.submit(check_row, board, i))
                    
                # 2. Column tasks
                for j in range(9):
                    tasks.append(executor.submit(check_col, board, j))
                    
                # 3. 3x3 subgrid tasks
                for r in (0, 3, 6):
                    for c in (0, 3, 6):
                        tasks.append(executor.submit(check_subgrid, board, r, c))
                        
                # Gather results; if any task returns False, the board is invalid
                for task in tasks:
                    if not task.result():
                        return False
                        
            return True

        return is_valid_sudoku_multithreaded(board)
        