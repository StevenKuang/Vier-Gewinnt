"""
Aufgabenblatt 5 EPR
Group 11
Author: Liming Kuang -- 6815480, Melonie
Tutor: Felix Lapp

This is a simple python implementation of a modofied version of 
the game "Connect Four"
"""
import numpy as np
#from math import sqrt, log, e  #an example for modules from the standard bib
#from numpy import array       #another example for third party module
#import meinmodul              #example for your own module

TEST HIHIHIHIH STEVEN KUANG

__author__ = "6815480: Liming Kuang, 654321: Terry Gilliam"  
__credits__ = "" 
__email__ = "limingkuang@gmail.com, "

def print_matrix(lst):
    """A simple function to print a 2 dimentional list elegantly. """
    print('\n'.join(['   '.join([str(i) for i in row]) for row in lst]))


def match(board):
    """match is a function to determine if any one of the players has won the game.
    It takes the baord and the location of the last played disk as parameters.
    """
    flag = False
    for i in range(9): 
        for j in range(10): 
            color = board[i][j]

    if board[i][j+1] != color and board[i][j-1] != color:
        if (board[i+1][j] == color and board[i+1][j+1] == color and board[i+2][j+1] == color) or
        ((board[i+1][j] == color and board[i+1][j-1] == color and board[i+2][j-1] == color)):
            return 1
        else:
            return 0
    else:

        
            

def main():
    """Here to start this module from the console or shell. """
    board=[]            # create an empty 9*10 chess board
    for i in range(9): 
        row=[] 
        for j in range(10): 
            row.append(None) 
        board.append(row) 
    print_matrix(board)
if __name__ == '__main__':
    main()
