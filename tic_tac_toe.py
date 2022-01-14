# File Name: tic_tac_toe.py
# Author: Rick Larrabee

def main ():
    print ('Welcome to the great game of tic tac toe')
    print ('please enter the player information.')
    player_1 = input('Enter the name for player 1 (will be X): ')
    player_2 = input('Enter the name for player 2 (will be O): ')
    current_player = player_1
    current_play = 0
    board_squares = set_board ()
    while not (determine_winner(board_squares) or current_play == 9):
        print_board(board_squares)
        player_move(current_play, current_player, player_1, player_2, board_squares)
        current_play = current_play + 1
        print(current_play)
        current_player = switch_player (current_player, player_1, player_2)
    determine_draw (current_play)
    print_board

def set_board ():
    board_squares = []

    for value in range (9):
        board_squares.append(value+1)

    return board_squares

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

def determine_winner (squares):
    return (squares[0] == squares[1] ==squares[2] or
            squares[3] == squares[4] ==squares[5] or
            squares[6] == squares[7] ==squares[8] or
            squares[0] == squares[4] ==squares[8] or
            squares[2] == squares[4] ==squares[6] or
            squares[0] == squares[3] ==squares[6] or
            squares[1] == squares[4] ==squares[7] or
            squares[2] == squares[5] ==squares[8])

def determine_draw (current_play):
    if current_play == 9:
        print('This game is a draw.')


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

def switch_player (current_player, player_1, player_2):
    if current_player == player_1:
        current_player = player_2
    elif current_player == player_2:
        current_player = player_1
    return current_player
        

if __name__ == "__main__":
    main()