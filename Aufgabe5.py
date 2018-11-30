"""
Aufgabenblatt 5 EPR
Group 11
Author: Liming Kuang -- 6815480, Melanie Wester -- 5613641
Tutor: Felix Lapp

This is a simple python implementation of a modofied version of 
the game "Connect Four"
"""
import os, copy, sys

__author__ = "6815480: Liming Kuang, 5613641: Melanie Wester"  
__credits__ = "" 
__email__ = "limingkuang@gmail.com, s9108655@stud.uni-frankfurt.de"

def is_full(board):
    """is_full is a function which determines if the chess board is full
    board: the chess board that's being currently used
    This function returns True or False:
    True: this chess board is already full
    False: this chess board is still not full
    """
    for j in range(10):
        if board[0][j] == None:
            return False
    return True
    
def is_able_to_drop(col, board):
    """is_able_to_drop is a function to check if this column is valid for dropping a disk
    board: the chess board that's being currently used
    col: the index of the list
    """
    if (col < 10 and col >= 0) and board[0][col] == None:
        return True
    else:
        return False

def drop_disk(board, column, player):
    """drop_disk is a function to play a disk at the top of a specific column
    This function takes 3 parameters:
    board: the chess board that's being currently used
    column: an int, indicates the column where the user want to drop the disk
    player: a list, that contains information about the current player.
            It has the structure of [str, str, str]
            e.g.:['Player 1', 'Liming', 'X']
    """
    for i in range (0,9):
        if i <= 7 and board[i][column] == None and board[i+1][column] != None:
            board[i][column] = player[2]
        elif i == 8 and board[i][column] == None:
            board[i][column] = player[2]
# ◉◎
def print_matrix(lst):
    """A simple function to print a 2 dimentional list elegantly. 
    ◉◎ looks better than X and O so we use these too.
    """
    lst_out = copy.deepcopy(lst)
    for i in range (9):
        for j in range (10):
            if lst_out[i][j] == 'O':
                lst_out[i][j] = '◉'
            elif lst_out[i][j] == 'X':
                lst_out[i][j] = '◎'
            else:
                lst_out[i][j] = ''
    print("1\t2\t3\t4\t5\t6\t7\t8\t9\t10")
    print('\n'.join(['\t'.join([str(i) for i in row]) for row in lst_out]))

def match(b):
    """match is a function to determine if any one of the players has won the game.
    It takes the baord and the location of the last played disk as parameters.
    b for board, val for value
    This function returns True or False:
    True: Someone has won the game
    False: There's currently no one's won the game
    """
    flag = False
    for i in range(8): 
        for j in range(9): 
            val = b[i][j]
            # a = b[i][j+1] == val and b[i-1][j+1] == val and b[i-1][j+2] == val
            # b = b[i][j+1] == val and b[i+1][j+1] == val and b[i+1][j+2] == val
            # c = b[i+1][j] == val and b[i+1][j+1] == val and b[i+2][j+1] == val
            # d = b[i+1][j] == val and b[i+1][j-1] == val and b[i+2][j-1] == val
            if val == None:
                pass
            else:
                if i == 0:
                    if j == 8:
                        if b[i+1][j] == val and b[i+1][j+1] == val and b[i+2][j+1] == val:
                            flag = True
                    else:
                        if ((b[i][j+1] == val and b[i+1][j+1] == val and b[i+1][j+2] == val) or
                        (b[i+1][j] == val and b[i+1][j+1] == val and b[i+2][j+1] == val)):
                            flag = True
                elif i == 7:
                    if j == 8:
                        pass
                    else:
                        if ((b[i][j+1] == val and b[i-1][j+1] == val and b[i-1][j+2] == val) or 
                        (b[i][j+1] == val and b[i+1][j+1] == val and b[i+1][j+2] == val)):
                            flag = True
                elif j == 8:
                    if ((b[i+1][j] == val and b[i+1][j+1] == val and b[i+2][j+1] == val) or 
                    (b[i+1][j] == val and b[i+1][j-1] == val and b[i+2][j-1] == val)):
                        flag = True
                else:
                    if ((b[i][j+1] == val and b[i-1][j+1] == val and b[i-1][j+2] == val) or 
                    (b[i][j+1] == val and b[i+1][j+1] == val and b[i+1][j+2] == val) or 
                    (b[i+1][j] == val and b[i+1][j+1] == val and b[i+2][j+1] == val) or 
                    (b[i+1][j] == val and b[i+1][j-1] == val and b[i+2][j-1] == val)):
                        flag = True
    return flag
def restart_or_quit():
    """restart_or_quit is a function that determines if the player wants to restart the game,
    or quit it. It takes no parameter and returns 0 or 1:
    0 for restart the game
    1 for quit the game
    """
    while True:
        print("Press enter if you want to restart the game,"+
        " and enter 'q' if you want to quit the game!")
        opt = sys.stdin.readline()
        if opt == '\n':
            return 0
        elif opt == "q\n":
            return 1
        else:
            print("This input is invalid.")
def win(player_name, board):
    """win is a function that determines what to do when one player has won the game.
    This function takes 2 parameters:
    player_name: a string that contains the name of the winner.
    board: the chess board that's being currently used
    This function returns 0 or 1:
    0 for restart the game
    1 for quit the game
    """
    os.system('cls')
    print(player_name + " has won the game!")
    print_matrix(board)
    return restart_or_quit()

def a_round(board, player_ls, cnt = 0):
    """a_round is the function where a round of the game starts and iterates
    This function takes 3 parameters:
    board: the chess board that's being currently used
    player_ls: the list of player
    cnt: select which player to start from, default is set to 0
    This function returns 0 or 1:
    0 for restart the game
    1 for quit the game
    """
    someone_win = False
    while not someone_win:
        now = cnt % 2
        os.system('cls')
        print("Now it's " + player_ls[now][1] + "'s turn.")
        print_matrix(board)
        while True:
            raw_cl = input("Please enter the column that you want to play. (If you want to quit, "+
            "please enter 'q'. If you want to restart the game, please enter 'r')\n")
            if raw_cl.isdigit() and int(raw_cl) >= 1 and int(raw_cl) <= 10:
                column = int(raw_cl) - 1
                if is_able_to_drop(column, board):
                    drop_disk(board, column, player_ls[now])
                    print_matrix(board)
                    if match(board):
                        someone_win = True
                        return win(player_ls[now][1], board)
                    break
                else:
                    if is_full(board):
                        print("The chess board is full and no one's won the game.")
                        return restart_or_quit()
                    print("This column is already full, please choose another column.")
            elif raw_cl == 'q':
                return 1
            elif raw_cl == 'r':
                return 0
            else:
                print("Invalid input, please enter a column index between 1 and 10.")
        cnt += 1
    return 1 # exit the program
            
def main():
    """Here to start this module from the console or shell. """
    while True:         # use the while loop to realise the 'restart game' function
        board=[]            # create an empty 9*10 chess board
        for i in range(9): 
            row=[] 
            for j in range(10): 
                row.append(None) 
            board.append(row)
        player_list = [['Player 1', 'Marshall', 'X'], ['Player 2', 'Mathers', 'O']]
        if a_round(board, player_list) == 1:
            break
if __name__ == '__main__':
    main()
