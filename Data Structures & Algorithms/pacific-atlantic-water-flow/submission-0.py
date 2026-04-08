from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def bfs(heights: List[List[int]], q) -> Set[Tuple[int, int]]:

            visited = set()

            for row, col in q:
                visited.add((row, col))

            directions = [
                (0,1),
                (0,-1),
                (1,0),
                (-1,0)
            ]

            while q:

                row, col = q.popleft()

                current_height = heights[row][col]

                for d_row, d_col in directions:

                    n_row = d_row + row
                    n_col = d_col + col

                    if 0 <= n_row < len(heights) and 0 <= n_col < len(heights[n_row]):

                        if heights[n_row][n_col] >= current_height and (n_row, n_col) not in visited:

                            q.append((n_row, n_col))
                            visited.add((n_row, n_col))

            return visited

        # we first pre-populate a queue, pacific and atlantic nodes

        pacific_q = deque()
        atlantic_q = deque()

        for col in range(len(heights[0])):

            pacific_q.append((0,col))
            atlantic_q.append((len(heights) - 1, col))

        for row in range(len(heights)):
            pacific_q.append((row, 0))
            atlantic_q.append((row, len(heights[row]) - 1))

        pacific_q_visited = bfs(heights, pacific_q)
        atlantic_q_visited = bfs(heights, atlantic_q)

        intersection = pacific_q_visited.intersection(atlantic_q_visited)

        return [list(cell) for cell in intersection]
            



