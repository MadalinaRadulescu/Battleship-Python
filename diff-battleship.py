from random import randint, choice
import time

# bug, daca e o nava cu toate caracterele H(hit) in loc de T(turned), nu se schimba in S(sunk)

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

def get_board_size():
    
    while True:
        board_size = input("Choose the board size between 5 and 10\n")
        try:
            int_board = int(board_size)
            if int_board in range(5,11):
                return int_board
            else:
                print("Please choos a valid board size!\n")
        except ValueError:
            print("\nPlease choose a valid board size!\n")

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
                int_ship_lenght =int(ship_length)
                if int_ship_lenght in range(1, 5):
                    ships_length.append(int_ship_lenght)
                    break
            except ValueError:
                print("Oops, this is not in range, please try again.\n")

    return int(ships_number), ships_length

def get_turns_to_play(ships_lenght):
    
    minimum_turns = sum(ships_lenght)
    while True:
        turns = input(f"How many turns would you like to play? Choose a number between {minimum_turns} and 50\n")
        try:
            int_turns = int(turns)
            if int_turns in range(minimum_turns,51):
                return int_turns
            elif int_turns == 0:
                int_turns = 100
                return int_turns
            else:
                print("Please choose a valid number of turns\n")
        except ValueError:
            print("Please choose a valid number of turns\n")

def generate_board(board_size):
    
    board = []
    for _ in range(board_size):
        row = []
        board.append(row)
        for _ in range(board_size):
            space = "-"
            row.append(space)

    return board

def print_board(board, board_size):

    # letters = " ABCDEFGHIJ"
    first_row = "  "
    n = 0
    for i in range(1,board_size+1):     
        first_row+=" "+str(i)
        
    print(f"\n{first_row}")
    for i in board:        
        print(chr(n+65)+ "  " + " ".join(i))
        n += 1

def generate_ships(ships_number=3, ship_length=[3,3,2]):
    
    ships = []
    for n in range(ships_number):
        ship = (["T"]*ship_length[n])
        ships.append(ship)    

    return ships

def get_coordinates(board_size):

    letters = "ABCDEFGHIJKL"
    numbers = range(1, board_size+1)
    while True:
        player_cordinates = input("\nPlease select coordinates:\n").upper()
        try:
            if player_cordinates:
                try:
                    if player_cordinates[0] in letters[:board_size] and int(player_cordinates[1:]) in numbers:                    
                            return tuple((ord(player_cordinates[0])-ord("A"), int(player_cordinates[1:])-1))
                except IndexError:
                    pass
                else:
                    print("That's not a valid input! Try again!\n")
            else:
                print("Not valid input!\n")
        except ValueError:
            print("\nPlease insert valid coordinates\nExample - A10\nFirst the column - 'A', second the row '10' \n")

def get_ship_direction(ship_direction):

    user_choice = input(ship_direction)

    return user_choice

def get_ship_direction_AI(valid_directions):
    
    time.sleep(1)
    return choice(valid_directions) 
    
def place_ships_human(ships, board, board_size, player_versus,counter):

    print_board(board,board_size)
    ships_placed_coordinates = []
    ships_coordinates_on_map = []
    temporary = tuple()   
    
    for ship in ships:
        while True:
            if player_versus == "1":
                row, column = get_coordinates(board_size)
            elif player_versus == "2":
                if counter % 2 == 0:
                    row, column = get_coordinates(board_size)
             
            ship_direction,valid_directions = validate_ship_position(row,column,board,ship)
            if ship_direction != "\nNow, please select the direction you want the ship to go\n":
                while True:
                    c=0
                    try:

                        if player_versus == "1":
                            user_choice = get_ship_direction(ship_direction)
                        elif player_versus == "2":
                            if counter % 2 == 0:
                                user_choice = get_ship_direction(ship_direction)


                        if user_choice in valid_directions or len(ship) == 1:
                            if user_choice == "0":
                                board[row][column] = "T"
                                temporary = (row+c,column)
                                ships_placed_coordinates.append(temporary)
                                c+=1
                                ships_coordinates_on_map.append(ships_placed_coordinates)
                            if user_choice == "1":
                                ships_placed_coordinates = []
                                for i in ship:
                                    board[row+c][column] = "T"
                                    temporary = (row+c,column)
                                    ships_placed_coordinates.append(temporary)
                                    c+=1
                                ships_coordinates_on_map.append(ships_placed_coordinates)
                                break                        
                            elif user_choice == "2":
                                ships_placed_coordinates = []
                                for i in ship:                                
                                    board[row][column+c] = "T"
                                    temporary = (row,column+c)
                                    ships_placed_coordinates.append(temporary)
                                    c+=1
                                ships_coordinates_on_map.append(ships_placed_coordinates)
                                break
                            elif user_choice == "3":
                                ships_placed_coordinates = []
                                for i in ship:
                                    board[row-c][column] = "T"                           
                                    temporary = (row-c,column)
                                    ships_placed_coordinates.append(temporary)
                                    c+=1
                                ships_coordinates_on_map.append(ships_placed_coordinates)
                                break
                            elif user_choice == "4":
                                ships_placed_coordinates = []
                                for i in ship:
                                    board[row][column-c] = "T"
                                    temporary = (row,column-c)
                                    ships_placed_coordinates.append(temporary)
                                    c+=1
                                ships_coordinates_on_map.append(ships_placed_coordinates)
                                break

                    except IndexError:
                        pass

                    else:
                            print("Please make a valid input\n")

                spacing_ships(board)
                print_board(board, board_size)
                break

            else:
                print("\nPlease try again, looks like there wasn't enough space for the ship to be placed.\n")

    
    return board,ships_coordinates_on_map

def place_ships_AI(ships, board, board_size, player_versus,counter):

    print_board(board,board_size)
    ships_placed_coordinates = []
    ships_coordinates_on_map = []
    temporary = tuple()

    for ship in ships:
        while True:
            if player_versus == "2":
                if counter % 2 == 1:
                    row, column = play_with_AI(board_size, player_versus, counter)
            elif player_versus == "3":
                row, column = play_with_AI(board_size, player_versus, counter)
             
            ship_direction,valid_directions = validate_ship_position(row,column,board,ship)
            if ship_direction != "\nNow, please select the direction you want the ship to go\n":
                while True:
                    c=0
                    try:
                        
                        if player_versus == "2":
                            if counter % 2 == 1:
                                user_choice = get_ship_direction_AI(valid_directions)
                        elif player_versus == "3":
                            user_choice = get_ship_direction_AI(valid_directions)
                            

                        if user_choice in valid_directions or len(ship) == 1:
                            if user_choice == "0":
                                board[row][column] = "T"
                                temporary = (row+c,column)
                                ships_placed_coordinates.append(temporary)
                                ships_coordinates_on_map.append(ships_placed_coordinates)
                                return board,ships_coordinates_on_map
                            if user_choice == "1":
                                ships_placed_coordinates = []
                                for i in ship:
                                    board[row+c][column] = "T"
                                    temporary = (row+c,column)
                                    ships_placed_coordinates.append(temporary)
                                    c+=1
                                ships_coordinates_on_map.append(ships_placed_coordinates)
                                break                        
                            elif user_choice == "2":
                                ships_placed_coordinates = []
                                for i in ship:                                
                                    board[row][column+c] = "T"
                                    temporary = (row,column+c)
                                    ships_placed_coordinates.append(temporary)
                                    c+=1
                                ships_coordinates_on_map.append(ships_placed_coordinates)
                                break
                            elif user_choice == "3":
                                ships_placed_coordinates = []
                                for i in ship:
                                    board[row-c][column] = "T"                           
                                    temporary = (row-c,column)
                                    ships_placed_coordinates.append(temporary)
                                    c+=1
                                ships_coordinates_on_map.append(ships_placed_coordinates)
                                break
                            elif user_choice == "4":
                                ships_placed_coordinates = []
                                for i in ship:
                                    board[row][column-c] = "T"
                                    temporary = (row,column-c)
                                    ships_placed_coordinates.append(temporary)
                                    c+=1
                                ships_coordinates_on_map.append(ships_placed_coordinates)
                                break
                    except IndexError:
                        pass

                spacing_ships(board)
                print_board(board, board_size)
                break
    
    return board,ships_coordinates_on_map

def validate_ship_position(row, column, board,ship):

    ship_direction = "\nNow, please select the direction you want the ship to go\n"
    valid_directions = ""
    while True:
        if len(ship)==1:
            ship_direction  += "\n0-Just put it!"
            valid_directions += "0"
            return ship_direction,valid_directions
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

def update_board_after_shoot_human(player_board, guess_board, board_size, player_versus, counter,ships_length):

    while True:
        if player_versus == "1":
                row, column = get_coordinates(board_size)
        elif player_versus == "2":
            if counter % 2 == 0:
                row, column = get_coordinates(board_size)                

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
                # switch_hits_to_sunk(row,player_board,guess_board, ships_length)
                return guess_board
                
            
        except IndexError:
            pass
            
        else:
            print("Try another one, seems it wasn't a valid input")   

def update_board_after_shoot_AI(player_board, guess_board, board_size, player_versus, counter,ships_length):
    while True:
        if player_versus == "2":
           if counter % 2 == 1:
                row, column = play_with_AI(board_size, player_versus, counter)
        elif player_versus == "3":
            row, column = play_with_AI(board_size, player_versus, counter)                

        try:
            if player_board[row][column] in ["-", "Z"]:
                player_board[row][column] = "o"
                guess_board[row][column] = "o"
                print("\nComputer missed this time!")
                return guess_board
        
            elif player_board[row][column] == "T":
                player_board[row][column] = "H"
                guess_board[row][column] = "H"    
                print("\nComputer got a shot!")
                # switch_hits_to_sunk(row,player_board,guess_board, ships_length)
                return guess_board                
            
        except IndexError:
            pass
               
def win_condition(board, board_size):

    counter = 0
    for row in board:
        if "T" not in row:
            counter += 1
        else:
            pass 

    return counter==board_size

def tie_condition(turns, counter):

    if turns == counter//2:
        return True
    else:
        return False

# Play with AI
def play_with_AI(board_size, player_versus, counter, player_guess_board, difficulty_of_AI="1"):
    
    # Hits este o variabila care se declara inainte de inceperea jocului, in partea de AI.
    # Ea da count pentru fiecare Hit de pe tabla inamicului
    # Prima oara se compara pentru validare, dupa ce vede daca hits venit din afara este mai mare 
    # Decat cel care e in interiorul functiei

    time.sleep(1)
    if player_versus == "2":
        if difficulty_of_AI == "1":

            coordinates_validation_list = []
            while True:
                coordinates = randint(0,board_size),randint(0,board_size)
                if coordinates not in coordinates_validation_list:
                    coordinates_validation_list.append(coordinates)
                    return coordinates 

        elif difficulty_of_AI == "2":

            coordinates, board_hits_counter = smart_AI(player_guess_board,coordinates_validation_list,board_hits_counter)

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

    letters = ord("A")
    first_row = "  "
    new_str = " "
    space_var = " "* (board_size-4)
    n = 0
    for i in range(1,board_size+1):
        first_row+= " "+str(i)
        
    c = 0
    for i in new_str:
        print(f"\n{space_var}{name}{space_var}{name_two}{space_var}\n")
        print(f"{first_row}    {first_row}")
    for i in player_one_guess_board:
        
        print(str(chr(letters+c))+ "  " + " ".join(player_one_guess_board[n])+ "    " + str(chr(letters+c))+ "  " + " ".join(player_two_guess_board[n]))
        c += 1
        n += 1

# # # # # # # # # Not Used
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

# # # # # # # # # Not Used
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
                        ship_to_sunk.append((index_r,index_c))
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
                        ship_to_sunk.append((index_r,index_c))
                    if player_board[index_r][index_c] == "T":
                        counter_of_H = 0
                        ship_lenght = []
                        return ship_to_sunk
                    if player_board[index_r][index_c] == "Z" and counter_of_H > 1:
                        return ship_to_sunk
                    if index_c is row:
                        if player_board[index_r][index_c] == "H":
                            return ship_to_sunk
                counter+=1
        index_r+=1

# # # # # # # # # 
def switch_hits_to_sunk(row,player_board, player_guess_board, ship_lenght):

    ship_to_sunk = check_row(row, ship_lenght,player_board)

    counter = 0
    if ship_to_sunk != []:
        for i in ship_to_sunk:
            player_board[row][ship_to_sunk[counter]] == "S"
            player_guess_board[row][ship_to_sunk[counter]] == "S"
            counter += 1

    counter = 0
    ship_to_sunk = check_column(player_board, ship_lenght)
    if ship_to_sunk != []:
        for i in ship_to_sunk:
            x,y = ship_to_sunk[counter]
            player_board[x][y] = "S"
            player_guess_board[x][y] = "S"
            counter += 1

def sunk_ships(player_board, ships_coordinates_on_map,player_guess_board):

    hits_counter = 0

    for ship in ships_coordinates_on_map:
        for ship_part in ship:            
            row = ship_part[0]
            column = ship_part[1]
            if player_board[row][column] == "H":
                hits_counter += 1                    
                if hits_counter == len(ship):
                    for ship_part in ship:
                        row = ship_part[0]
                        column = ship_part[1]
                        player_board[row][column] = "S"
                        player_guess_board[row][column] = "S"
    
# de adaugat o lista cu coordonatele hit de fiecare data cand se loveste un ship si dupa sa se gasesc toate coordonatele sa se reseteze
def perimeter_verification_AI(player_board,board_hits_counter,coordinates_validation_list,turns_without_hit,targeted_ship_coordinates):

    # se analizeaza toate posibilitatile pentru vecinii din jurul partii lovite de nava, se trece dintr-o functie in alata pana se gaseste o alta parte
    def up_verify(player_board,board_hits_counter,coordinates_validation_list,turns_without_hit,targeted_ship_coordinates):

        if board_hits_counter > inside_hits_counter and column-1>=0 and player_board[row-1][column] == "-":
            inside_hits_counter = board_hits_counter
            row,column = coordinates_validation_list[-1]
            coordinates = row-1,column
            targeted_ship_coordinates.append(coordinates)
            return coordinates, inside_hits_counter, targeted_ship_coordinates
        elif turns_without_hit == 1 and column-1>=0 and player_board[row-1][column] == "-":
            row,column = coordinates_validation_list[-2]
            coordinates = row-1,column
            targeted_ship_coordinates.append(coordinates)
            return coordinates, inside_hits_counter, targeted_ship_coordinates
        elif turns_without_hit == 2 and column-1>=0 and player_board[row-1][column] == "-":
            row,column = coordinates_validation_list[-3]
            coordinates = row-1,column
            targeted_ship_coordinates.append(coordinates)
            return coordinates, inside_hits_counter, targeted_ship_coordinates
        elif turns_without_hit == 3 and column-1>=0 and player_board[row-1][column] == "-":
            row,column = coordinates_validation_list[-4]
            coordinates = row-1,column
            targeted_ship_coordinates.append(coordinates)
            return coordinates, inside_hits_counter, targeted_ship_coordinates
        else:
            right_verify(player_board,board_hits_counter,coordinates_validation_list,turns_without_hit)

    def right_verify(player_board,board_hits_counter,coordinates_validation_list,turns_without_hit,targeted_ship_coordinates):

        if board_hits_counter > inside_hits_counter and row+1<len(player_board[0]) and player_board[row][column+1] == "-":
            inside_hits_counter = board_hits_counter
            row,column = coordinates_validation_list[-1]
            coordinates = row,column+1
            targeted_ship_coordinates.append(coordinates)
            return coordinates, inside_hits_counter, targeted_ship_coordinates
        elif turns_without_hit == 1 and row+1<len(player_board[0]) and player_board[row][column+1] == "-":
            row,column = coordinates_validation_list[-2]
            coordinates = row,column+1
            targeted_ship_coordinates.append(coordinates)
            return coordinates, inside_hits_counter, targeted_ship_coordinates
        elif turns_without_hit == 2 and row+1<len(player_board[0]) and player_board[row][column+1] == "-":
            row,column = coordinates_validation_list[-3]
            coordinates = row,column+1
            targeted_ship_coordinates.append(coordinates)
            return coordinates, inside_hits_counter, targeted_ship_coordinates
        elif turns_without_hit == 3 and row+1<len(player_board[0]) and player_board[row][column+1] == "-":
            row,column = coordinates_validation_list[-4]
            coordinates = row,column+1
            targeted_ship_coordinates.append(coordinates)
            return coordinates, inside_hits_counter, targeted_ship_coordinates
        else:
            down_verify(player_board,board_hits_counter,coordinates_validation_list,turns_without_hit)

    def down_verify(player_board,board_hits_counter,coordinates_validation_list,turns_without_hit,targeted_ship_coordinates):

        if board_hits_counter > inside_hits_counter and column+1<len(player_board[0]) and player_board[row+1][column] == "-":
            inside_hits_counter = board_hits_counter
            row,column = coordinates_validation_list[-1]
            coordinates = row+1,column 
            targeted_ship_coordinates.append(coordinates)
            return coordinates, inside_hits_counter, targeted_ship_coordinates
        elif turns_without_hit == 1 and column+1<len(player_board[0]) and player_board[row+1][column]:
            row,column = coordinates_validation_list[-2]
            coordinates = row+1,column
            targeted_ship_coordinates.append(coordinates)
            return coordinates, inside_hits_counter, targeted_ship_coordinates
        elif turns_without_hit == 2 and column+1<len(player_board[0]) and player_board[row+1][column]:
            row,column = coordinates_validation_list[-3]
            coordinates = row+1,column
            targeted_ship_coordinates.append(coordinates)
            return coordinates, inside_hits_counter, targeted_ship_coordinates
        elif turns_without_hit == 3 and column+1<len(player_board[0]) and player_board[row+1][column]:
            row,column = coordinates_validation_list[-4]
            coordinates = row+1,column
            targeted_ship_coordinates.append(coordinates)
            return coordinates, inside_hits_counter, targeted_ship_coordinates
        else:
            left_verify(player_board,board_hits_counter,coordinates_validation_list,turns_without_hit)

    def left_verify(player_board,board_hits_counter,coordinates_validation_list,turns_without_hit,targeted_ship_coordinates):

        if board_hits_counter > inside_hits_counter and row-1>=0 and player_board[row][column-1] == "-":
            inside_hits_counter = board_hits_counter
            row,column = coordinates_validation_list[-1]
            coordinates = row,column-1
            targeted_ship_coordinates.append(coordinates)
            return coordinates, inside_hits_counter, targeted_ship_coordinates
        if turns_without_hit == 3 and row-1>=0:
            row,column = coordinates_validation_list[-2]
            coordinates = row,column-1
            targeted_ship_coordinates.append(coordinates)
            return coordinates, inside_hits_counter, targeted_ship_coordinates
        if turns_without_hit == 3 and row-1>=0:
            row,column = coordinates_validation_list[-3]
            coordinates = row,column-1
            targeted_ship_coordinates.append(coordinates)
            return coordinates, inside_hits_counter, targeted_ship_coordinates
        if turns_without_hit == 3 and row-1>=0:
            row,column = coordinates_validation_list[-4]
            coordinates = row,column-1
            targeted_ship_coordinates.append(coordinates)
            return coordinates, inside_hits_counter, targeted_ship_coordinates
        else:
            up_verify(player_board,board_hits_counter,coordinates_validation_list,turns_without_hit)
        
    coordinates,inside_counter,targeted_ship_coordinates = up_verify(player_board,board_hits_counter,coordinates_validation_list,turns_without_hit,targeted_ship_coordinates)

    return coordinates,inside_counter,targeted_ship_coordinates

def destroy_founded_ship(player_board,targeted_ship_coordinates):

    # daca primul index din elementele din lista targeted_ship_coordinates este aceeasi
    # inseamna ca randul trebuie sa ramana acelasi pana ce toata nava a fost lovita
    if targeted_ship_coordinates[-1][0] == targeted_ship_coordinates[-2][0]:
        row = player_board[targeted_ship_coordinates[-1][0]]
        
        if player_board[row][targeted_ship_coordinates[-1][1]+1] == "-" and targeted_ship_coordinates[-1][1]+1<len(player_board[0]):   # daca este loc in dreapta sa loveasca, v-a lovi 
            column = player_board[row][targeted_ship_coordinates[-1][1]+1]
            targeted_ship_coordinates.append(row,column)
        elif player_board[row][targeted_ship_coordinates[0][1]-1] == "-" and targeted_ship_coordinates[0][1]-1>=0:  # daca nu a gasit loc in dreapta, v-a lovi in stanga
            column = player_board[row][targeted_ship_coordinates[0][1]-1]
            targeted_ship_coordinates.append(row,column)

    # daca al doilea index din coordonatele din lista targeted_ship_coordinates este aceeasi
    # inseamna ca trebuie pastrata coloana si verificat in sus si in jos
    elif targeted_ship_coordinates[-1][1] == targeted_ship_coordinates[-2][1]:
        column = player_board[targeted_ship_coordinates[-1][1]]

        if player_board[targeted_ship_coordinates[-1][0]+1][column] == "-" and targeted_ship_coordinates[-1][0]+1<len(player_board[0]): # daca este loc sa mearga in jos, v-a lovi in jos
            row = player_board[targeted_ship_coordinates[-1][0]+1][column]
            targeted_ship_coordinates.append(row,column)
        elif player_board[targeted_ship_coordinates[0][0]-1][column] == "-" and targeted_ship_coordinates[0][0]-1>=0: # daca nu a gasit loc in jos, v-a lovi in sus
            row = player_board[targeted_ship_coordinates[0][0]-1][column]
            targeted_ship_coordinates.append(row,column)


    return row,column

def count_hits_on_board(player_board):

    board_hits_counter = 0

    for row in player_board:
        for space in row:
            if space == "H":
                board_hits_counter+=1

    return board_hits_counter      

def count_sunk_on_board(player_board):

    sunk_counter = 0

    for row in player_board:
        for space in row:
            if space == "S":
                sunk_counter +=1

    return sunk_counter

def smart_AI(player_board,coordinates_validation_list,board_hits_counter):


    board_hits_counter = count_hits_on_board(player_board)
    sunk_counter = count_sunk_on_board(player_board)

    # daca e prima runda sau daca s-a scufundat o nava, se reseteaza counterii si incepe sa se vaneze urmatoarea pana v-a fii gasita random
    if board_hits_counter - sunk_counter <= 0:
        inside_hits_counter = 0
        turns_without_hit = 0
        # Task 1
        if board_hits_counter == 0:
            coordinates = randint(0,len(player_board)),randint(0,len(player_board))
            if coordinates not in coordinates_validation_list:
                coordinates_validation_list.append(coordinates)
                return coordinates, inside_hits_counter, targeted_ship_coordinates

        # Task 2
    if board_hits_counter == 1:
        coordinates,inside_counter,targeted_ship_coordinates = perimeter_verification_AI(player_board,board_hits_counter,coordinates_validation_list,turns_without_hit,targeted_ship_coordinates)

        # Task 3 si Task 4
    elif board_hits_counter > 1:
        coordinates = destroy_founded_ship(player_board,targeted_ship_coordinates)


 

    return coordinates, board_hits_counter
    
        
        



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
        player_one_board, ships_one_coordinates_on_map = place_ships_human(player_one_ships, player_one_board, board_size, player_versus, counter)

        name_two = input("What's your name, player two?\n")
        print(f'{name_two}, it is time to make your tactics') 
        player_two_board, ships_two_coordinates_on_map = place_ships_human(player_two_ships, player_two_board, board_size, player_versus, counter)
    
    elif player_versus == "2":
        name = input("What's your name, player one?\n") 
        print(f'{name}, it is time to make your tactics') 
        player_one_board, ships_one_coordinates_on_map =place_ships_human(player_one_ships, player_one_board, board_size, player_versus, counter)
        counter = 1

        name_two = "the computer"
        print("\n It's time for computer to place the ships\n")
        player_two_board, ships_two_coordinates_on_map = place_ships_AI(player_two_ships, player_two_board, board_size, player_versus, counter)
        print(f"You are playing against {name_two}")

    elif player_versus == "3":
        name = "Anos Voldigoad"
        player_one_board, ships_one_coordinates_on_map = place_ships_AI(player_one_ships, player_one_board, board_size, player_versus, counter)
        print(f"You are playing against {name}")
        name_two = "Silver Surfer"
        player_two_board, ships_two_coordinates_on_map = place_ships_AI(player_two_ships, player_two_board, board_size, player_versus, counter)
        print(f"You are playing against {name_two}")

        
    counter = 0
    while True:
        print(f"Number of turn: {counter//2} out of {turns}")

        if player_versus == "1":
            if counter % 2 == 0:
                print(f"\nIt's time for {name} to shoot")
                print_paralel_board(board_size, player_one_guess_board, player_two_guess_board, name, name_two)
                update_board_after_shoot_human(player_two_board,player_two_guess_board, board_size, player_versus, counter, ships_length)
                sunk_ships(player_two_board,ships_two_coordinates_on_map,player_two_guess_board)
    
                if win_condition(player_two_board, board_size):
                    print_paralel_board(board_size, player_one_guess_board, player_two_guess_board, name, name_two)
                    print(f"{name}, you have won!")
                    break
            
            # Player 2
            if counter % 2 == 1:
                print(f"\nIt's time for {name_two} to shoot")
                print_paralel_board(board_size, player_one_guess_board, player_two_guess_board, name, name_two)
                update_board_after_shoot_human(player_one_board,player_one_guess_board, board_size, player_versus, counter,ships_length)
                sunk_ships(player_one_board,ships_one_coordinates_on_map,player_one_guess_board)
                if win_condition(player_one_board, board_size):
                    print_paralel_board(board_size, player_one_guess_board, player_two_guess_board, name, name_two)
                    print(f"{name_two}, you have won!")
                    break
        
        if player_versus == "2":
            if counter % 2 == 0:
                print(f"\nIt's time for {name} to shoot")
                print_paralel_board(board_size, player_one_guess_board, player_two_guess_board, name, name_two)
                update_board_after_shoot_human(player_two_board,player_two_guess_board, board_size, player_versus, counter, ships_length)
                sunk_ships(player_two_board,ships_two_coordinates_on_map,player_two_guess_board)
                if win_condition(player_two_board, board_size):
                    print_paralel_board(board_size, player_one_guess_board, player_two_guess_board, name, name_two)
                    print(f"{name}, you have won!")
                    break
            if counter % 2 == 1:
                name_two = "Darth Vader"
                print(f"\nIt's time for {name_two} to shoot")
                print_paralel_board(board_size, player_one_guess_board, player_two_guess_board, name, name_two)
                update_board_after_shoot_AI(player_one_board,player_one_guess_board, board_size, player_versus, counter, ships_length)
                sunk_ships(player_one_board,ships_one_coordinates_on_map,player_one_guess_board)
                if win_condition(player_two_board, board_size):
                    print_paralel_board(board_size, player_one_guess_board, player_two_guess_board, name, name_two)
                    print(f"{name_two} has won")
                    break
        
        if player_versus == "3":
            if counter % 2 == 0:
                print(f"\nIt's time for {name} to shoot")
                print_paralel_board(board_size, player_one_guess_board, player_two_guess_board, name, name_two)
                update_board_after_shoot_AI(player_two_board,player_two_guess_board, board_size, player_versus, counter, ships_length)
                sunk_ships(player_two_board,ships_two_coordinates_on_map,player_two_guess_board)
                if win_condition(player_one_board, board_size):
                    print_paralel_board(board_size, player_one_guess_board, player_two_guess_board, name, name_two)
                    print("Ano Voldigord has won")
                    break
            if counter % 2 == 1:
                print(f"\nIt's time for {name_two} to shoot")
                print_paralel_board(board_size, player_one_guess_board, player_two_guess_board, name, name_two)
                update_board_after_shoot_AI(player_one_board,player_one_guess_board, board_size, player_versus, counter, ships_length)
                sunk_ships(player_one_board,ships_one_coordinates_on_map,player_one_guess_board)
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
