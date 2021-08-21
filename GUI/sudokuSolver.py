
# Don't forget to modify your soduko accordingly such as may be your sudoku contains (0) as empty places and numbers as (integers)
# Here empty places are considered as "." and numbers as strings

# HELPER ----- FUNCTION 
def is_valid_move(grid, row, col, number):
    # Check for same number in row 
    for x in range(9):
        if grid[row][x] == number:
            return False

    # Check for same number in column
    for x in range(9):
        if grid[x][col] == number:
            return False

    # check for same number in local field (square)
    corner_row = row - row % 3
    corner_col = col - col % 3
    for x in range(3):
        for y in range(3):
            if grid[corner_row + x][corner_col + y] == number:
                return False
    return True

# SOLVE ----- FUNCTION 
def solve(grid):
    # traversing sudoku grid one entry at a time, update sudoku with possible values
    # also  keep a  check  if  that values is valid thru backtracking
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                # iterate over grid to check valid solution for sudoku
                for num in range(1, 10):
                    if is_valid_move(grid, i, j, str(num)):
                        grid[i][j] = str(num)

                        # again check if updated grid is valid
                        if solve(grid):
                            return True
                        grid[i][j] = "."
                # no valid num found via bactracking
                return False
    return True

# MAIN --- CODE 
board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
        ]
        
solve(board)

# in-place suduko puzzle gets solved(modified)
# print(board)

# print in the format of 2-D array
outputSudoku = []
for i in range(9):
    solvedSudoku = []
    for j in range(9):
        solvedSudoku.append(board[i][j])
    outputSudoku.append(solvedSudoku)
    print(outputSudoku[i])


