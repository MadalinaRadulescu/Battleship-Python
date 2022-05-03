
# returneaza player_versus
def get_game_mode():

    while True:
        player_versus = input(" Choose your gamemode:\n 1- Player vs Player\n 2- Player vs AI\n ")
        if player_versus =="1" or player_versus =="2":
            return player_versus
        else:
            print("Choose between 1 and 2")

# returneaza board_size
def get_board_size():
    
    while True:
        board_size = input("Choose the board size between 5 and 10")
        if int(board_size) in range(5,11):
            return board_size
        else:
            print("Please choos a valid board size!")

# returneaza ships_number
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


# returneaza board
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

# returneaza ships
def generate_ships(ships_number):

    ships = []
    for ship in range(ships_number):
        ship_creator = []
        for ship_part in range(3):
            ship_part = "T"
            ship_creator.append(ship_part)
        ships.append(ship_creator)

    return ships

# returneaza player_coordinates
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
def validate_ship_position(row,column, board):
    
    while True:
        pass
        
            
    

# return board
def place_ships(ships, board, board_size):
    pass

# return board
def spacing_ships(board):
    pass

# return hidden board
def update_board_after_shoot(player_board, hidden_board, board_size):
    pass

# returneaza true sau false
def win_condition(player_one_board, player_two_board):
    pass

# returneaza true sau false
def tie_condition(turns, counter):
    pass


def play_with_AI():
    pass


def main():
    pass