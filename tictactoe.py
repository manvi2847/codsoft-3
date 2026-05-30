import math

# Initialize the board as a list of 9 empty strings
board = [' ' for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(f"| {board[i]} | {board[i+1]} | {board[i+2]} |")

def check_win(player):
    # All possible winning combinations
    win_coords = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_coords)

def is_board_full():
    return ' ' not in board

def minimax(is_maximizing):
    if check_win('O'): return 1
    if check_win('X'): return -1
    if is_board_full(): return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def get_best_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

# --- Game Loop ---
print("You are 'X', AI is 'O'. Input moves 0-8.")
while not (check_win('X') or check_win('O') or is_board_full()):
    print_board()
    move = int(input("Your move (0-8): "))
    if board[move] == ' ':
        board[move] = 'X'
        if not (check_win('X') or is_board_full()):
            ai_move = get_best_move()
            board[ai_move] = 'O'
    else:
        print("Invalid move!")

print_board()
print("Game Over!")
