def is_safe(board, row, col, n):

    for i in range(row):
        if board[i][col] == 1:
            return False

        
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1


    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True

def solve_n_queens(board, row, n):

    if row == n:
        return True


    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            
            if solve_n_queens(board, row + 1, n):
                return True


            board[row][col] = 0

    return False
def print_board(board, n):
    print("\nSolution Board:\n")
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
if __name__ == "__main__":
    print("N-QUEENS PROBLEM USING BACKTRACKING\n")
    n = int(input("Enter number of queens (N): "))
    board = [[0 for _ in range(n)] for _ in range(n)]
    if solve_n_queens(board, 0, n):
        print_board(board, n)
    else:
        print("\nNo solution exists.")
