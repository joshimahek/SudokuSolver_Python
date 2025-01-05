def find_next_empty(puzzle):
    # Find the next empty spot in the puzzle
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None

def is_valid(puzzle, guess, row, col):
    # Check if the guess is valid in the row
    if guess in puzzle[row]:
        return False

    # Check if the guess is valid in the column
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # Check if the guess is valid in the 3x3 grid
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def solveSudoku(puzzle):
    # Find the next empty spot
    row, col = find_next_empty(puzzle)

    # If there are no empty spots, the puzzle is solved
    if row is None:
        return True

    # Try guesses from 1 to 9
    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess

            # Recursively attempt to solve the puzzle
            if solveSudoku(puzzle):
                return True

        # Reset the guess if it doesn't work
        puzzle[row][col] = -1

    return False

if __name__ == '__main__':
    example_board = [
       [3, 9, -1,  -1, 5, -1,  -1, -1, -1],
       [-1, -1, -1,  2, -1, -1,  -1, -1, 5],
       [-1, -1, -1,  7, 1, 9,  -1, 8, -1],

       [-1, 5, -1,  -1, 6, 8,  -1, -1, -1],
       [2, -1, 6,  -1, -1, 3,  -1, -1, -1],
       [-1, -1, -1,  -1, -1, -1,  -1, -1, 4],

       [5, -1, -1,  -1, -1, -1,  -1, -1, -1],
       [6, 7, -1,  1, -1, 5,  -1, 4, -1],
       [1, -1, 9,  -1, -1, -1,  2, -1, -1]
    ]

    if solveSudoku(example_board):
        for row in example_board:
            print(row)
    else:
        print("No solution exists.")
