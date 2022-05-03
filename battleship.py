
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