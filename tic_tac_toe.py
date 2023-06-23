import random
board = [" ", " ", " ", 
        " ", " ", " ", 
        " ", " ", " "]

current_player = "X"
winner = None
game_running = True
choice = None

# printing the game board
def print_board(board):
    print(" %c | %c | %c" %(board[0], board[1], board[2]))
    print("___|___|___")
    print(" %c | %c | %c" %(board[3], board[4], board[5]))
    print("___|___|___")
    print(" %c | %c | %c" %(board[6], board[7], board[8]))
    print("   |   |   ")

# take player input
def player_input(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == " ":
        board[inp-1] = current_player
    else:
        print("Oops! you can't overwrite")

# check for win or tie
def check_horz(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != " ":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != " ":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != " ":
        winner = board[6]
        return True

def check_row(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != " ":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != " ":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != " ":
        winner = board[2]
        return True

def check_diag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != " ":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != " ":
        winner = board[2]
        return True

def check_tie(board):
    global game_running
    if " " not in board:
        print_board(board)
        print("It's a tie")
        game_running = False  

def check_win():
    global game_running
    if check_diag(board) or check_horz(board) or check_row(board):
        print_board(board)
        print(f"Player {winner} won")
        game_running = False     

# switch the player
def switch_player():
    global current_player 
    if current_player == "X":
        print("Its O's turn")
        current_player = "O"
    else: 
        print("Its X's turn")
        current_player = "X"        

# switch to computer
def computer(board):
    while current_player == "O":
        position = random.randint(0,8)
        if board[position] == " ":
            board[position] = "O"
            switch_player()

# starting the game
while game_running:
    print("Let's start the game!")
    try: 
        choice = int(input("Enter 1 for one player game\nEnter 2 for two player game: "))
    except ValueError:
        print("Invalid choice")
        continue
    if choice == 1:
        while game_running:
            print_board(board)
            player_input(board)
            switch_player()
            computer(board)
            check_win()
            check_tie(board)

    elif choice == 2:
        while game_running:
            print_board(board)
            player_input(board)
            switch_player()
            check_win()
            check_tie(board)

    contd = input("Do you want to continue?\nEnter yes to continue\nEnter no to exit: ")
    if contd == "yes":
        game_running = True
        board = [" ", " ", " ", 
                " ", " ", " ", 
                " ", " ", " "]

    elif contd == "no":
        print("Thanks for playing")
        game_running = False
    else: 
        print("Enter a valid choice")
