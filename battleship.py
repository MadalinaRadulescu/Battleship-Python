
# returneaza player_versus
def get_game_mode():

    while True:
        player_versus = input(" Choose your gamemode:\n 1- Player vs Player\n 2- Player vs AI\n ")
        if player_versus =="1" or player_versus =="2":
            return player_versus
        else:
            print("Choose between 1 and 2")


# returneaza board_size int de input
def get_board_size():
    
    while True:
        board_size = input("Choose the board size between 5 and 10")
        if int(board_size) in range(5,11):
            return board_size
        else:
            print("Please choos a valid board size!")

# returneaza ships_number integer input
def get_ships_number():

    while True:
        ships_number = input("Choose the number of ships between 1 and 3:  ")
        if int(ships_number) in range(1,4):
            return ships_number
        else:
            print("Please choose a correct number(1 to 3)")

# returneaza turns_number
def get_turns_to_play():
    
    while True:
        turns_number = input("How many turns would you like to play? Choose a number between 5 and 50.")
        if int(turns_number) in range(5,51):
            return turns_number
        else:
            print("Please choose a valid number of turns")


# returneaza board lista de liste
def generate_board(board_size):
    
    board = []
    for i in range(board_size):
        i = []
        board.append(i)
        for j in range(i):
            j = ["-"]
            i.append(j)

    return board

# printeazaz boardul
def print_board(board, board_size):
    pass

# returneaza ships o lista de liste
def generate_ships(ships_number):

    ships = []
    for ship in range(ships_number):
        ship_creator = []
        for ship_part in range(3):
            ship_part = "T"
            ship_creator.append(ship_part)
        ships.append(ship_creator)

    return ships

# returneaza player_coordinates  2 cifre coordonate
def get_coordinates(board_size):
    letters = "ABCDEFGHIJ"
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    while True:
        player_cordinates = input("\nPlease select coordinates:\n").upper()
        if player_cordinates:
            if player_cordinates[0] in letters[:board_size] and int(player_cordinates[1]) in numbers:
                return tuple((ord(player_cordinates[0])-65, ord(player_cordinates[1])-49))
            else:
                print("That's not a valid input! Try again !")
        else:
            print("Not valid input ! ")



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
def update_board_after_shoot(player_board, guess_board, board_size,user_coordinates):
    while True:
        coordinates =user_coordinates #aici o sa fie functia care o sa dea coordonatele de la player sau de la AI
        row = ord(coordinates[0]) - ord("a")
        column = int(coordinates[1])-1
        if player_board[row][column] == "-":
            player_board[row][column] = "o"
            guess_board[row][column] = "o"
            print("you've missed this time!")
            print_board(guess_board, board_size)
            return guess_board
        elif player_board[row][column] == "T":
            player_board[row][column] = "H"
            guess_board[row][column] = "H"    
            print("You got a shot!")
            print_board(guess_board, board_size)
        elif player_board[row][column] == "Z":
            player_board[row][column] = "o"
            guess_board[row][column] = "o"
            print("you've missed this time!")
            print_board(guess_board, board_size)
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




if __name__ == "__main__":

    main()
