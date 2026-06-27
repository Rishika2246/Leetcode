class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [""] * numRows
        cur_row = 0
        direction = -1   # will flip to 1 initially

        for char in s:
            rows[cur_row] += char
            
            # change direction at top or bottom
            if cur_row == 0 or cur_row == numRows - 1:
                direction *= -1
            
            cur_row += direction
        
        return "".join(rows)