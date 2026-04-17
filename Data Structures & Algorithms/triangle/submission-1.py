class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        memo = dict()

        def dfs(row, col):

            if (row, col) in memo:
                return memo[(row, col)]
            
            if row == len(triangle):
                return 0

            # move to i + 1 on next row, but add the cur row cols value
            move = triangle[row][col] + dfs(row + 1, col + 1)

            # stay, don't move. still add the cur row cols value
            stay = triangle[row][col] + dfs(row + 1, col)

            result = min(move, stay)

            memo[(row, col)] = result

            return result
        
        return dfs(0,0)




        