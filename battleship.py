
# returneaza player_versus
def get_game_mode():
    pass 

# returneaza board_size
def get_board_size():
    pass

# returneaza ships_number
def get_ships_number():
    pass

# returneaza turns number
def get_turns_to_play():
    pass

# returneaza board
def generate_board(board_size):
    pass

# printeazaz boardul
def print_board(board, board_size):
    pass

# returneaza ships
def generate_ships(ships_number):
    pass

# returneaza player_coordinates
def get_coordinates(board_size):
    pass

# returneaza ship_direction, valid_direction
def validate_ship_position(row,column, board):
    pass

#####
#####
# DE AICI IN SUS
# MIHAI
# RAUL
# CRISTI
#####
#####
# DE AICI IN JOS 
# MADA
# TOMA
#####
#####

# return board
def place_ships(ships, board, board_size):

    for ship in ships:
        while True:
            print_board(board,board_size)
            ship_coordinates = get_coordinates(board_size)
            row = ord(ship_coordinates[0]) - ord("a")
            column = int(ship_coordinates[1])-1
            ship_direction,valid_directions = validate_ship_position(row,column,board)
            if ship_direction != "\nNow, please select the direction you want the ship to go":
                while True:
                    user_choice = input(ship_direction)
                    if user_choice in valid_directions:
                        if user_choice == "1":
                            board[row][column] = "T" 
                            board[row+1][column] = "T"
                            board[row+2][column] = "T"
                            break
                        elif user_choice == "2":
                            board[row][column] = "T" 
                            board[row][column+1] = "T"
                            board[row][column+2] = "T"
                            break
                        elif user_choice == "3":
                            board[row][column] = "T" 
                            board[row-1][column] = "T"
                            board[row-2][column] = "T"
                            break
                        elif user_choice == "4":
                            board[row][column] = "T" 
                            board[row][column-1] = "T"
                            board[row][column-2] = "T"
                            break

                    else:
                        print("Please make a valid input")

                spacing_ships(board)
                break

            else:
                print("\nPlease try again, looks like there wasn't enough space for the ship to be placed.")

    
    return board

#ships not closer than 1 space
def spacing_ships(board):

    m=0
    for j in board:
        n=0
        for i in j:
            
            if i == "T":
                try:
                    if n+1 < len(board[0]) and j[n+1] == "-":
                        j[n+1] = "Z"
                except IndexError:
                    pass
                try:
                    if n-1 >= 0 and j[n-1] == "-":
                        j[n-1] = "Z"
                except IndexError:
                    pass
                try:
                    if m+1 < len(board) and board[m+1][n] == "-":
                        board[m+1][n] = "Z"
                except IndexError:
                    pass
                try:
                    if m-1 >= 0 and board[m-1][n] == "-":
                        board[m-1][n] = "Z"
                except IndexError:
                    pass
            n+=1   
        m+=1        

# return hidden board
def update_board_after_shoot(player_board, hidden_board, board_size):
    pass

# returneaza true sau false
def win_condition(player_one_board, player_two_board):
    pass

# returneaza true sau false
def tie_condition(turns, counter):
    pass

# Optional
def play_with_AI():
    pass


def main():
    pass




if __name__ == "__main__":
    main()