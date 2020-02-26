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

def verificare_placement(placement_list, row, col):
    if row == 0 and col == 0:
        if placement_list[1][0] == placement_list[0][1] == 0:
            return True
        else:
            return False
    if row == 0 and col == 4:
        if placement_list[0][3] == placement_list[1][4] == 0:
            return True
        else:
            return False
    if row == 4 and col == 4:
        if placement_list[4][3] == placement_list[3][4] == 0:
            return True
        else:
            return False
    if row == 4 and col == 0:
        if placement_list[3][0] == placement_list[4][1] == 0:
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
    print_board(placement1_list)
    while shipsx1 > 0:
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
                print("Your ships are too close")
                continue
            print_board(placement1_list)
        else:
            print("Invalid input!")
            continue
    while shipsx2 > 0:
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
                            print(
                                "In this our case the world is flat and you can't cross the edges")
                            continue
                        verificare_placement(placement1_list, row-1, col)
                        if verificare_placement(placement1_list, row-1, col) == True:
                            placement1_list[row][col] = "X"
                            placement1_list[row-1][col] = "X"
                            shipsx1 -= 1
                            print_board(placement1_list)
                        elif verificare_placement(placement1_list, row-1, col) == False:
                            print("Your ships are too close!")
                            continue
                    if direction == "s":
                        if row == 4:
                            print(
                                "In this our case the world is flat and you can't cross the edges")
                            continue
                        verificare_placement(placement1_list, row+1, col)
                        if verificare_placement(placement1_list, row+1, col) == True:
                            placement1_list[row][col] = "X"
                            placement1_list[row+1][col] = "X"
                            shipsx1 -= 1
                            print_board(placement1_list)
                        elif verificare_placement(placement1_list, row+1, col) == False:
                            print("Your ships are too close!")
                            continue
                    if direction == "e":
                        if col == 4:
                            print(
                                "In this our case the world is flat and you can't cross the edges")
                            continue
                        verificare_placement(placement1_list, row, col+1)
                        if verificare_placement(placement1_list, row, col+1) == True:
                            placement1_list[row][col] = "X"
                            placement1_list[row][col+1] = "X"
                            shipsx1 -= 1
                            print_board(placement1_list)
                        elif verificare_placement(placement1_list, row, col+1) == False:
                            print("Your ships are too close!")
                            continue
                    if direction == "w":
                        if col == 0:
                            print(
                                "In this our case the world is flat and you can't cross the edges")
                            continue
                        verificare_placement(placement1_list, row, col-1)
                        if verificare_placement(placement1_list, row, col-1) == True:
                            placement1_list[row][col] = "X"
                            placement1_list[row][col-1] = "X"
                            shipsx1 -= 1
                            print_board(placement1_list)
                        elif verificare_placement(placement1_list, row, col-1) == False:
                            print("Your ships are too close!")
                            continue
                else:
                    print("Invalid input!")
                    continue
            elif verificare_placement(placement1_list, row, col) == False:
                print("Your ships are too close")
                continue
        else:
            print("Invalid input!")
            continue
    return placement1_list

def placement2(placement2_list):
    shipsx1 = 3
    shipsx2 = 2
    print_board(placement2_list)
    while shipsx1 > 0:
        ships = shipsx1 + shipsx2
        print("Player 1, you have {} ships left to place".format(ships))
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
                print("Your ships are too close")
                continue
            print_board(placement2_list)
        else:
            print("Invalid input!")
            continue

    while shipsx2 > 0:
        ships = shipsx1 + shipsx2
        print("Player 1, you have {} ships left to place".format(ships))
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
                            print(
                                "In this our case the world is flat and you can't cross the edges")
                            continue
                        verificare_placement(placement2_list, row-1, col)
                        if verificare_placement(placement2_list, row-1, col) == True:
                            placement2_list[row][col] = "X"
                            placement2_list[row-1][col] = "X"
                            shipsx1 -= 1
                            print_board(placement2_list)
                        elif verificare_placement(placement2_list, row-1, col) == False:
                            print("Your ships are too close!")
                            continue
                    if direction == "s":
                        if row == 4:
                            print(
                                "In this our case the world is flat and you can't cross the edges")
                            continue
                        verificare_placement(placement2_list, row+1, col)
                        if verificare_placement(placement2_list, row+1, col) == True:
                            placement2_list[row][col] = "X"
                            placement2_list[row+1][col] = "X"
                            shipsx1 -= 1
                            print_board(placement2_list)
                        elif verificare_placement(placement2_list, row+1, col) == False:
                            print("Your ships are too close!")
                            continue
                    if direction == "e":
                        if col == 4:
                            print(
                                "In this our case the world is flat and you can't cross the edges")
                            continue
                        verificare_placement(placement2_list, row, col+1)
                        if verificare_placement(placement2_list, row, col+1) == True:
                            placement2_list[row][col] = "X"
                            placement2_list[row][col+1] = "X"
                            shipsx1 -= 1
                            print_board(placement2_list)
                        elif verificare_placement(placement2_list, row, col+1) == False:
                            print("Your ships are too close!")
                            continue
                    if direction == "w":
                        if col == 0:
                            print(
                                "In this our case the world is flat and you can't cross the edges")
                            continue
                        verificare_placement(placement2_list, row, col-1)
                        if verificare_placement(placement2_list, row, col-1) == True:
                            placement2_list[row][col] = "X"
                            placement2_list[row][col-1] = "X"
                            shipsx1 -= 1
                            print_board(placement2_list)
                        elif verificare_placement(placement2_list, row, col-1) == False:
                            print("Your ships are too close!")
                            continue
                else:
                    print("Invalid input!")
                    continue
            elif verificare_placement(placement2_list, row, col) == False:
                print("Your ships are too close")
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



# def mark(player, board):
#     if player == "1":
#         board[row][column] = 'x'
#     elif player == "2":
#         board[row][column] = '0'
#     else:
#         print("Insert only 1 or 2!")
#     return board
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
    print("\n"*250)
    print("\nPlayer1, go away and let player2 place his ships\n")
    input("Player 2 when you are ready press Enter...")
    placement2(placement2_list)
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
