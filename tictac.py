import math

board = [" " for _ in range(9)]

def print_board():
    for i in range(0,9,3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")

def check_winner():
    win_positions = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]

    for a,b,c in win_positions:
        if board[a]==board[b]==board[c] and board[a]!=" ":
            return board[a]

    if " " not in board:
        return "Draw"

    return None


def minimax(is_max, alpha, beta):

    result = check_winner()

    if result == "X":
        return 1
    elif result == "O":
        return -1
    elif result == "Draw":
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i]==" ":
                board[i]="X"
                val=minimax(False,alpha,beta)
                board[i]=" "
                best=max(best,val)
                alpha=max(alpha,val)
                if beta<=alpha:
                    break
        return best

    else:
        best = math.inf
        for i in range(9):
            if board[i]==" ":
                board[i]="O"
                val=minimax(True,alpha,beta)
                board[i]=" "
                best=min(best,val)
                beta=min(beta,val)
                if beta<=alpha:
                    break
        return best


def best_move():
    best_val=-math.inf
    move=-1

    for i in range(9):
        if board[i]==" ":
            board[i]="X"
            val=minimax(False,-math.inf,math.inf)
            board[i]=" "

            if val>best_val:
                best_val=val
                move=i

    return move


while True:

    print_board()
    pos=int(input("Enter position (0-8): "))

    if board[pos]==" ":
        board[pos]="O"

    if check_winner():
        break

    ai_move=best_move()
    board[ai_move]="X"

    if check_winner():
        break


print_board()
print("Winner:",check_winner())
