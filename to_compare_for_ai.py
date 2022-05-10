# if outsiboard_counter > inside_hits_counter and column+1<len(player_board[0]):
#     inside_hits_counter = board_hits_counter
#     row,column = coordinates_validation_list[-1]
#     coordinates = row+1,column   
#     turns_without_hit += 1

# elif turns_without_hit == 1 and row+1<len(player_board[0]):
#     row,column = coordinates_validation_list[-2]
#     coordinates = row,column+1

# elif turns_without_hit == 2 and column-1>=0:
#     row,column = coordinates_validation_list[-3]
#     coordinates = row-1,column

# if turns_without_hit == 3 and row-1>=0:
#     row,column = coordinates_validation_list[-4]
#     coordinates = row,column-1



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

def smart_AI(player_board,coordinates_validation_list):


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



