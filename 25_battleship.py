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


def init_list():

    init_board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
        0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    return init_board


def print_board(board):

    print('''
                1   2   3   4   5

            A   {}   {}   {}   {}   {}

            B   {}   {}   {}   {}   {}

            C   {}   {}   {}   {}   {}

            D   {}   {}   {}   {}   {}

            E   {}   {}   {}   {}   {}
        '''.format(board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[1][0], board[1][1], board[1][2],
                   board[1][3], board[1][4], board[2][0], board[2][1], board[2][2], board[2][3], board[2][4],
                   board[3][0], board[3][1], board[3][2], board[3][3], board[3][4],
                   board[4][0], board[4][1], board[4][2], board[4][3], board[4][4]))


def sound(sound_duration):
    if sound_duration == 'long':
        duration = 0.9  # seconds
        freq = 300  # Hz
        os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
    else:
        duration = 0.08  # seconds
        freq = 460  # Hz
        os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))


def placement1(board):
    placement1_list = copy.deepcopy(board)
    shipsx1 = 1
    shipsx2 = 1
    print_board(placement1_list)
    while shipsx1 > 0:
        ships = shipsx1 + shipsx2
        print("Player 1, you have {} ships left to place".format(ships))
        print("Now you should place a 1 block ship")
        place = str(
            input("Choose a position to place your ship: ").lower())
        if place[0] in ['a', 'b', 'c', 'd', 'e'] and place[1] in ['1', '2', '3', '4', '5']:
            row = ord(place[0]) - 97
            col = int(place[1]) - 1
# limitari de 1 casuta
            if row == 4:
                if placement1_list[row-1][col] == placement1_list[row][col+1] == placement1_list[row][col-1] == placement1_list[row][col] == 0:
                    placement1_list[row][col] = "X"
                    print_board(placement1_list)
                    shipsx1 -= 1
                else:
                    print("\nShips are too close\n")
                    continue
            elif col == 4:
                if placement1_list[row+1][col] == placement1_list[row-1][col] == placement1_list[row][col-1] == placement1_list[row][col] == 0:
                    placement1_list[row][col] = "X"
                    print_board(placement1_list)
                    shipsx1 -= 1
                else:
                    print("\nShips are too close\n")
                    continue
            elif row == 0:
                if placement1_list[row+1][col] == placement1_list[row][col+1] == placement1_list[row][col-1] == placement1_list[row][col] == 0:
                    placement1_list[row][col] = "X"
                    print_board(placement1_list)
                    shipsx1 -= 1
                else:
                    print("\nShips are too close\n")
                    continue
            elif col == 0:
                if placement1_list[row+1][col] == placement1_list[row-1][col] == placement1_list[row][col+1] == placement1_list[row][col] == 0:
                    placement1_list[row][col] = "X"
                    print_board(placement1_list)
                    shipsx1 -= 1
                else:
                    print("\nShips are too close\n")
                    continue
            elif placement1_list[row+1][col] == placement1_list[row-1][col] == placement1_list[row][col+1] == placement1_list[row][col-1] == placement1_list[row][col] == 0:
                placement1_list[row][col] = "X"
                print_board(placement1_list)
                shipsx1 -= 1
            else:
                print("\nShips are too close\n")
                continue
        else:
            print("Invalid input!")
            continue
    while shipsx2 > 0:
        ships = shipsx1 + shipsx2
        print("Player 1, you have {} ships left to place".format(ships))
        print("Now you should place a 2 blocks ship")
        place = str(
            input("Choose a position to place your ship's head: ").lower())
        if place[0] in ["a", "b", "c", "d", "e"] and place[1] in ["1", "2", "3", "4", "5"]:
            direction = input(
                "Choose on which direction you want to place your ship (N,S,E,W) :").lower()
            if direction in ["n", "s", "e", "w"]:
                row = ord(place[0])-97
                col = int(place[1])-1
                placement1_list[row][col] = "X"
                if direction == "n":
                    placement1_list[row-1][col] = "X"
                if direction == "s":
                    placement1_list[row+1][col] = "X"
                if direction == "e":
                    placement1_list[row][col+1] = "X"
                if direction == "w":
                    placement1_list[row][col-1] = "X"
                print_board(placement1_list)
                shipsx2 -= 1
            else:
                print("Invalid input!")
                continue
        else:
            print("Invalid input!")
            continue
    return placement1_list


def placement2(board):
    placement2_list = copy.deepcopy(board)
    shipsx1 = 1
    shipsx2 = 1
    print_board(placement2_list)
    while shipsx1 > 0:
        ships = shipsx1 + shipsx2
        print("Player 2, you have {} ships left to place".format(ships))
        print("Now you should place a 1 block ship")
        place = str(
            input("Choose a position to place your ship: ").lower())
        if place[0] in ["a", "b", "c", "d", "e"] and place[1] in ["1", "2", "3", "4", "5"]:
            row = ord(place[0])-97
            col = int(place[1]) - 1
    # limitari de 1 casuta
            if row == 4:
                if placement2_list[row-1][col] == placement2_list[row][col+1] == placement2_list[row][col-1] == placement2_list[row][col] == 0:
                    placement2_list[row][col] = "X"
                    print_board(placement2_list)
                    shipsx1 -= 1
                else:
                    print("\nShips are too close\n")
                    continue
            elif col == 4:
                if placement2_list[row+1][col] == placement2_list[row-1][col] == placement2_list[row][col-1] == placement2_list[row][col] == 0:
                    placement2_list[row][col] = "X"
                    print_board(placement2_list)
                    shipsx1 -= 1
                else:
                    print("\nShips are too close\n")
                    continue
            elif row == 0:
                if placement2_list[row+1][col] == placement2_list[row][col+1] == placement2_list[row][col-1] == placement2_list[row][col] == 0:
                    placement2_list[row][col] = "X"
                    print_board(placement2_list)
                    shipsx1 -= 1
                else:
                    print("\nShips are too close\n")
                    continue
            elif col == 0:
                if placement2_list[row+1][col] == placement2_list[row-1][col] == placement2_list[row][col+1] == placement2_list[row][col] == 0:
                    placement2_list[row][col] = "X"
                    print_board(placement2_list)
                    shipsx1 -= 1
                else:
                    print("\nShips are too close\n")
                    continue
            elif placement2_list[row+1][col] == placement2_list[row-1][col] == placement2_list[row][col+1] == placement2_list[row][col-1] == placement2_list[row][col] == 0:
                placement2_list[row][col] = "X"
                print_board(placement2_list)
                shipsx1 -= 1
            else:
                print("\nShips are too close\n")
                continue
        else:
            print("Invalid input!")
            continue
    while shipsx2 > 0:
        ships = shipsx1 + shipsx2
        print("Player 2, you have {} ships left to place".format(ships))
        print("Now you should place a 2 blocks ship")
        place = str(
            input("Choose a position to place your ship's head: ").lower())
        if place[0] in ["a", "b", "c", "d", "e"] and place[1] in ["1", "2", "3", "4", "5"]:
            direction = input(
                "Choose on which direction you want to place your ship (N,S,E,W) :").lower()
            if direction in ["n", "s", "e", "w"]:
                row = ord(place[0])-97
                col = int(place[1])-1
                placement2_list[row][col] = "X"
                if direction == "n":
                    placement2_list[row-1][col] = "X"
                if direction == "s":
                    placement2_list[row+1][col] = "X"
                if direction == "e":
                    placement2_list[row][col+1] = "X"
                if direction == "w":
                    placement2_list[row][col-1] = "X"
                print_board(placement2_list)
                shipsx2 -= 1
            else:
                print("Invalid input!")
                continue

        else:
            print("Invalid input!")
            continue
    return placement2_list


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


def main():
    cover()
    board = init_list()    # initial board (1)
    # board were player 1 checks it's tries(4)
    tries_1_list = copy.deepcopy(board)
    # board were player 2 checks it's tries(5)
    tries_2_list = copy.deepcopy(board)
    player = ""
    count = 0
    # board with ships placements for player 1 (2)
    placement_1_list = placement1(board)
# we have to make a privacy pause while the players are switching and clear the screen
    # board with ships placements for player 2 (3)
    placement_2_list = placement2(board)
    os.system('clear')
    while True:
        if count % 2 == 0:
            player = "1"
            print_board(tries_1_list)
            (row, col) = get_shot_input(player)
            tries_1_list = mark(placement_2_list, row, col, tries_1_list)
            print_board(tries_1_list)
            os.system('clear')
        else:
            player = "2"
            print_board(tries_2_list)
            (row, col) = get_shot_input(player)
            tries_2_list = mark(placement_1_list, row, col, tries_2_list)
            print_board(tries_2_list)
            os.system('clear')

        count += 1


main()
