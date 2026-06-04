
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Arrays of integers acting as bitmasks for rows, columns, and boxes
        # Initialized to 0 (meaning no numbers seen yet)
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                if val == '.':
                    continue
                
                # Convert character digit directly to bit shift value
                # "1" -> 1, "9" -> 9 (guaranteed valid by typical constraints)
                digit_bit = 1 << int(val)
                
                # Formula to map (r, c) coordinate to one of the 9 subgrids (0 to 8)
                box_idx = (r // 3) * 3 + (c // 3)

                # Bitwise AND checks if the digit bit was already flipped to 1
                if (rows[r] & digit_bit) or (cols[c] & digit_bit) or (boxes[box_idx] & digit_bit):
                    return False

                # Bitwise OR records the digit as 'seen'
                rows[r] |= digit_bit
                cols[c] |= digit_bit
                boxes[box_idx] |= digit_bit

        return True