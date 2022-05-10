# if outside_hits_counter > inside_hits_counter and column+1<len(player_board[0]):
#     inside_hits_counter = outside_hits_counter
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
def perimeter_verification_AI(player_board,outside_hits_counter,coordinates_validation_list,turns_without_hit,targeted_ship_coordinates):

    # se analizeaza toate posibilitatile pentru vecinii din jurul partii lovite de nava, se trece dintr-o functie in alata pana se gaseste o alta parte
    def up_verify(player_board,outside_hits_counter,coordinates_validation_list,turns_without_hit,targeted_ship_coordinates):

        if outside_hits_counter > inside_hits_counter and column-1>=0 and player_board[row-1][column] == "-":
            inside_hits_counter = outside_hits_counter
            last_hit_coordinates =coordinates_validation_list[-1]
            targeted_ship_coordinates.append(last_hit_coordinates)
            row,column = coordinates_validation_list[-1]
            coordinates = row-1,column
            return coordinates, inside_hits_counter
        elif turns_without_hit == 1 and column-1>=0 and player_board[row-1][column] == "-":
            row,column = coordinates_validation_list[-2]
            coordinates = row-1,column
            return coordinates, inside_hits_counter
        elif turns_without_hit == 2 and column-1>=0 and player_board[row-1][column] == "-":
            row,column = coordinates_validation_list[-3]
            coordinates = row-1,column
            return coordinates, inside_hits_counter
        elif turns_without_hit == 3 and column-1>=0 and player_board[row-1][column] == "-":
            row,column = coordinates_validation_list[-4]
            coordinates = row-1,column
            return coordinates, inside_hits_counter, targeted_ship_coordinates
        else:
            right_verify(player_board,outside_hits_counter,coordinates_validation_list,turns_without_hit)

    def right_verify(player_board,outside_hits_counter,coordinates_validation_list,turns_without_hit,targeted_ship_coordinates):

        if outside_hits_counter > inside_hits_counter and row+1<len(player_board[0]) and player_board[row][column+1] == "-":
            inside_hits_counter = outside_hits_counter
            last_hit_coordinates =coordinates_validation_list[-1]
            targeted_ship_coordinates.append(last_hit_coordinates)
            row,column = coordinates_validation_list[-1]
            coordinates = row,column+1
            return coordinates, inside_hits_counter
        elif turns_without_hit == 1 and row+1<len(player_board[0]) and player_board[row][column+1] == "-":
            row,column = coordinates_validation_list[-2]
            coordinates = row,column+1
            return coordinates, inside_hits_counter
        elif turns_without_hit == 2 and row+1<len(player_board[0]) and player_board[row][column+1] == "-":
            row,column = coordinates_validation_list[-3]
            coordinates = row,column+1
            return coordinates, inside_hits_counter
        elif turns_without_hit == 3 and row+1<len(player_board[0]) and player_board[row][column+1] == "-":
            row,column = coordinates_validation_list[-4]
            coordinates = row,column+1
            return coordinates, inside_hits_counter
        else:
            down_verify(player_board,outside_hits_counter,coordinates_validation_list,turns_without_hit)

    def down_verify(player_board,outside_hits_counter,coordinates_validation_list,turns_without_hit,targeted_ship_coordinates):

        if outside_hits_counter > inside_hits_counter and column+1<len(player_board[0]) and player_board[row+1][column] == "-":
            inside_hits_counter = outside_hits_counter
            last_hit_coordinates =coordinates_validation_list[-1]
            targeted_ship_coordinates.append(last_hit_coordinates)
            row,column = coordinates_validation_list[-1]
            coordinates = row+1,column 
            return coordinates, inside_hits_counter
        elif turns_without_hit == 1 and column+1<len(player_board[0]) and player_board[row+1][column]:
            row,column = coordinates_validation_list[-2]
            coordinates = row+1,column
            return coordinates, inside_hits_counter
        elif turns_without_hit == 2 and column+1<len(player_board[0]) and player_board[row+1][column]:
            row,column = coordinates_validation_list[-3]
            coordinates = row+1,column
            return coordinates, inside_hits_counter
        elif turns_without_hit == 3 and column+1<len(player_board[0]) and player_board[row+1][column]:
            row,column = coordinates_validation_list[-4]
            coordinates = row+1,column
            return coordinates, inside_hits_counter
        else:
            left_verify(player_board,outside_hits_counter,coordinates_validation_list,turns_without_hit)

    def left_verify(player_board,outside_hits_counter,coordinates_validation_list,turns_without_hit,targeted_ship_coordinates):

        if outside_hits_counter > inside_hits_counter and row-1>=0 and player_board[row][column-1] == "-":
            inside_hits_counter = outside_hits_counter
            last_hit_coordinates =coordinates_validation_list[-1]
            targeted_ship_coordinates.append(last_hit_coordinates)
            row,column = coordinates_validation_list[-1]
            coordinates = row,column-1
            return coordinates, inside_hits_counter
        if turns_without_hit == 3 and row-1>=0:
            row,column = coordinates_validation_list[-2]
            coordinates = row,column-1
            return coordinates, inside_hits_counter
        if turns_without_hit == 3 and row-1>=0:
            row,column = coordinates_validation_list[-3]
            coordinates = row,column-1
            return coordinates, inside_hits_counter
        if turns_without_hit == 3 and row-1>=0:
            row,column = coordinates_validation_list[-4]
            coordinates = row,column-1
            return coordinates, inside_hits_counter
        else:
            up_verify(player_board,outside_hits_counter,coordinates_validation_list,turns_without_hit)
        
    coordinates,inside_counter = up_verify(player_board,outside_hits_counter,coordinates_validation_list,turns_without_hit,targeted_ship_coordinates)

    return coordinates,inside_counter,targeted_ship_coordinates

def destroy_founded_ship(player_board,targeted_ship_coordinates):

    # daca primul index din elementele din lista targeted_ship_coordinates este aceeasi
    # inseamna ca randul trebuie sa ramana acelasi pana ce toata nava a fost lovita
    if targeted_ship_coordinates[-1][0] == targeted_ship_coordinates[-2][0]:
        row = player_board[targeted_ship_coordinates[-1][0]]
        
        if player_board[row][targeted_ship_coordinates[-1][1]+1] == "-":   # daca este loc in dreapta sa loveasca, v-a lovi (de adaugat sa nu treaca de map)
            column = player_board[row][targeted_ship_coordinates[-1][1]+1]
        elif player_board[row][targeted_ship_coordinates[0][1]-1] == "-":  # daca nu a gasit loc in dreapta, v-a lovi in stanga (de adaugat sa nu treaca de map)
            column = player_board[row][targeted_ship_coordinates[0][1]-1]

    # daca al doilea index din coordonatele din lista targeted_ship_coordinates este aceeasi
    # inseamna ca trebuie pastrata coloana si verificat in sus si in jos
    elif targeted_ship_coordinates[-1][1] == targeted_ship_coordinates[-2][1]:
        column = player_board[targeted_ship_coordinates[-1][1]]

        if player_board[targeted_ship_coordinates[-1][0]+1][column] == "-": # daca este loc sa mearga in jos, v-a lovi in jos(de adaugat validarea sa nu iasa din board)
            row = player_board[targeted_ship_coordinates[-1][0]+1][column]
        elif player_board[targeted_ship_coordinates[0][0]-1][column] == "-": # daca nu a gasit loc in jos, v-a lovi in sus(de adaugat validarea sa nu iasa din board)
            row = player_board[targeted_ship_coordinates[0][0]-1][column]


    return row,column


        
