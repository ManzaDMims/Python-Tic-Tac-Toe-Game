class TicTacToe:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_draw(board):
    return all(spot in ['X', 'O'] for spot in board)

def get_valid_moves(board):
    return [i for i, spot in enumerate(board) if spot not in ['X', 'O']]

def ai_move(board):
    valid_moves = get_valid_moves(board)
    return random.choice(valid_moves)

def tic_tac_toe():
    board = [str(i) for i in range(1, 10)]
    current_player = 'X'
    mode = input("Enter 1 for Player vs Player or 2 for Player vs AI: ")

    while True:
        print_board(board)
        valid_moves = get_valid_moves(board)
        
        if current_player == 'X' or mode == '1':
            move = input(f"Player {current_player}, enter your move (1-9): ")

            if move.isdigit() and int(move) - 1 in valid_moves:
                board[int(move) - 1] = current_player
            else:
                print("Invalid move. Please try again.")
                continue
        else:
            print("AI is making a move...")
            move = ai_move(board)
            board[move] = 'O'

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
