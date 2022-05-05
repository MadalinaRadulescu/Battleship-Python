
from ast import Break
from itertools import count
from optparse import check_builtin


ships_lenght = [1,4,3]
row = ["-","-","Z","H","H","H"]



def check_row(row,ships_lenght):
    
    counter_of_H = 0
    biggest_ship = max(ships_lenght)

    index=0
    for i in row:
        ship_to_sunk = []
        counter=1
        if i == "Z":            
            for j in range(biggest_ship+1):
                if row[index+counter] == "H":
                    counter_of_H +=1
                    ship_to_sunk.append(index+counter)
                if row[index+counter] == "T":
                    counter_of_H = 0
                    ship_to_sunk = []
                    return  ship_to_sunk
                if row[index+counter] == "Z" and counter_of_H > 1:
                    return  ship_to_sunk
                if index+counter is len(row)-1:
                    if row[index+counter]=="H":
                        return  ship_to_sunk
                counter+=1
        if i == "H":
            counter = 0
            for j in range(biggest_ship+1):
                if row[index+counter] == "H":
                    counter_of_H +=1
                    ship_to_sunk.append(index+counter)
                if row[index+counter] == "T":
                    counter_of_H = 0
                    ship_to_sunk = []
                    return  ship_to_sunk
                if row[index+counter] == "Z" and counter_of_H > 1:
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
                    if len(index_c) is len(row)-1:
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


print(check_row(row,ships_lenght))


