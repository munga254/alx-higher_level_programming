#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    # Check if it is safe to place a queen at board[row][col]

    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal on the left side
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve_nqueens(board, col):
    # Base case: If all queens are placed
    # then print the solution and return
    if col == N:
        print_solution(board)
        return

    # Consider this column and try placing
    # the queen in all rows one by one
    for row in range(N):
        if is_safe(board, row, col):
            # Place the queen in board[row][col]
            board[row][col] = 1

            # Recur to place the rest of the queens
            solve_nqueens(board, col + 1)

            # Backtrack: Remove the queen from board[row][col]
            board[row][col] = 0

def print_solution(board):
    # Print the board configuration for a solution
    for row in range(N):
        for col in range(N):
            if board[row][col] == 1:
                print(f"({row}, {col})", end=" ")
    print()

if __name__ == "__main__":
    # Check the command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Create an empty N x N board
    board = [[0] * N for _ in range(N)]

    # Solve the N Queens problem
    solve_nqueens(board, 0)

