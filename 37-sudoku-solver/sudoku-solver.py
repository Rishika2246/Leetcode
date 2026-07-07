class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append((i, j))
                else:
                    val = board[i][j]
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i // 3) * 3 + j // 3].add(val)
        
        def backtrack(index):
            if index == len(empty):
                return True
            
            i, j = empty[index]
            box_id = (i // 3) * 3 + j // 3
            
            for ch in '123456789':
                if ch not in rows[i] and ch not in cols[j] and ch not in boxes[box_id]:
                    board[i][j] = ch
                    rows[i].add(ch)
                    cols[j].add(ch)
                    boxes[box_id].add(ch)
                    
                    if backtrack(index + 1):
                        return True
                    
                    board[i][j] = '.'
                    rows[i].remove(ch)
                    cols[j].remove(ch)
                    boxes[box_id].remove(ch)
            
            return False
        
        backtrack(0)