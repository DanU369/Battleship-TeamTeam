import copy
import sys
import os
import subprocess
import time

def cover():
    print(
        '''
 ______     ______     ______   ______   __         ______     ______     __  __     __     ______  
/\  __ \   /\  __ \   /\__  _\ /\__  _\ /\ \       /\  ___\   /\  ___\   /\ \_\ \   /\ \   /\  __ \ 
\ \  __<   \ \  __ \  \/_/\ \/ \/_/\ \/ \ \ \____  \ \  __\   \ \___  \  \ \  __ \  \ \ \  \ \  __/ 
 \ \_____\  \ \_\ \_\    \ \_\    \ \_\  \ \_____\  \ \_____\  \/\_____\  \ \_\ \_\  \ \_\  \ \_\   
  \/_____/   \/_/\/_/     \/_/     \/_/   \/_____/   \/_____/   \/_____/   \/_/\/_/   \/_/   \/_/   
                                                                                                    
                                                  # #  ( )                                          
                                               ___#_#___|__                                         
                                           _  |____________|  _                                     
                                    _=====| | |            | | |==== _                              
                              =====| |.---------------------------. | |====                         
                <--------------------'   .  .  .  .  .  .  .  .   '--------------/                  
                  \                                                             /                   
                   \___________________________________________________________/                    
               wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww                
             wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww               
                wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww                 
''')

def sound(sound_duration):
    if sound_duration == 'long':
        duration = 0.9  # seconds
        freq = 300  # Hz
        os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
    else:
        duration = 0.08  # seconds
        freq = 460  # Hz
        os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))

    
def print_radars(player, tries_1_list, tries_2_list):

    if player == 1:
        print("      *****PLAYER {} IT'S YOUR TURN*****".format(player))
    if player == 2:
        print("                                            *****PLAYER {} IT'S YOUR TURN*****".format(player))
    print('''
                    1   2   3   4   5                     1   2   3   4   5
                    
                A   {}   {}   {}   {}   {}                 A   {}   {}   {}   {}   {}
                
                B   {}   {}   {}   {}   {}                 B   {}   {}   {}   {}   {}
                
                C   {}   {}   {}   {}   {}                 C   {}   {}   {}   {}   {}
                
                D   {}   {}   {}   {}   {}                 D   {}   {}   {}   {}   {}
                
                E   {}   {}   {}   {}   {}                 E   {}   {}   {}   {}   {}
                
                '''.format(tries_1_list[0][0], tries_1_list[0][1], tries_1_list[0][2], tries_1_list[0][3], tries_1_list[0][4], tries_2_list[0][0], tries_2_list[0][1], tries_2_list[0][2], tries_2_list[0][3], tries_2_list[0][4], tries_1_list[1][0], tries_1_list[1][1], tries_1_list[1][2], tries_1_list[1][3], tries_1_list[1][4], tries_2_list[1][0], tries_2_list[1][1], tries_2_list[1][2], tries_2_list[1][3], tries_2_list[1][4], tries_1_list[2][0], tries_1_list[2][1], tries_1_list[2][2], tries_1_list[2][3], tries_1_list[2][4], tries_2_list[2][0], tries_2_list[2][1], tries_2_list[2][2], tries_2_list[2][3], tries_2_list[2][4], tries_1_list[3][0], tries_1_list[3][1], tries_1_list[3][2], tries_1_list[3][3], tries_1_list[3][4], tries_2_list[3][0], tries_2_list[3][1], tries_2_list[3][2], tries_2_list[3][3], tries_2_list[3][4], tries_1_list[4][0], tries_1_list[4][1], tries_1_list[4][2], tries_1_list[4][3], tries_1_list[4][4], tries_2_list[4][0], tries_2_list[4][1], tries_2_list[4][2], tries_2_list[4][3], tries_2_list[4][4]))

def init_list():

    init_board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
        0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    return init_board


def print_board(board):

    print('''
                1   2   3   4    5
                
            A   {}   {}   {}   {}    {}
            
            B   {}   {}   {}   {}    {}
            
            C   {}   {}   {}   {}    {}
            
            D   {}   {}   {}   {}    {}
            
            E   {}   {}   {}   {}    {}
        '''.format(board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[1][0], board[1][1], board[1][2],
                   board[1][3], board[1][4], board[2][0], board[2][1], board[2][2], board[2][3], board[2][4],
                   board[3][0], board[3][1], board[3][2], board[3][3], board[3][4],
                   board[4][0], board[4][1], board[4][2], board[4][3], board[4][4]))

def verificare_placement(placement_list, row, col):
    if row == 0 and col == 0:
        if placement_list[1][0] == placement_list[0][1] == placement_list[0][0] == 0:
            return True
        else:
            return False
    if row == 0 and col == 4:
        if placement_list[0][3] == placement_list[1][4] == placement_list[0][4] == 0:
            return True
        else:
            return False
    if row == 4 and col == 4:
        if placement_list[4][3] == placement_list[3][4] == placement_list[4][4] == 0:
            return True
        else:
            return False
    if row == 4 and col == 0:
        if placement_list[3][0] == placement_list[4][1] == placement_list[4][0] == 0:
            return True
        else:
            return False
    if row == 4:
        if placement_list[row-1][col] == placement_list[row][col+1] == placement_list[row][col-1] == placement_list[row][col] == 0:
            return True
        else:
            return False
    elif col == 4:
        if placement_list[row+1][col] == placement_list[row-1][col] == placement_list[row][col-1] == placement_list[row][col] == 0:
            return True
        else:
            return False
    elif row == 0:
        if placement_list[row+1][col] == placement_list[row][col+1] == placement_list[row][col-1] == placement_list[row][col] == 0:
            return True
        else:
            return False
    elif col == 0:
        if placement_list[row+1][col] == placement_list[row-1][col] == placement_list[row][col+1] == placement_list[row][col] == 0:
            return True
        else:
            return False
    elif placement_list[row+1][col] == placement_list[row-1][col] == placement_list[row][col+1] == placement_list[row][col-1] == placement_list[row][col] == 0:
        return True
    else:
        return False


def placement1(placement1_list):
    shipsx1 = 3
    shipsx2 = 2
    while shipsx1 > 0:
        print_board(placement1_list)
        ships = shipsx1 + shipsx2
        print("Player 1, you have {} ships left to place".format(ships))
        print("Now you should place a 1 block ship")
        place = str(
            input("Choose a position to place your ship: ").lower())
        if place[0] in ["a", "b", "c", "d", "e"] and place[1] in ["1", "2", "3", "4", "5"] and len(place) == 2:
            row = ord(place[0])-97
            col = int(place[1])-1
            verificare_placement(placement1_list, row, col)
            if verificare_placement(placement1_list, row, col) == True:
                placement1_list[row][col] = "X"
                shipsx1 -= 1
            elif verificare_placement(placement1_list, row, col) == False:
                os.system("clear")
                print("Your ships are too close")
                continue
            os.system("clear")
        else:
            os.system("clear")
            print("Invalid input!")
            continue
    while shipsx2 > 0:
        print_board(placement1_list)
        ships = shipsx1 + shipsx2
        print("Player 1, you have {} ships left to place".format(ships))
        print("Now you should place a 2 blocks ship")
        place = str(
            input("Choose a position to place your ship's head: ").lower())
        if place[0] in ["a", "b", "c", "d", "e"] and place[1] in ["1", "2", "3", "4", "5"] and len(place) == 2:
            row = ord(place[0])-97
            col = int(place[1])-1
            verificare_placement(placement1_list, row, col)
            if verificare_placement(placement1_list, row, col) == True:
                direction = input(
                    "Choose on which direction you want to place your ship (N,S,E,W) :").lower()
                if direction in ["n", "s", "e", "w"]:
                    if direction == "n":
                        if row == 0:
                            os.system("clear")
                            print(
                                "In this case the world is flat and you can't cross the edges")
                            continue
                        verificare_placement(placement1_list, row-1, col)
                        if verificare_placement(placement1_list, row-1, col) == True:
                            placement1_list[row][col] = "X"
                            placement1_list[row-1][col] = "X"
                            shipsx2 -= 1
                            os.system("clear")
                        elif verificare_placement(placement1_list, row-1, col) == False:
                            os.system("clear")
                            print("Your ships are too close!")
                            continue
                    if direction == "s":
                        if row == 4:
                            os.system("clear")
                            print(
                                "In this case the world is flat and you can't cross the edges")
                            continue
                        verificare_placement(placement1_list, row+1, col)
                        if verificare_placement(placement1_list, row+1, col) == True:
                            placement1_list[row][col] = "X"
                            placement1_list[row+1][col] = "X"
                            shipsx2 -= 1
                            os.system("clear")
                        elif verificare_placement(placement1_list, row+1, col) == False:
                            os.system("clear")
                            print("Your ships are too close!")
                            continue
                    if direction == "e":
                        if col == 4:
                            os.system("clear")
                            print(
                                "In this case the world is flat and you can't cross the edges")
                            continue
                        verificare_placement(placement1_list, row, col+1)
                        if verificare_placement(placement1_list, row, col+1) == True:
                            placement1_list[row][col] = "X"
                            placement1_list[row][col+1] = "X"
                            shipsx2 -= 1
                            os.system("clear")
                        elif verificare_placement(placement1_list, row, col+1) == False:
                            os.system("clear")
                            print("Your ships are too close!")
                            continue
                    if direction == "w":
                        if col == 0:
                            os.system("clear")
                            print(
                                "In this case the world is flat and you can't cross the edges")
                            continue
                        verificare_placement(placement1_list, row, col-1)
                        if verificare_placement(placement1_list, row, col-1) == True:
                            placement1_list[row][col] = "X"
                            placement1_list[row][col-1] = "X"
                            shipsx2 -= 1
                            os.system("clear")
                        elif verificare_placement(placement1_list, row, col-1) == False:
                            os.system("clear")
                            print("Your ships are too close!")
                            continue
                else:
                    os.system("clear")
                    print("Invalid input!")
                    continue
            elif verificare_placement(placement1_list, row, col) == False:
                os.system("clear")
                print("Your ships are too close")
                continue
        else:
            os.system("clear")
            print("Invalid input!")
            continue
    return placement1_list

def placement2(placement2_list):
    shipsx1 = 3
    shipsx2 = 2
    while shipsx1 > 0:
        print_board(placement2_list)
        ships = shipsx1 + shipsx2
        print("Player 2, you have {} ships left to place".format(ships))
        print("Now you should place a 1 block ship")
        place = str(
            input("Choose a position to place your ship: ").lower())
        if place[0] in ["a", "b", "c", "d", "e"] and place[1] in ["1", "2", "3", "4", "5"] and len(place) == 2:
            row = ord(place[0])-97
            col = int(place[1])-1
            verificare_placement(placement2_list, row, col)
            if verificare_placement(placement2_list, row, col) == True:
                placement2_list[row][col] = "X"
                shipsx1 -= 1
            elif verificare_placement(placement2_list, row, col) == False:
                os.system("clear")
                print("Your ships are too close")
                continue
            os.system("clear")
        else:
            os.system("clear")
            print("Invalid input!")
            continue

    while shipsx2 > 0:
        print_board(placement2_list)
        ships = shipsx1 + shipsx2
        print("Player 2, you have {} ships left to place".format(ships))
        print("Now you should place a 2 blocks ship")
        place = str(
            input("Choose a position to place your ship's head: ").lower())
        if place[0] in ["a", "b", "c", "d", "e"] and place[1] in ["1", "2", "3", "4", "5"] and len(place) == 2:
            row = ord(place[0])-97
            col = int(place[1])-1
            verificare_placement(placement2_list, row, col)
            if verificare_placement(placement2_list, row, col) == True:
                direction = input(
                    "Choose on which direction you want to place your ship (N,S,E,W) :").lower()
                if direction in ["n", "s", "e", "w"]:
                    if direction == "n":
                        if row == 0:
                            os.system("clear")
                            print(
                                "In this case the world is flat and you can't cross the edges")
                            continue
                        verificare_placement(placement2_list, row-1, col)
                        if verificare_placement(placement2_list, row-1, col) == True:
                            placement2_list[row][col] = "X"
                            placement2_list[row-1][col] = "X"
                            shipsx2 -= 1
                            os.system("clear")
                        elif verificare_placement(placement2_list, row-1, col) == False:
                            os.system("clear")
                            print("Your ships are too close!")
                            continue
                    if direction == "s":
                        if row == 4:
                            os.system("clear")
                            print(
                                "In this case the world is flat and you can't cross the edges")
                            continue
                        verificare_placement(placement2_list, row+1, col)
                        if verificare_placement(placement2_list, row+1, col) == True:
                            placement2_list[row][col] = "X"
                            placement2_list[row+1][col] = "X"
                            shipsx2 -= 1
                            os.system("clear")
                        elif verificare_placement(placement2_list, row+1, col) == False:
                            os.system("clear")
                            print("Your ships are too close!")
                            continue
                    if direction == "e":
                        if col == 4:
                            os.system("clear")
                            print(
                                "In this case the world is flat and you can't cross the edges")
                            continue
                        verificare_placement(placement2_list, row, col+1)
                        if verificare_placement(placement2_list, row, col+1) == True:
                            placement2_list[row][col] = "X"
                            placement2_list[row][col+1] = "X"
                            shipsx2 -= 1
                            os.system("clear")
                        elif verificare_placement(placement2_list, row, col+1) == False:
                            os.system("clear")
                            print("Your ships are too close!")
                            continue
                    if direction == "w":
                        if col == 0:
                            os.system("clear")
                            print(
                                "In this case the world is flat and you can't cross the edges")
                            continue
                        verificare_placement(placement2_list, row, col-1)
                        if verificare_placement(placement2_list, row, col-1) == True:
                            placement2_list[row][col] = "X"
                            placement2_list[row][col-1] = "X"
                            shipsx2 -= 1
                            os.system("clear")
                        elif verificare_placement(placement2_list, row, col-1) == False:
                            os.system("clear")
                            print("Your ships are too close!")
                            continue
                else:
                    os.system("clear")
                    print("Invalid input!")
                    continue
            elif verificare_placement(placement2_list, row, col) == False:
                os.system("clear")
                print("Your ships are too close")
                continue
        else:
            os.system("clear")
            print("Invalid input!")
            continue
    return placement2_list

def surroundings_forging_list(other_player_board, row, column, marked_board):
    if 0 < row < 4 and 0 < column < 4:
        surroundings_other_player_board = [other_player_board[row - 1][column], other_player_board[row + 1]
                                           [column], other_player_board[row][column + 1], other_player_board[row][column - 1]]
        surroundings_marked_board = [marked_board[row - 1][column], marked_board[row + 1]
                                     [column], marked_board[row][column + 1], marked_board[row][column - 1]]
        return surroundings_other_player_board, surroundings_marked_board

    elif 0 < row < 4 and column == 0:
        surroundings_other_player_board = [other_player_board[row - 1][column],
                                           other_player_board[row + 1][column], other_player_board[row][column + 1]]
        surroundings_marked_board = [marked_board[row - 1][column],
                                     marked_board[row + 1][column], marked_board[row][column + 1]]
        return surroundings_other_player_board, surroundings_marked_board

    elif 0 < row < 4 and column == 4:
        surroundings_other_player_board = [other_player_board[row - 1][column],
                                           other_player_board[row + 1][column], other_player_board[row][column - 1]]
        surroundings_marked_board = [marked_board[row - 1][column],
                                     marked_board[row + 1][column], marked_board[row][column - 1]]
        return surroundings_other_player_board, surroundings_marked_board

    elif row == 0 and 0 < column < 4:
        surroundings_other_player_board = [other_player_board[row + 1][column],
                                           other_player_board[row][column + 1], other_player_board[row][column - 1]]
        surroundings_marked_board = [marked_board[row + 1][column],
                                     marked_board[row][column + 1], marked_board[row][column - 1]]
        return surroundings_other_player_board, surroundings_marked_board

    elif row == 4 and 0 < column < 4:
        surroundings_other_player_board = [other_player_board[row - 1][column],
                                           other_player_board[row][column + 1], other_player_board[row][column - 1]]
        surroundings_marked_board = [marked_board[row - 1][column],
                                     marked_board[row][column + 1], marked_board[row][column - 1]]
        return surroundings_other_player_board, surroundings_marked_board

    elif row == 0 and column == 0:
        surroundings_other_player_board = [
            other_player_board[row + 1][column], other_player_board[row][column + 1]]
        surroundings_marked_board = [
            marked_board[row + 1][column], marked_board[row][column + 1]]
        return surroundings_other_player_board, surroundings_marked_board

    elif row == 0 and column == 4:
        surroundings_other_player_board = [
            other_player_board[row + 1][column], other_player_board[row][column - 1]]
        surroundings_marked_board = [
            marked_board[row + 1][column], marked_board[row][column - 1]]
        return surroundings_other_player_board, surroundings_marked_board

    elif row == 4 and column == 0:
        surroundings_other_player_board = [
            other_player_board[row - 1][column], other_player_board[row][column + 1]]
        surroundings_marked_board = [
            marked_board[row - 1][column], marked_board[row][column + 1]]
        return surroundings_other_player_board, surroundings_marked_board

    elif row == 4 and column == 4:
        surroundings_other_player_board = [
            other_player_board[row - 1][column], other_player_board[row][column - 1]]
        surroundings_marked_board = [
            marked_board[row - 1][column], marked_board[row][column - 1]]
        return surroundings_other_player_board, surroundings_marked_board
    
def changing_first_h_for_2xship(row, column, marked_board):
    if 0 < row < 4 and 0 < column < 4:
        surroundings_marked_board = [marked_board[row - 1][column], marked_board[row + 1]
                                     [column], marked_board[row][column + 1], marked_board[row][column - 1]]
        if surroundings_marked_board[0] == 'H':
            return (row - 1, column)

        elif surroundings_marked_board[1] == 'H':
            return (row + 1, column)

        elif surroundings_marked_board[2] == 'H':
            return (row, column + 1)

        else:
            return (row, column - 1)

    elif 0 < row < 4 and column == 0:
        surroundings_marked_board = [marked_board[row - 1][column],
                                     marked_board[row + 1][column], marked_board[row][column + 1]]
        if surroundings_marked_board[0] == 'H':
            return (row - 1, column)

        elif surroundings_marked_board[1] == 'H':
            return (row + 1, column)

        else:
            return (row, column + 1)

    elif 0 < row < 4 and column == 4:
        surroundings_marked_board = [marked_board[row - 1][column],
                                     marked_board[row + 1][column], marked_board[row][column - 1]]
        if surroundings_marked_board[0] == 'H':
            return (row - 1, column)

        elif surroundings_marked_board[1] == 'H':
            return (row + 1, column)

        else:
            return (row, column - 1)

    elif row == 0 and 0 < column < 4:
        surroundings_marked_board = [marked_board[row + 1][column],
                                     marked_board[row][column + 1], marked_board[row][column - 1]]
        if surroundings_marked_board[0] == 'H':
            return (row + 1, column)

        elif surroundings_marked_board[1] == 'H':
            return (row, column+1)

        else:
            return (row, column - 1)

    elif row == 4 and 0 < column < 4:
        surroundings_marked_board = [marked_board[row - 1][column],
                                     marked_board[row][column + 1], marked_board[row][column - 1]]
        if surroundings_marked_board[0] == 'H':
            return (row - 1, column)

        elif surroundings_marked_board[1] == 'H':
            return (row, column+1)

        else:
            return (row, column - 1)

    elif row == 0 and column == 0:
        surroundings_marked_board = [
            marked_board[row + 1][column], marked_board[row][column + 1]]
        if surroundings_marked_board[0] == 'H':
            return (row + 1, column)

        else:
            return (row, column + 1)

    elif row == 0 and column == 4:
        surroundings_marked_board = [
            marked_board[row + 1][column], marked_board[row][column - 1]]
        if surroundings_marked_board[0] == 'H':
            return (row + 1, column)

        else:
            return (row, column - 1)

    elif row == 4 and column == 0:
        surroundings_marked_board = [
            marked_board[row - 1][column], marked_board[row][column + 1]]
        if surroundings_marked_board[0] == 'H':
            return (row - 1, column)

        else:
            return (row, column + 1)

    elif row == 4 and column == 4:
        surroundings_marked_board = [
            marked_board[row - 1][column], marked_board[row][column - 1]]
        if surroundings_marked_board[0] == 'H':
            return (row - 1, column)

        else:
            return (row, column - 1)

def mark(other_player_board, row, column, marked_board):
    new_row = 9
    new_col = 9
    surroundings_other_player_board, surroundings_marked_board = surroundings_forging_list(
        other_player_board, row, column, marked_board)
    if other_player_board[row][column] == 0:
        print("You've missed!")
        marked_board[row][column] = 'M'
# in case of missing
    elif marked_board[row][column] in ['M', 'S', 'H']:
        print("Oops! Already tried this position. Choose a diferent one next time.")
# in case of trying the same missed or sink as before
    elif other_player_board[row][column] == 'X' and surroundings_other_player_board.count("X") == 0:
        marked_board[row][column] = "S"
        sound('long')
        print("You've sunk a ship")
# sinking a boat made out of one block
    elif other_player_board[row][column] == 'X' and surroundings_marked_board.count("H") == 1:
        marked_board[row][column] = "S"
        new_row = changing_first_h_for_2xship(row, column, marked_board)[0]
        new_col = changing_first_h_for_2xship(row, column, marked_board)[1]
        marked_board[new_row][new_col] = "S"
        sound('long')
        print("You've sunk a ship")

# checking for a sink in a 2 block ship
    elif other_player_board[row][column] == 'X' and surroundings_other_player_board.count("X") == 1:
        marked_board[row][column] = "H"
        print("You've hit a ship!")
        sound('short')
# checking for a hit in a 2 block ship
    else:
        print("else din mark 273")  # de sters la final
    return marked_board

def get_shot_input(player):
    while True:
        shot = str(input("Player " + player +
                         " choose a position to shot: ").lower())
        if shot[0] in ["a", "b", "c", "d", "e"] and shot[1] in ["1", "2", "3", "4", "5"]:
            row = ord(shot[0])-97
            col = int(shot[1])-1
            return (row, col)
        else:
            print("Invalid input. Try again.")
            continue


def has_won(board,placement1):
    
    for i in board:
        for j in i:
            if j==s:
                count+=1
    if count==7:
        return True
    else:
        return False

def main():
    cover()
    board = init_list()
    tries_1_list = copy.deepcopy(board)
    tries_2_list = copy.deepcopy(board)
    player = ""
    count = 0
    placement1_list = copy.deepcopy(board)
    placement2_list = copy.deepcopy(board)
    print("\nPlayer2, go away and let player1 place his ships\n")
    placement1(placement1_list)
    print("\nPlayer1, go away and let player2 place his ships\n")
    input("Player 2 when you are ready press Enter...")
    placement2(placement2_list)
    while True:
        if count % 2 == 0:
            player == "1"
            print_radars(player, tries_1_list, tries_2_list)
            (row, col) = get_shot_input(player)
            tries_1_list = mark(placement_2_list, row, col, tries_1_list)
            print_radars(player, tries_1_list, tries_2_list)
            os.system("clear")
        else:
            player == "2"
            print_radars(player, tries_1_list, tries_2_list)
            (row, col) = get_shot_input(player)
            tries_2_list = mark(placement_1_list, row, col, tries_2_list)
            print_radars(player, tries_1_list, tries_2_list)
            os.system("clear")
        count += 1

if __name__=="__main__":
    main()
