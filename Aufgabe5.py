"""
Aufgabenblatt 5 EPR
Group 11
Author: Liming Kuang -- 6815480, Melanie Wester -- 5613641
Tutor: Felix Lapp

This is a simple python implementation of a modified version of 
the game "Connect Four"
"""
import os, copy, sys

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
                print("You chose", player_input)
                return (player_input)
            cls()
            # print("Please enter an integer between " + str(min_value) + " and " + str(max_value) + ". ")
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
            keep_name = keep_name.lower()
            if keep_name == "y":
                player_list.append([player_nr, player_name])
                if count == 1:
                    player_list[0].append('X')
                else:
                    player_list[1].append('O')
                count += 1
                break
            elif keep_name == "n":
                break
            else:
                cls()
                print("This is no valid input")
    if len(player_list) == 1:
        player_list.append(["Player 2", "Computer", 'O'])
    cls()
    print(player_list[0][1] + ", your coin is " + player_list[0][2])
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

    
def where_to_drop(board, column):
    """It returns the i in the (i,j) where the Player would be able to drop next""" 
    for i in range (0,9):
        if i <= 7 and board[i][column] == None and board[i+1][column] != None:
            return i
        elif i == 8 and board[i][column] == None:
            return i

        
def to_check_list(board):
    """It returns every (i,j) where the Computer would
    be able to drop next"""
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
    since if I use board the programm's gonna be too long in each line. 
    So I use b for board, val for value.
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
                if i == 0: # first line
                    if j == 8:
                        if ((b[i+1][j] == val and b[i+1][j+1] == val and b[i+2][j+1] == val) or
                        (b[i+1][j] == val and b[i+1][j-1] == val and b[i+2][j-1] == val)):
                            flag = True
                    else:
                        if ((b[i][j+1] == val and b[i+1][j+1] == val and b[i+1][j+2] == val) or
                        (b[i+1][j] == val and b[i+1][j+1] == val and b[i+2][j+1] == val)):
                            flag = True
                elif i == 7: # 2nd last line
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
    cls()
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
        cls()
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


def ways_have_gone(color, board):
    """ways_have_gone is a function for the KI which scores each field (i,j) based on
    how many coins are left to make a win"""
    list_to_check = to_check_list(board)
    list_of_score = [None] * 10

    work_b = copy.deepcopy(board)
    for i in work_b:
        i.insert(0, None)
        i.insert(0, None)
        i.append(None)
        i.append(None)
    for (x,y) in list_to_check:
        i = x
        j = y + 2 
        score = 3
        if work_b[i][j-1] != color and work_b[i][j+1] != color: # nothing on left and right side
            if i == 8:
                pass
            elif work_b[i+1][j] == color:
                score -= 1
                if work_b[i+1][j-1] == color or work_b[i+1][j+1] == color:
                    score -= 1
                    if i == 7:
                        pass
                    elif ((work_b[i+1][j-1] == color and work_b[i+2][j-1] == color) or
                    (work_b[i+1][j-1] == color and work_b[i+2][j-1] == color)):
                        score =- 1
        elif work_b[i][j-1] == color: # there is a match to the left
            score -= 1
            if i == 8:
                if work_b[i-1][j-1] == color:
                    score -= 1
                    if work_b[i-1][j-2] == color:
                        score -= 1
            elif work_b[i+1][j-1] == color:     # Fig 1
                score -= 1
                if work_b[i+1][j-2] == color:
                    score -= 1
            elif work_b[i+1][j] == color:       # Fig 2
                score -= 1
                if work_b[i+1][j+1] == color:
                    score -= 1
            elif (work_b[i+1][j] == color) or (work_b[i-1][j-1] == color):      # Fig 3
                score -= 1
                if (work_b[i+1][j] == color) and (work_b[i-1][j-1] == color):
                    score -= 1
        elif work_b[i][j+1] == color: # there is a match to the right
            score -= 1
            if i == 8:
                if work_b[i-1][j+1] == color:
                    score -= 1 
                    if work_b[i-1][j+2] == color:
                        score -= 1
            elif work_b[i-1][j+1] == color:     # Fig 1_1
                score -= 1 
                if work_b[i-1][j+2] == color:
                    score -= 1
            elif work_b[i+1][j] == color:       # Fig 1_2
                score -= 1
                if work_b[i+1][j-1] == color:
                    score -= 1
            elif work_b[i+1][j+1] == color:
                score -= 1
                if work_b[i+1][j+2] == color:
                    score -= 1
            elif work_b[i+1][j] == color or work_b[i-1][j+1]:
                score -= 1
                if work_b[i+1][j] == color and work_b[i-1][j+1]:
                    score -= 1
        list_of_score[y] = score    
    return list_of_score     
    
    
def main():
    """Here to start this module from the console or shell. """
    player_list = choose_players()  # gives a list with players name and which coin they uses
    while True:         # use the while loop to realise the 'restart game' function
        board=[]            # create an empty 9*10 chess board
        for i in range(9): 
            row=[] 
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
