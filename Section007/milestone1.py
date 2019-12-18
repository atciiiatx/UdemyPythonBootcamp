"""MIlestone 1."""


def greet():
    """Start the game."""
    print("Weldomce to Tic Tac Toe!")


def get_symbol_choice():
    """Let the user choose his symbol."""
    symbol = ''
    while symbol != 'X' and symbol != 'O':
        s = input("Would you like to Play X or O?")
        if s[0].lower() == 'x':
            symbol = 'X'
        elif s[0].lower() == 'o':
            symbol = 'O'
    print(f'You chose {symbol}')
    return symbol


def get_play_choice():
    """Let the user decide whether to play."""
    s = input("Would you like to play a game? Type Y or N. ")
    return s[0].lower() == 'y'


def init_player_symbols(symbol):
    """Initialize player symbols."""
    if symbol == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def init_game():
    """Initialize the game."""
    print('Starting game.')
    board = [x for x in range(1, 10)]
    symbol = get_symbol_choice()
    player_symbols = init_player_symbols(symbol)
    return [board, player_symbols]


def print_board(board):
    """Print the game board."""
    print('-------------')
    last = len(board) - 1
    for i in range(0, 3):

        print('|   |   |   |')
        print(f'| {board[last-2]} | {board[last-1]} | {board[last]} |')
        print('|   |   |   |')
        print('-------------')
        last -= 3


def get_selection(ps, board):
    """Let the user pick a square."""
    selection = -1
    while selection < 0:
        choice = int(input(f'Choose square for {ps}.'))
        if choice in range(1, 10):
            if board[choice-1] in ['X', 'Y']:
                print("That square is already chosen. Try again.")
            else:
                selection = choice - 1
        else:
            print("Choice out of range. Try again.")
    return selection


def game_over_horizontal(board):
    """Check for horizontal win"""
    start = 0
    for i in range(0, 3):
        count = 0
        player = board[start]
        for j in range(0, 3):
            if board[start+j] == player:
                count += 1
        if count == 3:
            return [True, 'Horizontal win by ' + player]
        start += 3
    return [False, 'Nobody won']


def game_over_vertical(board):
    """Check for vertical win."""
    start = 0
    for i in range(0, 3):
        count = 0
        player = board[start]
        for j in range(0, 3):
            if board[start+3*j] == player:
                count += 1
        if count == 3:
            return [True, 'Vertical win by ' + player]
        start += 1
    return [False, 'Nobody won']


def game_over_diagonal(board):
    """Determine whether the game is over."""
    if ((board[0] == board[4] and board[4] == board[8]) or
            (board[2] == board[4] and board[4] == board[6])):
        return [True, 'Diagonal win by ' + board[4]]
    return [False, 'Nobody won']


def game_over_no_moves(board):
    """Determine whether there are no moves yet."""
    for p in board:
        if p != 'X' and p != 'O':
            return [False, "Moves available"]
    return [True, "No moves left. Nobody won."]


def game_over(board):
    """Determine whether the game is over."""
    result = game_over_horizontal(board)
    if result[0]:
        return result
    result = game_over_vertical(board)
    if result[0]:
        return result
    result = game_over_diagonal(board)
    if result[0]:
        return result
    result = game_over_no_moves(board)
    return result


def play_game():
    """Play a round of the game."""
    board, player_symbols = init_game()
    player_number = 0
    while not game_over(board)[0]:
        ps = player_symbols[player_number]
        print_board(board)
        sel = get_selection(ps, board)
        board[sel] = ps
        player_number = (player_number + 1) % 2
    print(f'Game over. {game_over(board)[1]}')


greet()
while get_play_choice():
    play_game()
print('Goodbye')
