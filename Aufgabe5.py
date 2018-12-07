"""
Aufgabenblatt 5 EPR
Group 11
Author: Liming Kuang -- 6815480, Melanie Wester -- 5613641
Tutor: Felix Lapp

This is a simple python implementation of a modified version of
the game "Connect Four"
"""
import os
import copy
import sys
import random

__author__ = "6815480: Liming Kuang, 5613641: Melanie Wester"
__credits__ = ""
__email__ = "limingkuang@gmail.com, s9108655@stud.uni-frankfurt.de"
# ________________________________________________________________________________________


def cls():
    """cls is a function which clears the screen from the terminal or cmd"""
    os.system('cls' if os.name == 'nt' else 'clear')


def repeat_input(message, min_value, max_value):
    """repeat_input is a function which requests an integer between 2 values from an user.
    clears screen if user chooses values which are not in the requested range"""
    while True:
        player_input = input(message + " >>> ")
        try:
            player_input = int(player_input)
            if min_value <= player_input <= max_value:
                cls()
                print("You chose", player_input)
                return (player_input)
            cls()
            print("This is no valid input.")
        except ValueError:
            cls()
            print("This is no valid input.")


def choose_players():
    """choose_players is a function which creates a list with all participating Players,
    their names and which coin they use"""
    print('\n')
    player_list = []
    number_players = repeat_input("Please enter a number of players between 1 and 2", 1, 2)
    count = 1
    while count <= number_players:
        player_nr = "Player " + str(count)
        player_name = input("Please enter your name " + player_nr + " >>> ")
        cls()
        print(player_nr + ", your name is " + player_name)
        while True:
            keep_name = input("Would you like to keep the name " + player_name + "? y/n >>> ")
            cls()
            keep_name = keep_name.lower()
            if keep_name == "y" or keep_name == "yes":
                player_list.append([player_nr, player_name])
                if count == 1:
                    player_list[0].append('X')
                else:
                    player_list[1].append('O')
                count += 1
                break
            elif keep_name == "n" or keep_name == "no":
                break
            else:
                cls()
                print("This is no valid input")
    cls()
    print(player_list[0][1] + ", your coin is " + player_list[0][2])
    if len(player_list) == 2:
        print(player_list[1][1] + ", your coin is " + player_list[1][2])
    return player_list


def is_full(board):
    """is_full is a function which determines if the chess board is full
    board: the chess board that's being currently used
    This function returns True or False:
    True: this chess board is already full
    False: this chess board is still not full
    """
    for j in range(10):
        if board[0][j] is None:
            return False
    return True


def is_able_to_drop(col, board):
    """is_able_to_drop is a function to check if this column is valid for dropping a disk
    board: the chess board that's being currently used
    col: the index of the list
    """
    if (col < 10 and col >= 0) and board[0][col] is None:
        return True
    else:
        return False


def where_to_drop(board, column):
    """where_to_drop is a function that returns the i in the (i,j) of the point, where the computer could drop the next disk in this column.
    board: the chess board that's being currently used
    column: the column that the computer want to drop the next disk
    """ 
    for i in range(0, 9):
        if i <= 7 and board[i][column] is None and board[i+1][column] is not None:
            return i
        elif i == 8 and board[i][column] is None:
            return i


def to_check_list(board):
    """to_check_list generates a list of coordinates, where the computer should
    be calculating to anticipate the score of each point. It returns a list of tuples.
    board: the chess board that's being currently used
    """
    list_to_check = []
    for i in range (10):            
        list_to_check.append((where_to_drop(board, i),i))
    return list_to_check


def drop_disk(board, column, player):
    """drop_disk is a function to play a disk at the top of a specific column
    This function takes 3 parameters:
    board: the chess board that's being currently used
    column: an int, indicates the column where the user want to drop the disk
    player: a list, that contains information about the current player.
            It has the structure of [str, str, str]
            e.g.:['Player 1', 'Liming', 'X']
    """
    for i in range(0, 9):
        if i <= 7 and board[i][column] is None and board[i + 1][column] is not None:
            board[i][column] = player[2]
        elif i == 8 and board[i][column] is None:
            board[i][column] = player[2]


# ◉◎
def print_matrix(lst):
    """A simple function to print a 2 dimensional list elegantly.
    ◉◎ looks better than X and O so we use these too.
    """
    lst_out = copy.deepcopy(lst)
    for i in range(9):
        for j in range(10):
            if lst_out[i][j] == 'X':
                lst_out[i][j] = '◉'
            elif lst_out[i][j] == 'O':
                lst_out[i][j] = '◯'
            else:
                lst_out[i][j] = '.'
    print("1\t2\t3\t4\t5\t6\t7\t8\t9\t10")
    print('\n'.join(['\t'.join([str(i) for i in row]) for row in lst_out]))


def match(b):
    """match is a function to determine if any one of the players has won the game.
    It takes the board and the location of the last played disk as parameters.
    since if I use board the program is going be too long in each line.
    So I use b for board, val for value.
    This function returns True or False:
    True: Someone has won the game
    False: There is currently no one who has won the game
    """
    flag = False
    for i in range(8):
        for j in range(9):
            val = b[i][j]
            # a = b[i][j+1] == val and b[i-1][j+1] == val and b[i-1][j+2] == val
            # b = b[i][j+1] == val and b[i+1][j+1] == val and b[i+1][j+2] == val
            # c = b[i+1][j] == val and b[i+1][j+1] == val and b[i+2][j+1] == val
            # d = b[i+1][j] == val and b[i+1][j-1] == val and b[i+2][j-1] == val
            if val is None:
                pass
            else:
                if i == 0:  # first line
                    if j == 8:
                        if ((b[i + 1][j] == val and b[i + 1][j + 1] == val and b[i + 2][j + 1] == val) or
                                (b[i + 1][j] == val and b[i + 1][j - 1] == val and b[i + 2][j - 1] == val)):
                            flag = True
                    else:
                        if ((b[i][j + 1] == val and b[i + 1][j + 1] == val and b[i + 1][j + 2] == val) or
                                (b[i + 1][j] == val and b[i + 1][j + 1] == val and b[i + 2][j + 1] == val)):
                            flag = True
                elif i == 7:  # 2nd last line
                    if j == 8:
                        pass
                    else:
                        if ((b[i][j + 1] == val and b[i - 1][j + 1] == val and b[i - 1][j + 2] == val) or
                                (b[i][j + 1] == val and b[i + 1][j + 1] == val and b[i + 1][j + 2] == val)):
                            flag = True
                elif i == 8:
                    if j == 8:
                        pass
                    else:
                        if (b[i][j+1] == val and b[i-1][j+1] == val and b[i-1][j+2] == val):
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
        print('\n')
        print("Press enter if you want to restart the game and enter 'q' if you want to quit the game!")
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
    cls()
    print_matrix(board)
    print(player_name + " has won the game!")
    return restart_or_quit()


def a_round(board, player_ls, cnt=0):
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
        print_matrix(board)
        print('\n')
        if len(player_ls) == 1 and now == 1:        # if there is just one Player and its time for Player two -> KI makes a move
            player_ls.append(["Player 2", "Computer", 'O'])         # -------->> not the right place here, but: implement that if the computer has a 0 he should prefer it instead of the 0 of other player
            player_ls, cnt, column = ki_turn(board, player_ls[now][2], player_ls[0][2], player_ls, now, cnt, someone_win) # ------> problem if i want to restart after played against computer
            cls()
            print("The Computer has chosen column ", column + 1, " !")
            print('\n')
        else:
            print("Now it's " + player_ls[now][1] + "'s turn.")
            print('\n')
            while True:
                raw_cl = input("(To quit enter: 'q'. To restart enter: 'r')" +
                "\n\nPlease enter the column that you want to play >>> ")
                if raw_cl.isdigit() and int(raw_cl) >= 1 and int(raw_cl) <= 10:
                    column = int(raw_cl) - 1
                    if is_able_to_drop(column, board):
                        drop_disk(board, column, player_ls[now])
                        print_matrix(board)
                        if match(board):
                            someone_win = True
                            cls()
                            return win(player_ls[now][1], board)
                        cls()
                        break
                    else:
                        if is_full(board):
                            print("The chess board is full and no one's won the game.")
                            return restart_or_quit()
                        cls()
                        print("This column is already full, please choose another column.")
                elif raw_cl == 'q':
                    return 1
                elif raw_cl == 'r':
                    return 0
                else:
                    cls()
                    print_matrix(board)
                    print("Invalid input, please enter a column index between 1 and 10.")
            cnt += 1
    return 1  # exit the program


def fig1_1(work_b, color, color_other, i, j):
    """fig 1_1 is a function which calculates the score of a field for fig 1_1.
    it considers if row = 0 or column = (9 or 8) or there is the color of the other player in this 
    figure or there is no coin in (i,j+2) to achieve this figure"""                                                                    
    if i == 0 or j == 9 or j == 8 or ((work_b[i][j+1] or work_b[i-1][j+1] or work_b[i-1][j+2]) == color_other) or (work_b[i][j+2] is None):
        pass
    else:
        fig1_1 = [work_b[i][j+1], work_b[i-1][j+1], work_b[i-1][j+2]]
        sub = fig1_1.count(color)
        score = 3 - sub
        return score
        

def fig1_2(work_b, color, color_other, i, j):
    """fig 1_2 is a function which calculates the score of a field for fig 1_2.
    it considers if row = 8 or column = (0 or 9) or there is the color of the other player in this 
    figure or there is no coin in (i+1, j+1) to achieve this figure"""
    if i == 8 or j == 0 or j == 9 or ((work_b[i][j+1] or work_b[i+1][j] or work_b[i+1][j-1]) == color_other) or (work_b[i+1][j+1] is None):
        pass
    else:
        fig1_2 = [work_b[i][j+1], work_b[i+1][j], work_b[i+1][j-1]]
        sub = fig1_2.count(color)
        score = 3 - sub
        return score


def fig1_3(work_b, color, color_other, i, j):
    """fig 1_3 is a function which calculates the score of a field for fig 1_3.
    it considers if row = 8 or column = (0 or 1) or there is the color of the other player in this figure"""
    if i == 8 or j == 0 or j == 1 or ((work_b[i][j-1] or work_b[i+1][j-1] or work_b[i+1][j-2]) == color_other):
        pass
    else:
        fig1_3 = [work_b[i][j-1], work_b[i+1][j-1], work_b[i+1][j-2]]
        sub = fig1_3.count(color)
        score = 3 - sub
        return score


def fig1_4(work_b, color, color_other, i, j):
    """fig 1_4 is a function which calculates the score of a field for fig 1_4.
    it considers if row = 0 or column = (0 or 9) or there is the color of the other player in this
    figure or there is no coin in (i, j+1) to achieve this figure"""
    if i == 0 or j == 0 or j == 9 or ((work_b[i][j-1] or work_b[i-1][j+1]) == color_other) or (work_b[i][j+1] is None):
        pass
    else:
        fig1_4 = [work_b[i][j-1], work_b[i-1][j+1]]
        sub = fig1_4.count(color)
        score = 3 - sub
        return score


def fig2_1(work_b, color, color_other, i, j):
    """fig 2_1 is a function which calculates the score of a field for fig 2_1.
    it considers if row = 8 or column = (8 or 9) or there is the color of the other player in this figure"""
    if i == 8 or j == 8 or j == 9 or ((work_b[i][j+1] or work_b[i+1][j+1] or work_b[i+1][j+2]) == color_other):
        pass
    else:
        fig2_1 = [work_b[i][j+1], work_b[i+1][j+1], work_b[i+1][j+2]]
        sub = fig2_1.count(color)
        score = 3 - sub
        return score


def fig2_2(work_b, color, color_other, i, j):
    """fig 2_2 is a function which calculates the score of a field for fig 2_2.
    it considers if row = 8 or column = (0 or 9) or there is the color of the other player in this 
    figure or there is no coin in (i+1, j-1) to achieve this figure"""
    if i == 8 or j == 0 or j == 9 or ((work_b[i][j-1] or work_b[i+1][j] or work_b[i+1][j+1]) == color_other) or (work_b[i+1][j-1] is None):
        pass
    else:
        fig2_2 = [work_b[i][j-1], work_b[i+1][j], work_b[i+1][j+1]]
        sub = fig2_2.count(color)
        score = 3 - sub
        return score
    

def fig2_3(work_b, color, color_other, i, j):
    """fig 2_3 is a function which calculates the score of a field for fig 2_3.
    it considers if row = 0 or column = (0 or 9) or there is the color of the other player in this
    figure or there is no coin in (i, j-1) to achieve this figure"""
    if i == 0 or j == 0 or j == 9 or ((work_b[i][j+1] or work_b[i-1][j-1]) == color_other) or (work_b[i][j-1] is None):
        pass
    else:
        fig2_3 = [work_b[i][j+1], work_b[i-1][j-1]]
        sub = fig2_3.count(color)
        score = 3 - sub
        return score


def fig2_4(work_b, color, color_other, i, j):
    """fig 2_4 is a function which calculates the score of a field for fig 2_4.
    it considers if row = 0 or column = (0 or 1) or there is the color of the other player in this 
    figure or there is no coin in (i, j-2) to achieve this figure"""
    if i == 0 or j == 0 or j == 1 or ((work_b[i][j-1] or work_b[i-1][j-1] or work_b[i-1][j-2]) == color_other) or (work_b[i][j-2] is None):
        pass
    else:
        fig2_4 = [work_b[i][j-1], work_b[i-1][j-1], work_b[i-1][j-2]]
        sub = fig2_4.count(color)
        score = 3 - sub
        return score


def fig3_1(work_b, color, color_other, i, j):
    """fig 3_1 is a function which calculates the score of a field for fig 3_1.
    it considers if row = (0 or 1) or column = 9 or there is the color of the other player in this 
    figure or there is no coin in (i, j+1) to achieve this figure"""
    if i == 0 or i == 1 or j == 9 or ((work_b[i-1][j+1] or work_b[i-2][j+1]) == color_other) or (work_b[i][j+1] is None):
        pass
    else:
        fig3_1 = [work_b[i-1][j+1], work_b[i-2][j+1]]
        sub = fig3_1.count(color)
        score = 3 - sub
        return score


def fig3_2(work_b, color, color_other, i, j):
    """fig 3_2 is a function which calculates the score of a field for fig 3_2.
    it considers if row = (0 or 8) or column = 9 or there is the color of the other player in this 
    figure or there is no coin in (i+1, j+1) to achieve this figure"""
    if i == 0 or i == 8 or j == 9 or ((work_b[i+1][j] or work_b[i][j+1] or work_b[i-1][j+1]) == color_other) or (work_b[i+1][j+1] is None):
        pass
    else:
        fig3_2 = [work_b[i+1][j], work_b[i][j+1], work_b[i-1][j+1]]
        sub = fig3_2.count(color)
        score = 3 - sub
        return score


def fig3_3(work_b, color, color_other, i, j):
    """fig 3_3 is a function which calculates the score of a field for fig 3_3.
    it considers if row = (0 or 8) or column = 0 or there is the color of the other player in this figure"""
    if i == 0 or i == 8 or j == 0 or ((work_b[i][j-1] or work_b[i+1][j-1]) == color_other):
        pass
    else:
        fig3_3 = [work_b[i][j-1], work_b[i+1][j-1]]
        sub = fig3_3.count(color)
        score = 3 - sub
        return score


def fig3_4(work_b, color, color_other, i, j):
    """fig 3_4 is a function which calculates the score of a field for fig 3_4.
    it considers if row = (7 or 8) or column = 0 or there is the color of the other player in this figure"""
    if i == 7 or i == 8 or j == 0 or ((work_b[i+1][j] or work_b[i+1][j-1] or work_b[i+2][j-1]) == color_other):
        pass
    else:
        fig3_4 = [work_b[i+1][j], work_b[i+1][j-1], work_b[i+2][j-1]]
        sub = fig3_4.count(color)
        score = 3 - sub
        return score


def fig4_1(work_b, color, color_other, i, j):
    """fig 4_1 is a function which calculates the score of a field for fig 4_1.
    it considers if row = (7 or 8) or column = 9 or there is the color of the other player in this figure"""
    if i == 7 or i == 8 or j == 9 or ((work_b[i+1][j] or work_b[i+1][j+1] or work_b[i+2][j+1]) == color_other):
        pass
    else:
        fig4_1 = [work_b[i+1][j], work_b[i+1][j+1], work_b[i+2][j+1]]
        sub = fig4_1.count(color)
        score = 3 - sub
        return score


def fig4_2(work_b, color, color_other, i, j):
    """fig 4_2 is a function which calculates the score of a field for fig 4_2.
    it considers if row = (0 or 8) or column = 9 or there is the color of the other player in this figure"""
    if i == 0 or i == 8 or j == 9 or ((work_b[i][j+1] or work_b[i+1][j+1]) == color_other):
        pass
    else:
        fig4_2 = [work_b[i][j+1], work_b[i+1][j+1]]
        sub = fig4_2.count(color)
        score = 3 - sub
        return score


def fig4_3(work_b, color, color_other, i, j):
    """fig 4_3 is a function which calculates the score of a field for fig 4_3.
    it considers if row = (0 or 8) or column = 0 or there is the color of the other player in this 
    figure or there is no coin in (i+1, j-1) to achieve this figure"""
    if i == 0 or i == 8 or j == 0 or ((work_b[i+1][j] or work_b[i][j-1] or work_b[i-1][j-1]) == color_other) or (work_b[i+1][j-1] is None):
        pass
    else:
        fig4_3 = [work_b[i+1][j], work_b[i][j-1], work_b[i-1][j-1]]
        sub = fig4_3.count(color)
        score = 3 - sub
        return score


def fig4_4(work_b, color, color_other, i, j):
    """fig 4_4 is a function which calculates the score of a field for fig 4_4.
    it considers if row = (0 or 1) or column = 0 or there is the color of the other player in this 
    figure or there is no coin in (i, j-1) to achieve this figure"""
    if i == 0 or i == 1 or j == 0 or ((work_b[i-1][j-1] or work_b[i-2][j-1]) == color_other) or (work_b[i][j-1] is None):
        pass
    else:
        fig4_4 = [work_b[i-1][j-1], work_b[i-2][j-1]]
        sub = fig4_4.count(color)
        score = 3 - sub
        return score
    

def score_fields(board, color, color_other):
    """score_fields is a function that generates a list of scores on each point, 
    where is possible to be played in the next round for the computer or player.
    color: is either 'X' or 'O', which indicates which player we are currently conducting
    the anticipation algorithm on.
    board: the chess board that's being currently used
    """
    list_to_check = to_check_list(board)
    for (i, j) in list_to_check:
        if i == None:
            list_to_check.remove((i,j))
    list_of_score = [None] * 10

    work_b = copy.deepcopy(board)
    for (i, j) in list_to_check:
        scores_all_ij = []       # collects all scores (for each possible figure) on ONE field where I am able to drop a coin
        # scores for KI
        scores_fig1 = [fig1_1(work_b, color, color_other, i, j), fig1_2(work_b, color, color_other, i, j), fig1_3(work_b, color, color_other, i, j), fig1_4(work_b, color, color_other, i, j)]
        scores_fig2 = [fig2_1(work_b, color, color_other, i, j), fig2_2(work_b, color, color_other, i, j), fig2_3(work_b, color, color_other, i, j), fig2_4(work_b, color, color_other, i, j)]
        scores_fig3 = [fig3_1(work_b, color, color_other, i, j), fig3_2(work_b, color, color_other, i, j), fig3_3(work_b, color, color_other, i, j), fig3_4(work_b, color, color_other, i, j)]
        scores_fig4 = [fig4_1(work_b, color, color_other, i, j), fig4_2(work_b, color, color_other, i, j), fig4_3(work_b, color, color_other, i, j), fig4_4(work_b, color, color_other, i, j)]
        
        scores_all_ij.extend(scores_fig1)
        scores_all_ij.extend(scores_fig2)
        scores_all_ij.extend(scores_fig3)
        scores_all_ij.extend(scores_fig4)

        # scores for Player
        scores_fig1 = [fig1_1(work_b, color_other, color, i, j), fig1_2(work_b, color_other, color, i, j), fig1_3(work_b, color_other, color, i, j), fig1_4(work_b, color_other, color, i, j)]
        scores_fig2 = [fig2_1(work_b, color_other, color, i, j), fig2_2(work_b, color_other, color, i, j), fig2_3(work_b, color_other, color, i, j), fig2_4(work_b, color_other, color, i, j)]
        scores_fig3 = [fig3_1(work_b, color_other, color, i, j), fig3_2(work_b, color_other, color, i, j), fig3_3(work_b, color_other, color, i, j), fig3_4(work_b, color_other, color, i, j)]
        scores_fig4 = [fig4_1(work_b, color_other, color, i, j), fig4_2(work_b, color_other, color, i, j), fig4_3(work_b, color_other, color, i, j), fig4_4(work_b, color_other, color, i, j)]
        
        scores_all_ij.extend(scores_fig1)
        scores_all_ij.extend(scores_fig2)
        scores_all_ij.extend(scores_fig3)
        scores_all_ij.extend(scores_fig4)

        scores_all_ij = [index for index in scores_all_ij if index is not None]
        scores_all_ij.sort()
        print("scores_all_ij:", scores_all_ij)      # TESTING
        if scores_all_ij != []:
            rating_field = [scores_all_ij[0], scores_all_ij.count(scores_all_ij[0])]    # takes lowest score and how many times a field contains it
        else:
            rating_field = [5, 5]         # if there are no scores for a field
        list_of_score[j] = rating_field
        print("rating field:", rating_field) # TESTING
        print("list of score:", list_of_score) # TESTING
    return list_of_score    # rates every possible field by its lowest score and how many times a field contains this score


def choose_column(board, color, color_other):
    """choose_column is a function to determine in which column should the computer play next.
    It returns an int, which is the column.
    board: the chess board that's being currently used
    """
    list_of_score = score_fields(board, color, color_other)
    check_list_of_score = copy.deepcopy(list_of_score)
    count = 0
    for index in check_list_of_score:
        if index == None:
            check_list_of_score[count] = [1000, 1000]
        count += 1
    check_list_of_score.sort()

    position_1 = 0
    position_2 = 1

    while True:
        for index in check_list_of_score:
            print("index:", index)
            if position_2 < 10:
                if check_list_of_score[position_1][0] == check_list_of_score[position_2][0]:
                    position_2 += 1
                else:
                    break
        best_score = check_list_of_score[:position_2][::-1][0]  # best score from every field on the board
        break

    choose_column = []
    column = 0
    while True:
        for index in list_of_score:
            if index == best_score:
                choose_column.append(column)    # checks where best score with highest amount is located
                column += 1
            else:
                column += 1
        break
    if len(choose_column) > 1:
        return random.choice(choose_column) # if there is more than one best score with highest amount it chooses randomly
    else:
        return choose_column[0]

def ki_turn(board, color, color_other, player_ls, now, cnt, someone_win):
    """ki_turn is a function which lets the KI make a move when its her turn"""
    column = choose_column(board, color, color_other)          
    drop_disk(board, column, player_ls[now])
    print_matrix(board)
    if match(board):
        someone_win = True
        return win(player_ls[now][1], board)
    else:
        del player_ls[1]
        cnt += 1
        return player_ls, cnt, column


def main():
    """Here to start this module from the console or shell. """
    player_list = choose_players()  # gives a list with players name and which coin they uses
    while True:  # use the while loop to realise the 'restart game' function
        board = []  # create an empty 9*10 chess board
        for i in range(9):
            row = []
            for j in range(10):
                row.append(None)
            board.append(row)
        # player_list = [['Player 1', 'Marshall', 'X'], ['Player 2', 'Mathers', 'O']]  # Testing
        if a_round(board, player_list) == 1:
            break


if __name__ == '__main__':
    main()

'''
SOURCES:
http://www.lojol.de/html/4gewinnt.html
https://www.youtube.com/watch?v=XOga3EhS59c
'''
