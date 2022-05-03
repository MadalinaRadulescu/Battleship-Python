
# returneaza player_versus
def get_game_mode():
    pass 

# returneaza board_size int de input
def get_board_size():
    pass

# returneaza ships_number integer input
def get_ships_number():
    pass

# returneaza turns number
def get_turns_to_play():
    pass

# returneaza board lista de liste
def generate_board(board_size):
    pass

# printeazaz boardul
def print_board(board, board_size):
    pass

# returneaza ships o lista de liste
def generate_ships(ships_number):
    pass

# returneaza player_coordinates  2 cifre coordonate
def get_coordinates(board_size):
    pass

# returneaza ship_direction, valid_direction
def validate_ship_position(row, column, board):
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
def update_board_after_shoot(player_board, guess_board, board_size):
    while True:
        coordinates = get_coordinates(board_size)
        row = ord(coordinates[0]) - ord("a")
        column = int(coordinates[1])-1
        if player_board[row][column] == "-":
            player_board[row][column] = "o"
            guess_board[row][column] = "o"
            print("you've missed this time!")
            return guess_board
        elif player_board[row][column] == "T":
            player_board[row][column] = "H"
            guess_board[row][column] = "H"    
            print("You got a shot!")
            try:
                if player_board[row][column] == player_board[row+1][column] == player_board[row+2][column] == "H":
                    player_board[row][column] = player_board[row+1][column] = player_board[row+2][column] = "S"
                    guess_board[row][column] = guess_board[row+1][column] = guess_board[row+2][column] = "S"
                    return guess_board
            except IndexError:
                pass
            try:
                if player_board[row][column] == player_board[row][column+1] == player_board[row][column+2] == "H":
                    player_board[row][column] = player_board[row][column+1] = player_board[row][column+2] = "S"
                    guess_board[row][column] = guess_board[row][column+1] = guess_board[row][column+2] = "S"
                    return guess_board    
            except IndexError:
                pass  
            try:
                if player_board[row][column] == player_board[row-1][column] == player_board[row-2][column] == "H":
                    player_board[row][column] = player_board[row-1][column] = player_board[row-2][column] = "S"
                    guess_board[row][column] = guess_board[row-1][column] = guess_board[row-2][column] = "S"
                    return guess_board    
            except IndexError:
                pass  
            try:
                if player_board[row][column] == player_board[row][column-1] == player_board[row][column-2] == "H":
                    player_board[row][column] = player_board[row][column-1] = player_board[row][column-2] = "S"
                    guess_board[row][column] = guess_board[row][column-1] = guess_board[row][column-2] = "S"
                    return guess_board    
            except IndexError:
                pass  
            return guess_board
        else:
            print("Try another one, seems it wasn't a valid input")

# returneaza true sau false
def win_condition(board, board_size):
    counter = 0
    for row in board:
        if "T" not in row:
            counter += 1
        else:
            pass
            
    if counter == board_size:
        return True
    else:
        return False 

# returneaza true sau false
def tie_condition(turns, counter):
    if turns == counter:
        return True
    else:
        return False

# Optional
def play_with_AI():
    pass


def main():
    pass
