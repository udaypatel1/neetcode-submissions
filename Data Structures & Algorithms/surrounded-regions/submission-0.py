from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        visited = set()
        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS):

                if board[r][c] == 'O' and (r, c) not in visited:

                    q = deque([(r, c)])
                    local = set([(r, c)])
                    visited.add((r, c))
                    valid = True

                    while q:
                        row, col = q.popleft()

                        # touches border → not capturable
                        if row == 0 or col == 0 or row == ROWS - 1 or col == COLS - 1:
                            valid = False

                        for dr, dc in directions:
                            nr, nc = row + dr, col + dc

                            if 0 <= nr < ROWS and 0 <= nc < COLS:

                                if board[nr][nc] == 'O' and (nr, nc) not in visited:

                                    visited.add((nr, nc))
                                    local.add((nr, nc))
                                    q.append((nr, nc))

                    if valid:
                        for row, col in local:
                            board[row][col] = 'X'
