class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(list)
        col = defaultdict(list)
        block = defaultdict(list)
        for x in range(9):
            for y in range(9):
                if board[x][y] == ".":
                    continue
               
                block_index = (x // 3) * 3 + (y // 3)

                if board[x][y] in row[x]:
                    return False
                row[x].append(board[x][y])
                if board[x][y] in col[y]:
                    return False
                col[y].append(board[x][y]) 
                if board[x][y] in block[block_index]:
                    return False
                block[block_index].append(board[x][y])
            print(block)
        return True