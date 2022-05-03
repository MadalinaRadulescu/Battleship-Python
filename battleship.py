
# returneaza player_versus
def get_game_mode():

    while True:
        player_versus = input(" Choose your gamemode:\n 1- Player vs Player\n 2- Player vs AI\n ")
        try:
            if player_versus in ["1","2"]:
                return player_versus
            else:
                print("Choose between 1 and 2")
        except ValueError:
            print("Choose a valid number")


# returneaza board_size int de input
def get_board_size():
    
    while True:
        board_size = input("Choose the board size between 5 and 10")
        try:
            if int(board_size) in range(5,11):
                return board_size
            else:
                print("Please choos a valid board size!")
        except ValueError:
            print("\nPlease choose a valid board size!\n")

# returneaza ships_number integer input
def get_ships_number():

    while True:
        ships_number = input("Choose the number of ships between 1 and 3:  ")
        try:
            if int(ships_number) in range(1,4):
                return ships_number
            else:
                print("Please choose a correct number(1 to 3)")
        except ValueError:
            print("Please choose a correct number(1 to 3)")

# returneaza turns_number
def get_turns_to_play():
    
    while True:
        turns_number = input("How many turns would you like to play? Choose a number between 5 and 50.")
        try:
            if int(turns_number) in range(5,51):
                return turns_number
            else:
                print("Please choose a valid number of turns")
        except ValueError:
            print("Please choose a valid number of turns")

# returneaza board lista de liste
def generate_board(board_size):
    
    board = []
    for i in range(board_size):
        i = []
        board.append(i)
        for j in range(board_size):
            j = ["-"]
            i.append(j)

    return board

# printeazaz boardul
def print_board(board, board_size):

    letters = " ABCDEFGHIJ"
    first_row = "  "
    n = 0
    for i in range(1,board_size+1):
        first_row+= " "
        first_row+=(" ".join(str(i)))
        
    print(f"\n{first_row}\n")
    for i in board:
        n += 1
        print(str(letters[n])+ "  " + " ".join(i))

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
        try:
            if player_cordinates:
                if player_cordinates[0] in letters[:board_size] and int(player_cordinates[1]) in numbers:
                    return tuple((ord(player_cordinates[0])-65, ord(player_cordinates[1])-49))
                else:
                    print("That's not a valid input! Try again !")
            else:
                print("Not valid input ! ")
        except ValueError:
            print("\nPlease insert valid coordinates\nExample - A10\nFirst the column - 'A', second the row '10' \n")



# returneaza ship_direction, valid_direction
def validate_ship_position(row, column, board):

    ship_direction = "\nNow, please select the direction you want the ship to go"
    valid_directions = ""
    while True:
        try:
            if board[row][column] == "-" and board[row+1][column] == "-" and board[row+2][column] == "-" and row+1<len(board[0]) and row+2<len(board[0]):
                ship_direction  += "\n1-Down"
                valid_directions += "1"
        except IndexError:
            pass
        try:
            if board[row][column] == "-" and board[row][column+1] == "-" and board[row][column+2] == "-" and column+1<len(board[0]) and column+2<len(board[0]):
                ship_direction += "\n2-Right"
                valid_directions += "2"
        except IndexError:
            pass
        try :
            if board[row][column] == "-" and board[row-1][column] == "-" and board[row-2][column] == "-" and row-1>=0 and row-2>=0:
                ship_direction += "\n3-Up"
                valid_directions += "3"
        except IndexError:
            pass
        try:
            if board[row][column] == "-" and board[row][column-1] == "-" and board[row][column-2] == "-" and column-1>=0 and column-2>=0:
                ship_direction  += "\n4-Left"
                valid_directions += "4"
        except IndexError:
            pass

        return ship_direction,valid_directions

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
    pass

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
