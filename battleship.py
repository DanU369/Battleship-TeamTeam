import copy
l = """
 ______     ______     ______   ______   __         ______     ______     __  __     __     ______  
/\  == \   /\  __ \   /\__  _\ /\__  _\ /\ \       /\  ___\   /\  ___\   /\ \_\ \   /\ \   /\  == \ 
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
"""


def init_list(board):

    board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
        0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    return board


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


def placement1():
    shipsx1 = 3
    shipsx2 = 2
    print_board(placement1_list)
    while shipsx1 > 0:
        ships = shipsx1+shipsx2
        print("You have {} ships left to place".format(ships))
        print("Now you should place a 1 block ship")
        place = str(input("Choose a position to place your ship: ").lower())
        if place[0] in ["a", "b", "c", "d", "e"] and place[1] in ["1", "2", "3", "4", "5"]:
            row = ord(place[0])-97
            col = int(place[1])-1
# limitari de 1 casuta
            if row == 4:
                if placement1_list[row-1][col] == placement1_list[row][col+1] == placement1_list[row][col-1] == placement1_list[row][col] == 0:
                    placement1_list[row][col] = "X"
                    print_board(placement1_list)
                    shipsx1 -= 1
                else:
                    print("Ships are too close")
                    continue
            elif col == 4:
                if placement1_list[row+1][col] == placement1_list[row-1][col] == placement1_list[row][col-1] == placement1_list[row][col] == 0:
                    placement1_list[row][col] = "X"
                    print_board(placement1_list)
                    shipsx1 -= 1
                else:
                    print("Ships are too close")
                    continue
            elif row == 0:
                if placement1_list[row+1][col] == placement1_list[row][col+1] == placement1_list[row][col-1] == placement1_list[row][col] == 0:
                    placement1_list[row][col] = "X"
                    print_board(placement1_list)
                    shipsx1 -= 1
                else:
                    print("Ships are too close")
                    continue
            elif col == 0:
                if placement1_list[row+1][col] == placement1_list[row-1][col] == placement1_list[row][col+1] == placement1_list[row][col] == 0:
                    placement1_list[row][col] = "X"
                    print_board(placement1_list)
                    shipsx1 -= 1
                else:
                    print("Ships are too close")
                    continue
            elif placement1_list[row+1][col] == placement1_list[row-1][col] == placement1_list[row][col+1] == placement1_list[row][col-1] == placement1_list[row][col] == 0:
                placement1_list[row][col] = "X"
                print_board(placement1_list)
                shipsx1 -= 1
            else:
                print("Ships are too close")
                continue
        else:
            print("Invalid input!")
            continue
    while shipsx2 > 0:
        ships = shipsx1+shipsx2
        print("You have {} ships left to place".format(ships))
        print("Now you should place a 2 blocks ship")
        place = str(
            input("Choose a position to place your ship's head: ").lower())
        if place[0] in ["a", "b", "c", "d", "e"] and place[1] in ["1", "2", "3", "4", "5"]:
            direction = input(
                "Choose on wich direction you want to place your ship (N,S,E,W) :").lower()
            if direction in ["n","s","e","w"]:
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


# def limitari_1casuta(placement1_list, row, col):
    # if row == 4:
    #     if placement1_list[row-1][col] == placement1_list[row][col+1] == placement1_list[row][col-1] == placement1_list[row][col] == 0:
    #         placement1_list[row][col] = "X"
    #         print_board(placement1_list)
    #         return False
    #     else:
    #         print("Ships are too close")
    #         return True
    # elif col == 4:
    #     if placement1_list[row+1][col] == placement1_list[row-1][col] == placement1_list[row][col-1] == placement1_list[row][col] == 0:
    #         placement1_list[row][col] = "X"
    #         print_board(placement1_list)
    #         return False
    #     else:
    #         print("Ships are too close")
    #         return True
    # elif row == 0:
    #     if placement1_list[row+1][col] == placement1_list[row][col+1] == placement1_list[row][col-1] == placement1_list[row][col] == 0:
    #         placement1_list[row][col] = "X"
    #         print_board(placement1_list)
    #         return False
    #     else:
    #         print("Ships are too close")
    #         return True
    # elif col == 0:
    #     if placement1_list[row+1][col] == placement1_list[row-1][col] == placement1_list[row][col+1] == placement1_list[row][col] == 0:
    #         placement1_list[row][col] = "X"
    #         print_board(placement1_list)
    #         return False
    #     else:
    #         print("Ships are too close")
    #         return True
    # else:
    #     if placement1_list[row+1][col] == placement1_list[row-1][col] == placement1_list[row][col+1] == placement1_list[row][col-1] == placement1_list[row][col] == 0:
    #         placement1_list[row][col] = "X"
    #         print_board(placement1_list)
    #         return False
    #     else:
    #         print("Ships are too close")
    #         return True

def main():
    print(l)
    board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
        0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    placement1_list = copy.deepcopy(board)  # de modificat pe git
    placement1()
    print_board(board)

# def get_shot_input():
#     while True:
#         shot = str(input("Choose a position to shot: ").lower())
#         if shot[0] in ["a", "b", "c", "d", "e"] and shot[1] in ["1", "2", "3", "4", "5"]:
#             row = ord(shot[0])-97
#             col = int(shot[1])-1
#             return (row, col)
#         else:
#             print("Invalid input. Try again.")
#             continue


# print(get_shot_input())
