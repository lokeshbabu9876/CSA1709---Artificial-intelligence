N = 8  # size of chessboard

def print_solution(board):
    for i in range(N):
        row = ""
        for j in range(N):
            if board[i] == j:
                row += "Q "
            else:
                row += ". "
        print(row)
    print("\n")

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_nqueens(row, board, solutions):
    if row == N:
        solutions.append(board[:])
        print_solution(board)   # Print each solution
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(row + 1, board, solutions)

def solve():
    board = [-1] * N
    solutions = []
    solve_nqueens(0, board, solutions)
    print("Total solutions:", len(solutions))

# Run solver
solve()
