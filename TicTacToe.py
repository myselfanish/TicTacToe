from tkinter import *
import tkinter.messagebox
import random

root = Tk()

label1 = Label(root, text="Welcome to T.T.T", bg='blue', fg='white')
label1.pack()

tkinter.messagebox._show('Welcome Message', 'Welcome to T.T.T')


def display_board(board):  # this function is for displaying grids and marks for user convenience
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')


def player_input():  # this function is for asking user to make a choice ie., like toss to start game
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O :').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):  # this function is for checking whether the player is win or nor
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # if all the marks in top row are equal
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # if all the marks in middle row are equal
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # if all the marks in bottom row are equal
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # if all the marks in first column are equal
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # if all the marks in second column are equal
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # if all the marks in third column are equal
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # if all the marks in left to right daigonal
            (board[9] == mark and board[5] == mark and board[1] == mark))   # if all the marks in left to right daigonal


def choose_first():  # this function is for selecting one random player to play first turn
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):  # this function is used for checking whether a space is available or not in board
    return board[position] == ' '


def full_board_check(board):  # this function is used for checking whether the board is full or not
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):  # this function is for taking input from user

    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = input('Choose your next position : (1-9)')
    return int(position)


def replay():  # this function is used for asking user to start the game and also to replay the game or not
    return input('Do you want to play again? Enter Yes or No : ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')

while True:  # this loop will reset the board to empty when game is started.

    board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    toss = turn + ' Won the toss'
    tkinter.messagebox._show('Players Info', toss)
    print(turn + ' will go first.')
    game_on = True

    while game_on:
        if turn == 'Player 1':
            # Player 1 will get the first chance to play

            display_board(board)
            tkinter.messagebox._show('Players Info', 'Player 1, Its your turn')
            position = player_choice(board)
            place_marker(board, player1_marker, position)

            if win_check(board, player1_marker):  # this loop checks whether the player has won or not
                display_board(board)
                tkinter.messagebox._show('Players Info', 'Player 1 has won the game!')
                print('Player 1 has won the game!')
                game_on = False  # if player wins then the game is stopped by changing it to false
            else:
                if full_board_check(board):  # it checks the board whether it is fully occupied or not
                    display_board(board)
                    tkinter.messagebox._show('Players Info', 'The game is DRAW !')
                    print('The game is a draw !')  # if board if full and no player wins the game, it returns draw statement
                    break
                else:
                    turn = 'Player 2'  # if there is space it makes the turn to another player

        else:
            # Player 2 will get the chance to play

            display_board(board)
            tkinter.messagebox._show('Players Info', 'Player 2, Its your turn')
            position = player_choice(board)
            place_marker(board, player2_marker, position)

            if win_check(board, player2_marker):
                display_board(board)
                tkinter.messagebox._show('Players Info', 'Player 2 has won the game!')
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    tkinter.messagebox._show('Players Info', 'The game is DRAW !')
                    print('The game is a Draw !')
                    break
                else:
                    turn = 'Player 1'

    if not replay():  # this code will break the loop and stops the program
        break



