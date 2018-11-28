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

def print_matrix(lst):
    """A simple function to print a 2 dimentional list elegantly. """
    print('\n'.join(['\t'.join([str(i) for i in row]) for row in lst]))


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
