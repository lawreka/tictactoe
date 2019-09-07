from IPython.display import clear_output
import random

def display_board(board):
    top = {"1": f"  {board[1]}  |", "2": f" {board[2]}  |", "3": f" {board[3]}  "}
    middle = {"4": f"  {board[4]}  |", "5": f" {board[5]}  |", "6": f" {board[6]}  "}
    bottom = {"7": f"  {board[7]}  |", "8": f" {board[8]}  |", "9": f" {board[9]} "}
    divider = "–––––––––––––––"
    print("\n")
    for i in top:
        print(top[i], end=" ")
    print(f'\n {divider}')
    for i in middle:
        print(middle[i], end=" ")
    print(f'\n {divider}')
    for i in bottom:
        print(bottom[i], end=" ")
    print("\n")

def player_input():
    player1 = input("\nPlease pick a marker (X/O):  ")
    while player1 is not 'X' and player1 is not 'O':
        player1 = input("\nPlease pick a marker (X/O):  ")
    else:
        print(f'\nPlayer 1 is {player1}')
        return player1

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark:
        print(f'\n{mark} wins, top row')
        return True
    elif board[4] == board[5] == board[6] == mark:
        print(f'\n{mark} wins, middle row')
        return True
    elif board[7] == board[8] == board[9] == mark:
        print(f'\n{mark} wins, bottom row')
        return True
    elif board[1] == board[4] == board[7] == mark:
        print(f'\n{mark} wins, first col')
        return True
    elif board[2] == board[5] == board[8] == mark:
        print(f'\n{mark} wins, second col')
        return True
    elif board[3] == board[6] == board[9] == mark:
        print(f'\n{mark} wins, third col')
        return True
    elif board[1] == board[5] == board[9] == mark:
        print(f'\n{mark} wins, diagonally')
        return True
    elif board[3] == board[5] == board[7] == mark:
        print(f'\n{mark} wins, diagonally')
        return True
    else:
        return False

def choose_first():
    first = random.randint(1,2)
    print(f'\nPlayer {first} goes first')
    return first

def space_check(board, position):
    position = int(position)
    if board[position] == 'X':
        print("\nThat space is taken")
        return False
    elif board[position] == 'O':
        print("\nThat space is taken")
        return False
    else:
        return True

def full_board_check(board):
    full = False
    for i in range(1,10):
        if board[i] == 'X':
            full = True
        elif board[i] == 'O':
            full = True
        else:
            full = False
            break
    if full == True:
        return True
    else:
        return False

def player_choice(board):
    position = input("Choose your next move (1-9):  ")
    while space_check(board, position) == False:
        print("\nChoose another space")
        position = input("\nChoose your next move (1-9):  ")
    else:
        return int(position)

def replay():
    again = input("\nDo you want to play again? (Y/N):  ")
    if again == 'Y':
        print('\nOK! rematch')
        return True
    else:
        print("\nOK :( game over")
        return False

print('Welcome to Tic Tac Toe!')
player1 = 'none'
player2 = 'none'
game = True
#while True:
while game == True:
    print("Let's go")
    # Set the game up here
    board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    display_board(board)
    player1 = player_input()
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    turn = choose_first()
    game_on = True
    game = False
    while game_on == True:
        if turn == 1:
            print('\nPlayer 1:')
            choice = player_choice(board)
            place_marker(board, player1, choice)
            display_board(board)
            if win_check(board, player1):
                print("\nPlayer 1 wins")
                game_on = False
            elif full_board_check(board):
                print("Stalemate")
                game_on = False
            else:
                turn = 2
        else:
            print('\n\nPlayer 2:')
            choice = player_choice(board)
            place_marker(board, player2, choice)
            display_board(board)
            if win_check(board, player2):
                game_on = False
                print("\nPlayer 2 wins")
            elif full_board_check(board):
                print("Stalemate")
                game_on = False
            else:
                turn = 1
    else:
        game = replay()
