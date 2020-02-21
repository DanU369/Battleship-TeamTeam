import copy


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


def placement1(board):
    placement1_list = copy.deepcopy(board)
    shipsx1 = 3
    shipsx2 = 2
    print_board(placement1_list)
    while shipsx1 > 0:
        ships = shipsx1 + shipsx2
        print("Player 1, you have {} ships left to place".format(ships))
        print("Now you should place a 1 block ship")
        place = str(
            input("Choose a position to place your ship: ").lower())
        row = ord(place[0])-97
        col = int(place[1])-1
        placement1_list[row][col] = "X"
        print_board(placement1_list)
        shipsx1 -= 1
    while shipsx2 > 0:
        ships = shipsx1 + shipsx2
        print("Player 1, you have {} ships left to place".format(ships))
        print("Now you should place a 2 blocks ship")
        place = str(
            input("Choose a position to place your ship's head: ").lower())
        direction = input(
            "Choose on which direction you want to place your ship (N,S,E,W) :").lower()
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
    return placement1_list


def placement2(board):
    placement2_list = copy.deepcopy(board)
    shipsx1 = 3
    shipsx2 = 2
    print_board(placement2_list)
    while shipsx1 > 0:
        ships = shipsx1 + shipsx2
        print("Player 2, you have {} ships left to place".format(ships))
        print("Now you should place a 1 block ship")
        place = str(
            input("Choose a position to place your ship: ").lower())
        row = ord(place[0])-97
        col = int(place[1])-1
        placement2_list[row][col] = "X"
        print_board(placement2_list)
        shipsx1 -= 1
    while shipsx2 > 0:
        ships = shipsx1 + shipsx2
        print("Player 2, you have {} ships left to place".format(ships))
        print("Now you should place a 2 blocks ship")
        place = str(
            input("Choose a position to place your ship's head: ").lower())
        direction = input(
            "Choose on which direction you want to place your ship (N,S,E,W) :").lower()
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
    return placement2_list


def get_shot_input():
    while True:
        shot = str(input("Choose a position to shot: ").lower())
        if shot[0] in ["a", "b", "c", "d", "e"] and shot[1] in ["1", "2", "3", "4", "5"]:
            row = ord(shot[0])-97
            col = int(shot[1])-1
            return (row, col)
        else:
            print("Invalid input. Try again.")
            continue


# def mark(player, board):
#     if player == "1":
#         board[row][column] = 'x'
#     elif player == "2":
#         board[row][column] = '0'
#     else:
#         print("Insert only 1 or 2!")
#     return board


def main():
    cover()
    board = init_list()
    player = str(input("Input 1 for Player 1 and 2 for Player 2: "))
    count = 0
    while True:
        if count % 2 == 0:
            player == "1"
            placement_1_list = placement1(board)
            print(placement_1_list)
        else:
            player == "2"
            print_board(board)
            placement_2_list = placement2(board)
            print(placement_2_list)

        count += 1
        print("Teste github")


main()
