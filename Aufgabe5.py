"""
Aufgabenblatt 5 EPR
Group 11
Author: Liming Kuang -- 6815480, Melanie Wester -- 5613641
Tutor: Felix Lapp

This is a simple python implementation of a modofied version of 
the game "Connect Four"
"""
import numpy as np
#from math import sqrt, log, e  #an example for modules from the standard bib
#from numpy import array       #another example for third party module
#import meinmodul              #example for your own module

__author__ = "6815480: Liming Kuang, 5613641: Melanie Wester"  
__credits__ = "" 
__email__ = "limingkuang@gmail.com, s9108655@stud.uni-frankfurt.de"

def is_full(board):
    """is_full is a function which determines if the chess board is full"""
    for j in range(10):
        if board[0][j] == None:
            return False
    return True
    
def is_able_to_drop(col, board):
    """is_able_to_drop is a function to check if this column is valid for dropping a disk
    The col here is the index of the list
    """
    if (col < 10 and col >= 0) and board[0][col] == None:
        return True
    else:
        return False

def drop_disk(board, column, player):
    """drop_disk is a function to play a disk at the top of a specific column"""
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
def a_round(board, player_ls, cnt):
    """a_round is the function where a round of the game starts and iterates"""
    someone_win = False
    while not someone_win:
        now = cnt % 2
        os.system('cls')
        print("Now it's " + player_ls[now][1] + "'s turn.")
        print_matrix(board)
        while True:
            raw_cl = input("Please enter the column that you want to play: ")
            if raw_cl.isdigit() and int(raw_cl) >= 1 and int(raw_cl) <= 10:
                column = int(raw_cl) - 1
                if is_able_to_drop(column, board):
                    drop_disk(board, column, player_ls[now])
                    print_matrix(board)
                    if match(board):
                        print(player_ls[now][1] + " has won the game!")
                        someone_win = True
                    break
                else:
                    if is_full(board):
                        print("The chess board is full and no one's won the game. Press enter to restart.")
                    print("This column is already full, please choose another column.")

            else:
                print("Invalid input, please enter a column index between 1 and 10.")
        cnt += 1
            
def main():
    """Here to start this module from the console or shell. """
    board=[]            # create an empty 9*10 chess board
    for i in range(9): 
        row=[] 
        for j in range(10): 
            row.append(None) 
        board.append(row) 
    player_list = [['Player 1', 'Marshall', 'X'], ['Player 2', 'Mathers', 'O']] # just for testing
    a_round(board, player_list, 0)
if __name__ == '__main__':
    main()
