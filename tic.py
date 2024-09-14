# Tic-Tac-Toe Game in Python

# Create an empty Tic-Tac-Toe board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function for player move
def player_move(player):
    while True:
        move = input(f"Player {player}, enter a move (1-9): ")
        if move.isdigit():
            move = int(move) - 1
            if 0 <= move <= 8 and board[move] == ' ':
                board[move] = player
                break
            else:
                print("Invalid move! Try again.")
        else:
            print("Please enter a number.")

# Function to check if a player has won
def check_win(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to check for a draw
def is_draw(board):
    return ' ' not in board

# Main game loop
def tic_tac_toe():
    current_player = 'X'
    
    while True:
        print_board(board)
        player_move(current_player)
        
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
tic_tac_toe()
