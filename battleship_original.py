from random import randint, random, choice
import time
from wsgiref.util import shift_path_info

# de facut print pt ambele boarduri in paralel
# timesleep pentru partile unde joaca ai-ul
# ai
# bug, ramane blocat pe linia 392 si nu iese din else
# bug, daca e o nava cu toate caracterele H(hit) in loc de T(turned), nu se schimba in S(sunk)
# de facut AI vs AI

# returneaza player_versus
def get_game_mode():

    difficulty_of_AI=""
    while True:
        player_versus = input(" Choose your gamemode:\n 1- Player vs Player\n 2- Player vs AI\n 3- AI vs AI \n")
        try:
            if player_versus == "1":
                return player_versus, difficulty_of_AI
            elif player_versus == "2":
                difficulty_of_AI = input("Please select the difficulty of AI\n 1- I want to have fun\n 2- DESTROY ME!\n")
                if difficulty_of_AI in ["1", "2"]:
                    return player_versus, difficulty_of_AI
            elif player_versus == "3":
                return player_versus, difficulty_of_AI
            else:
                print("Choose between 1, 2 and 3")
        except ValueError:
            print("Choose a valid number")

# returneaza board_size int de input
def get_board_size():
    
    while True:
        board_size = input("Choose the board size between 5 and 10\n")
        try:
            if int(board_size) in range(5,11):
                return int(board_size)
            else:
                print("Please choos a valid board size!\n")
        except ValueError:
            print("\nPlease choose a valid board size!\n")

# returneaza ships_number integer input
def get_ships_number():

    while True:
        ships_number = input("Choose the number of ships between 1 and 3:\n")
        try:
            if int(ships_number) in range(1,4):
                break
            else:
                print("Please choose a correct number(1 to 3)\n")
        except ValueError:
            print("Please choose a correct number(1 to 3)\n")

    n=0
    ships_length = []
    for ship in range(int(ships_number)):
        n+=1       
        while True:
            ship_length = input(f"How big you want the ship number {n}/{ships_number} (1-4)?\n")
            try:
                if int(ship_length) in range(1, 5):
                    ships_length.append(int(ship_length))
                    break
            except ValueError:
                print("Oops, this is not in range, please try again.\n")

    return int(ships_number), ships_length

# returneaza turns_number
def get_turns_to_play(ships_lenght):
    
    minimum_turns = sum(ships_lenght)
    while True:
        turns = input(f"How many turns would you like to play? Choose a number between {minimum_turns} and 50\n")
        try:
            if int(turns) in range(minimum_turns,51):
                return int(turns)
            elif int(turns) == 0:
                turns = 100
                return int(turns)
            else:
                print("Please choose a valid number of turns\n")
        except ValueError:
            print("Please choose a valid number of turns\n")

# returneaza board lista de liste
def generate_board(board_size):
    
    board = []
    for i in range(board_size):
        i = []
        board.append(i)
        for j in range(board_size):
            j = "-"
            i.append(j)

    return board

# printeazaz boardul
def print_board(board, board_size):

    letters = " ABCDEFGHIJ"
    first_row = "  "
    n = 0
    for i in range(1,board_size+1):
        
        first_row+= " "
        if i > 9 :
            first_row+=("".join(str(i)))
        else:        
            first_row+=(" ".join(str(i)))
        
    print(f"\n{first_row}")
    for i in board:
        n += 1
        print(str(letters[n])+ "  " + " ".join(i))

# returneaza ships o lista de liste
def generate_ships(ships_number=3, ship_length=[3,3,2]):
    
    n=0
    ships = []
    for ship in range(ships_number):
        ship = (["T"]*ship_length[n])
        ships.append(ship)
        n+=1

    return ships

# returneaza player_coordinates  2 cifre coordonate
def get_coordinates(board_size):

    letters = "ABCDEFGHIJKL"
    numbers = range(1, board_size+1)
    while True:
        player_cordinates = input("\nPlease select coordinates:\n").upper()
        try:
            if player_cordinates:
                print(player_cordinates)
                try:
                    if player_cordinates[0] in letters[:board_size] and int(player_cordinates[1:]) in numbers:
                        if int(player_cordinates[1:]) > 9 : 
                            return tuple((ord(player_cordinates[0])-ord("A"), 9))
                        else:                       
                            return tuple((ord(player_cordinates[0])-ord("A"), ord(player_cordinates[1:])-ord("1")))
                except IndexError:
                    pass
                else:
                    print("That's not a valid input! Try again!\n")
            else:
                print("Not valid input!\n")
        except ValueError:
            print("\nPlease insert valid coordinates\nExample - A10\nFirst the column - 'A', second the row '10' \n")

# cand o sa fie turn-ul pentru playeri reali, se v-a declara ca variabila user_choice = numele functiei
def get_ship_direction(ship_direction):

    user_choice = input(ship_direction)

    return user_choice

# cand o sa fie turn-ul pentru computer, se v-a declara ca variabila user_choice = numele functiei
def get_ship_direction_AI(valid_directions):
    
    time.sleep(1)
    return choice(valid_directions) 
    
# return board
def place_ships(ships, board, board_size, player_versus,counter):

    print_board(board,board_size)
    for ship in ships:
        while True:
            if player_versus == "1":
                row, column = get_coordinates(board_size)
            elif player_versus == "2":
                if counter % 2 == 0:
                    row, column = get_coordinates(board_size)
                elif counter % 2 == 1:
                    row, column = play_with_AI(board_size, player_versus, counter)
            elif player_versus == "3":
                row, column = play_with_AI(board_size, player_versus, counter)
             
            ship_direction,valid_directions = validate_ship_position(row,column,board,ship)
            if ship_direction != "\nNow, please select the direction you want the ship to go\n":
                while True:
                    c=0
                    try:
                        if len(ship) == 1:
                            user_choice = ""
                            pass
                        else:
                            if player_versus == "1":
                                user_choice = get_ship_direction(ship_direction)
                            elif player_versus == "2":
                                if counter % 2 == 0:
                                    user_choice = get_ship_direction(ship_direction)
                                elif counter % 2 == 1:
                                    user_choice = get_ship_direction_AI(valid_directions)
                            elif player_versus == "3":
                                user_choice = get_ship_direction_AI(valid_directions)
                        if user_choice in valid_directions or len(ship) == 1:
                            if len(ship) == 1:
                                board[row][column] = "T"
                                break
                            if user_choice == "1":
                                for i in ship:
                                    board[row+c][column] = "T"
                                    c+=1
                                break                        
                            elif user_choice == "2":
                                for i in ship:                                
                                    board[row][column+c] = "T" 
                                    c+=1
                                break
                            elif user_choice == "3":
                                for i in ship:
                                    board[row-c][column] = "T"                             
                                    c+=1
                                break
                            elif user_choice == "4":
                                for i in ship:
                                    board[row][column-c] = "T" 
                                    c+=1
                                break
                    except IndexError:
                        pass

                    else:
                        if player_versus == "1":
                            print("Please make a valid input\n")

                spacing_ships(board)
                print_board(board, board_size)
                break

            else:
                print("\nPlease try again, looks like there wasn't enough space for the ship to be placed.\n")

    
    return board

# returneaza ship_direction, valid_direction
def validate_ship_position(row, column, board,ship):

    ship_direction = "\nNow, please select the direction you want the ship to go\n"
    valid_directions = ""
    while True:
        
        try:
            c=0
            valid_position=0
            for i in ship:
                if board[row+c][column] == "-":
                    valid_position+=1
                c+=1
            if valid_position == len(ship) and row+1<len(board[0]) and row+2<len(board[0]):
                ship_direction  += "\n1-Down"
                valid_directions += "1"
            
        except IndexError:
            pass

        try:
            c=0
            valid_position=0
            for i in ship:
                if board[row][column+c] == "-":
                    valid_position+=1
                c+=1
            if valid_position == len(ship) and column+1<len(board[0]) and column+2<len(board[0]):
                ship_direction += "\n2-Right"
                valid_directions += "2"
                      
        except IndexError:
            pass

        try :
            c=0
            valid_position=0 
            for i in ship:
                if board[row-c][column] == "-":
                    valid_position += 1
                c += 1
            if valid_position == len(ship) and row-(len(ship)-1)>=0:
                ship_direction += "\n3-Up"
                valid_directions += "3"
            
        except IndexError:
            pass

        try:
            c=0
            valid_position=0
            for i in ship:
                if board[row][column-c] == "-":
                    valid_position += 1
                c+=1
            if valid_position == len(ship) and column-(len(ship)-1)>=0:
                ship_direction  += "\n4-Left"
                valid_directions += "4"
            
        except IndexError:
            pass

        return ship_direction,valid_directions

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
def update_board_after_shoot(player_board, guess_board, board_size, player_versus, counter,ships_length):

    while True:
        if player_versus == "1":
                row, column = get_coordinates(board_size)
        elif player_versus == "2":
            if counter % 2 == 0:
                row, column = get_coordinates(board_size)
            elif counter % 2 == 1:
                row, column = play_with_AI(board_size, player_versus, counter)
        elif player_versus == "3":
            row, column = play_with_AI(board_size, player_versus, counter)
                
        # switch_hits_to_sunk(row,player_board,guess_board, ships_length)

        try:
            if player_board[row][column] in ["-", "Z"]:
                player_board[row][column] = "o"
                guess_board[row][column] = "o"
                print("\nyou've missed this time!")
                return guess_board
        
            elif player_board[row][column] == "T":
                player_board[row][column] = "H"
                guess_board[row][column] = "H"    
                print("\nYou got a shot!")
                return guess_board
            
        except IndexError:
            pass
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

    if turns == counter//2:
        return True
    else:
        return False

# Optional
# Hits este o variabila care se declara inainte de inceperea jocului, in partea de AI.
# Ea da count pentru fiecare Hit de pe tabla inamicului
# Prima oara se compara pentru validare, dupa ce vede daca hits venit din afara este mai mare 
# Decat cel care e in interiorul functiei
def play_with_AI(board_size, player_versus, counter,hits=1,p_hits=1, player_one_guess_board=5, difficulty_of_AI="1"):
    
    time.sleep(1)
    if player_versus == "2":
        if difficulty_of_AI == "1":

            coordinates_validation_list = []
            while True:
                coordinates = randint(0,board_size),randint(0,board_size)
                if coordinates not in coordinates_validation_list:
                    coordinates_validation_list.append(coordinates)
                    return coordinates  
    if player_versus == "3":
        if counter % 2 == 0:
            coordinates_validation_list = []
            while True:
                coordinates = randint(0,board_size),randint(0,board_size)
                if coordinates not in coordinates_validation_list:
                    coordinates_validation_list.append(coordinates)
                    return coordinates 
        elif counter % 2 == 1:
            coordinates_validation_list_two = []
            while True:
                coordinates = randint(0,board_size),randint(0,board_size)
                if coordinates not in coordinates_validation_list_two:
                    coordinates_validation_list_two.append(coordinates)
                    return coordinates
        
def print_paralel_board(board_size, player_one_guess_board, player_two_guess_board, name, name_two):

    letters = " ABCDEFGHIJ"
    first_row = "  "
    new_str = " "
    space_var = " "* (board_size-4)
    n = 0
    for i in range(1,board_size+1):
        first_row+= " "
        if i < 10:
            first_row+=(" ".join(str(i)))
        else:
            first_row+=("".join(str(i)))
        
    c = 0
    for i in new_str:
        print(f"\n{space_var}{name}{space_var} {name_two}{space_var}\n")
        print(f"{first_row}   {first_row}")
    for i in player_one_guess_board:
        c += 1
        print(str(letters[c])+ "  " + " ".join(player_one_guess_board[n])+ "   " + str(letters[c])+ "  " + " ".join(player_two_guess_board[n]))
        n += 1

def check_row(row,ships_lenght, player_board):
    
    counter_of_H = 0
    biggest_ship = max(ships_lenght)

    index=0
    for i in player_board[row]:
        ship_to_sunk = []
        counter=1
        if i == "Z":            
            for j in range(biggest_ship+1):
                if player_board[row][index+counter] == "H":
                    counter_of_H +=1
                    ship_to_sunk.append(index+counter)
                if player_board[row][index+counter] == "T":
                    counter_of_H = 0
                    ship_to_sunk = []
                    return  ship_to_sunk
                if player_board[row][index+counter] == "Z" and counter_of_H > 1:
                    return  ship_to_sunk
                if index+counter is len(row)-1:
                    if player_board[row][index+counter]=="H":
                        return  ship_to_sunk
                counter+=1
        if i == "H":
            counter = 0
            for j in range(biggest_ship+1):
                if player_board[row][index+counter] == "H":
                    counter_of_H +=1
                    ship_to_sunk.append(index+counter)
                if player_board[row][index+counter] == "T":
                    counter_of_H = 0
                    ship_to_sunk = []
                    return  ship_to_sunk
                if player_board[row][index+counter] == "Z" and counter_of_H > 1:
                    return  ship_to_sunk
                counter+=1
        index+=1

def check_column(player_board, ship_lenght):
    
    counter_of_H = 0
    biggest_ship = max(ship_lenght)
    index_r = 0
    for row in player_board:
        index_c = 0
        for space in row:
            ship_to_sunk = []
            counter = 1
            if player_board[index_r][index_c] == "Z":
                for j in range(biggest_ship+1):
                    if player_board[index_r][index_c] == "H":
                        counter_of_H += 1
                        ship_to_sunk.append(tuple(player_board[index_r][index_c]))
                    if player_board[index_r][index_c] == "T":
                        counter_of_H = 0
                        ship_lenght = []
                        return ship_to_sunk
                    if player_board[index_r][index_c] == "Z" and counter_of_H > 1:
                        return ship_to_sunk
                    if index_c is len(row)-1:
                        if player_board[index_r][index_c] == "H":
                            return ship_to_sunk
                    counter+=1
            if player_board[index_r][index_c] == "H":
                counter = 0
                for j in range(biggest_ship+1):
                    if player_board[index_r][index_c] == "H":
                        counter_of_H += 1
                        ship_to_sunk.append(tuple(player_board[index_r][index_c]))
                    if player_board[index_r][index_c] == "T":
                        counter_of_H = 0
                        ship_lenght = []
                        return ship_to_sunk
                    if player_board[index_r][index_c] == "Z" and counter_of_H > 1:
                        return ship_to_sunk
                    if len(index_c) is len(row)-1:
                        if player_board[index_r][index_c] == "H":
                            return ship_to_sunk
                    counter+=1
        index_r+=1

def switch_hits_to_sunk(row,player_board, player_guess_board, ship_lenght):

    ship_to_sunk = check_row(row, ship_lenght,player_board)

    counter = 0
    if ship_to_sunk != []:
        for i in ship_to_sunk:
            player_board[row][counter] == "S"
            player_guess_board[row][counter] == "S"
            counter += 1

    counter = 0
    ship_to_sunk = check_column(player_board, ship_lenght)
    if ship_to_sunk != []:
        for i in ship_to_sunk:
            x,y = ship_to_sunk[counter]
            player_board[x][y] = "S"
            player_guess_board[x][y] = "S"
            counter += 1


        

def main():
    
    player_versus, difficulty_of_AI = get_game_mode()
    board_size = get_board_size()
    ships_number, ships_length = get_ships_number()
    turns = get_turns_to_play(ships_length)

    player_one_board = generate_board(board_size)
    player_one_guess_board = generate_board(board_size)
    player_one_ships = generate_ships(ships_number,ships_length)

    player_two_board = generate_board(board_size)
    player_two_guess_board = generate_board(board_size)
    player_two_ships = generate_ships(ships_number,ships_length)
    
    
 # to remove, not needed cause it is called later - updated removed
    
    counter = 0
    if player_versus == "1":
        name = input("What's your name, player one?\n") 
        print(f'{name}, it is time to make your tactics') 
        place_ships(player_one_ships, player_one_board, board_size, player_versus, counter)

        name_two = input("What's your name, player two?\n")
        print(f'{name_two}, it is time to make your tactics') 
        place_ships(player_two_ships, player_two_board, board_size, player_versus, counter)
    
    elif player_versus == "2":
        name = input("What's your name, player one?\n") 
        print(f'{name}, it is time to make your tactics') 
        place_ships(player_one_ships, player_one_board, board_size, player_versus, counter)
        counter = 1
        name_two = "the computer"
        place_ships(player_two_ships, player_two_board, board_size, player_versus, counter)
        print(f"You are playing against {name_two}")

    elif player_versus == "3":
        name = "Anos Voldigoad"
        place_ships(player_one_ships, player_one_board, board_size, player_versus, counter)
        print(f"You are playing against {name}")
        name_two = "Silver Surfer"
        place_ships(player_two_ships, player_two_board, board_size, player_versus, counter)
        print(f"You are playing against {name_two}")

        
    counter = 0
    while True:
        print(f"Number of turn: {counter//2} out of {turns}")

        if player_versus == "1":
            if counter % 2 == 0:
                print(f"\nIt's time for {name} to shoot")
                print_paralel_board(board_size, player_one_guess_board, player_two_guess_board, name, name_two)
                update_board_after_shoot(player_two_board,player_two_guess_board, board_size, player_versus, counter, ships_length)
                if win_condition(player_two_board, board_size):
                    print_paralel_board(board_size, player_one_guess_board, player_two_guess_board, name, name_two)
                    print(f"{name}, you have won!")
                    break
            
            # Player 2
            if counter % 2 == 1:
                print(f"\nIt's time for {name_two} to shoot")
                print_paralel_board(board_size, player_one_guess_board, player_two_guess_board, name, name_two)
                update_board_after_shoot(player_one_board,player_one_guess_board, board_size, player_versus, counter,ships_length)
                if win_condition(player_one_board, board_size):
                    print_paralel_board(board_size, player_one_guess_board, player_two_guess_board, name, name_two)
                    print(f"{name_two}, you have won!")
                    break
        
        if player_versus == "2":
            if counter % 2 == 0:
                print(f"\nIt's time for {name} to shoot")
                print_paralel_board(board_size, player_one_guess_board, player_two_guess_board, name, name_two)
                update_board_after_shoot(player_two_board,player_two_guess_board, board_size, player_versus, counter, ships_length)
                if win_condition(player_two_board, board_size):
                    print_paralel_board(board_size, player_one_guess_board, player_two_guess_board, name, name_two)
                    print(f"{name}, you have won!")
                    break
            if counter % 2 == 1:
                print(f"\nIt's time for {name_two} to shoot")
                print_paralel_board(board_size, player_one_guess_board, player_two_guess_board, name, name_two)
                update_board_after_shoot(player_one_board,player_one_guess_board, board_size, player_versus, counter, ships_length)
                if win_condition(player_two_board, board_size):
                    print_paralel_board(board_size, player_one_guess_board, player_two_guess_board, name, name_two)
                    print(f"{name_two} has won")
                    break
        
        if player_versus == "3":
            if counter % 2 == 0:
                print(f"\nIt's time for {name} one to shoot")
                print_paralel_board(board_size, player_one_guess_board, player_two_guess_board, name, name_two)
                update_board_after_shoot(player_two_board,player_two_guess_board, board_size, player_versus, counter, ships_length)
                if win_condition(player_two_board, board_size):
                    print_paralel_board(board_size, player_one_guess_board, player_two_guess_board, name, name_two)
                    print("Ano Voldigord has won")
                    break
            if counter % 2 == 1:
                print(f"\nIt's time for {name_two} two to shoot")
                print_paralel_board(board_size, player_one_guess_board, player_two_guess_board, name, name_two)
                update_board_after_shoot(player_one_board,player_one_guess_board, board_size, player_versus, counter, ships_length)
                if win_condition(player_two_board, board_size):
                    print_paralel_board(board_size, player_one_guess_board, player_two_guess_board, name, name_two)
                    print(f"{name_two} has won")
                    break

        if tie_condition(turns, counter):
            print_paralel_board(board_size, player_one_guess_board, player_two_guess_board, name, name_two)
            print("\nIt's a tie!\n")
            break

        counter+=1

    


if __name__ == "__main__":

    main()
