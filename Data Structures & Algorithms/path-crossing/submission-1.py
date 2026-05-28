class Solution:
    def isPathCrossing(self, path: str) -> bool:

        visited = set()
        
        cur_x = 0
        cur_y = 0

        visited.add((cur_x, cur_y))
        
        for direction in path:

            print(cur_x, cur_y)

            if direction == 'N' and (cur_x, cur_y + 1) not in visited:
                cur_x, cur_y = cur_x, cur_y + 1
                visited.add((cur_x, cur_y))
            elif direction == 'E' and (cur_x + 1, cur_y) not in visited:
                cur_x, cur_y = cur_x + 1, cur_y
                visited.add((cur_x, cur_y))
            elif direction == 'S' and (cur_x, cur_y - 1) not in visited:
                cur_x, cur_y = cur_x, cur_y - 1
                visited.add((cur_x, cur_y))
            elif direction == 'W' and (cur_x - 1, cur_y) not in visited:
                cur_x, cur_y = cur_x - 1, cur_y
                visited.add((cur_x, cur_y))
            else:
                return True
        
        return False
        