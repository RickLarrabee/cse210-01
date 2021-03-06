# File Name: tic_tac_toe.py
# Author: Rick Larrabee

"""This tic tac toe game shows the ability to utilize functions to make
simple game in Python"""

# Main function that runs the game 
def main ():
    print ('Welcome to the great game of tic tac toe')
    print ('please enter the player information.')
    player_1 = "Player 1"
    player_2 = "Player 2"
    current_player = player_1
    current_play = 0
    board_squares = set_board ()
    while not (determine_winner(board_squares) or current_play == 9):
        print_board(board_squares)
        player_move(current_play, current_player, player_1, player_2, board_squares)
        print('\n')
        current_play = current_play + 1
        if not (determine_winner(board_squares) or current_play == 9):
            current_player = switch_player (current_player, player_1, player_2)
    print_board(board_squares)
    if current_play == 9:
        print("It is a draw")
    else:
        print (f"Congratulaitons {current_player} you won!")
    print ('\n')
    if play_again() == "Y":
        main()
    else:
        print("Thank you for playing.")

# Function that sets the values for the board in a list
def set_board ():
    board_squares = []

    for value in range (9):
        board_squares.append(value+1)

    return board_squares

# Function that prints the board for the players to see.
def print_board (squares):
    
    print ('   |   |   ')
    print (f' {squares[0]} | {squares[1]} | {squares[2]}')
    print ('   |   |   ')
    print ('------------')
    print ('   |   |   ')
    print (f' {squares[3]} | {squares[4]} | {squares[5]}')
    print ('   |   |   ')
    print ('------------')   
    print ('   |   |   ')
    print (f' {squares[6]} | {squares[7]} | {squares[8]}')
    print ('   |   |   ')

# Function that will look at the current board and determine if there is a winner.
def determine_winner (squares):
    return (squares[0] == squares[1] ==squares[2] or
            squares[3] == squares[4] ==squares[5] or
            squares[6] == squares[7] ==squares[8] or
            squares[0] == squares[4] ==squares[8] or
            squares[2] == squares[4] ==squares[6] or
            squares[0] == squares[3] ==squares[6] or
            squares[1] == squares[4] ==squares[7] or
            squares[2] == squares[5] ==squares[8])

# Function allows the current player to select the square they want and determines if the move is valid.
def player_move (current, current_player, player_1, player_2, squares):
    while True:
        try:
            player_move = int(input (f'{current_player} please select a unused number from the board: '))
            if player_move > 9 or player_move < 1:
                raise ValueError
            elif squares[player_move -1] == 'X' or squares[player_move -1] == 'O':
                raise ValueError 
            elif current_player == player_1:
                squares[player_move -1] = 'X'
            elif current_player == player_2:
                squares[player_move -1] = 'O'
            break

        except ValueError:
            print ('wrong input, please try again.')


# Function to change the player for the next move.
def switch_player (current_player, player_1, player_2):
    if current_player == player_1:
        current_player = player_2
    elif current_player == player_2:
        current_player = player_1
    return current_player

# Function to ask if the players want another game.
def play_again ():
    while True:
        try:
            new_game=input ("Do you want to play again (Y or N): ")
            if new_game.upper() not in ("Y", "N"):
                raise ValueError
            break
        except ValueError:
            print ("You must choose Y or N")
    return new_game.upper()

if __name__ == "__main__":
    main()