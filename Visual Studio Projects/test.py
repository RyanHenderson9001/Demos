import random

# Size of the Sudoku grid
N = 9
SUBGRID_SIZE = 3  # 3x3 subgrids

def print_board(board):
    """Print the Sudoku board in a user-friendly format."""
    for row in range(N):
        if row % SUBGRID_SIZE == 0 and row != 0:
            print("-" * 21)  # Print line between subgrids
        for col in range(N):
            if col % SUBGRID_SIZE == 0 and col != 0:
                print("|", end=" ")
            print(board[row][col], end=" ")
        print()

def is_valid(board, row, col, num):
    """Check if a number can be placed at board[row][col]."""
    # Check if the number is in the current row
    if num in board[row]:
        return False
    
    # Check if the number is in the current column
    for r in range(N):
        if board[r][col] == num:
            return False

    # Check if the number is in the current 3x3 subgrid
    start_row = (row // SUBGRID_SIZE) * SUBGRID_SIZE
    start_col = (col // SUBGRID_SIZE) * SUBGRID_SIZE
    for r in range(start_row, start_row + SUBGRID_SIZE):
        for c in range(start_col, start_col + SUBGRID_SIZE):
            if board[r][c] == num:
                return False
    
    return True

def solve(board):
    """Solve the Sudoku puzzle using backtracking."""
    for row in range(N):
        for col in range(N):
            if board[row][col] == 0:  # Empty space
                for num in range(1, N + 1):  # Try numbers 1-9
                    if is_valid(board, row, col, num):
                        board[row][col] = num  # Place number
                        if solve(board):  # Recursively try to solve
                            return True
                        board[row][col] = 0  # Backtrack
                return False  # If no valid number, return False
    return True  # Puzzle solved

def generate_sudoku():
    """Generate a random solvable Sudoku puzzle."""
    # Create an empty board
    board = [[0] * N for _ in range(N)]
    
    # Fill the diagonal 3x3 subgrids (this part ensures uniqueness)
    for i in range(0, N, SUBGRID_SIZE):
        nums = random.sample(range(1, N+1), N)  # Randomize numbers 1-9
        idx = 0
        for r in range(i, i + SUBGRID_SIZE):
            for c in range(i, i + SUBGRID_SIZE):
                board[r][c] = nums[idx]
                idx += 1

    # Solve the board to ensure it's a valid Sudoku puzzle
    if solve(board):
        return board
    else:
        return generate_sudoku()  # Try again if it's not solvable

def remove_numbers(board, num_cells_to_remove):
    """Remove numbers randomly to create the puzzle."""


    puzzle = [row[:] for row in board]  # Make a copy of the board
    count = 0
    while count < num_cells_to_remove:
        row = random.randint(0, N-1)
        col = random.randint(0, N-1)
        if puzzle[row][col] != 0:
            puzzle[row][col] = 0  # Remove the number
            count += 1
    return puzzle

def main():
    """Main function to generate, display, and solve Sudoku."""
    print("Generating Sudoku puzzle...")
    board = generate_sudoku()
    print("Generated Sudoku Board:")
    print_board(board)
    
    print("\nSolving Sudoku...")
    if solve(board):
        print("Solved Sudoku Board:")
        print_board(board)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
