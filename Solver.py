ROWS, COLS = 9, 9
NUM_ROW_IN_SQUARE, NUM_COL_IN_SQUARE = 3, 3

def solver(puzzle):
    next_coordinates = find_next(puzzle)
    if not next_coordinates:
        return True
    else:
        row, col = next_coordinates

    for i in range(10):
        if check_valid_number(row, col, i, puzzle):
            puzzle[row][col] = i

            if solver(puzzle):
                return True
            
            puzzle[row][col] = 0

    return False


def find_next(puzzle):
    for i in range(ROWS):
        for j in range(COLS):
            if puzzle[i][j] == 0:
                return (i, j)

    return None

def check_valid_number(row, col, num, puzzle):

    # check if number is in the row
    if num in puzzle[row]:
        return False
    
    # check if number is in the column
    for i in range(ROWS):
        if i == row:
            continue

        if puzzle[i][col] == num:
            return False

    # check if number is in square
    colOffset = col % NUM_COL_IN_SQUARE # checks column offset in the given square
    rowOffset = row % NUM_ROW_IN_SQUARE # checks row offset in the given square

    for i in range(3):
        for j in range(3):
            if i == row and j == col:
                continue

            if num == puzzle[i + row - rowOffset][j + col - colOffset]:
                return False


    return True

def print_puzzle(example_puzzle):
    for i in range(ROWS):
        for j in range(COLS):
            print(example_puzzle[i][j], end = " ")
        print()
    return 0

example_puzzle = [[0,0,0,2,6,0,7,0,1],
                  [6,8,0,0,7,0,0,9,0],
                  [1,9,0,0,0,4,5,0,0],
                  [8,2,0,1,0,0,0,4,0],
                  [0,0,4,6,0,2,9,0,0],
                  [0,5,0,0,0,3,0,2,8],
                  [0,0,9,3,0,0,0,7,4],
                  [0,4,0,0,5,0,0,3,6],
                  [7,0,3,0,1,8,0,0,0]]