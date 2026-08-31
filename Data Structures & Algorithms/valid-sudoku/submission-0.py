class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = set()
            for j in range(9):
                box = board[i][j]
                if box != '.' and box in seen:
                    return False
                seen.add(box)

        for j in range(9):
            seen = set()
            for i in range(9):
                box = board[i][j]
                if box != '.' and box in seen:
                    return False
                seen.add(box)

        for row_box in range(3):
            for col_box in range(3):
                seen = set()
                for i in range(3 * row_box, 3 * row_box + 3):
                    for j in range(3 * col_box, 3 * col_box + 3):
                        box = board[i][j]
                        if box != '.' and box in seen:
                            return False
                        seen.add(box)

        return True