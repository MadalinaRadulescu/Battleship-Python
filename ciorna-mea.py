from battleship import *
# def place_ships(ships, board, board_size,):

#     for ship in ships:
#         while True:
#             print_board(board,board_size)
#             row, column = get_coordinates(board_size)
#             ship_direction,valid_directions = validate_ship_position(row,column,board)
#             if ship_direction != "\nNow, please select the direction you want the ship to go":
#                 while True:
#                     user_choice = input(ship_direction)
#                     if user_choice in valid_directions:
#                         if user_choice == "1":
#                             board[row][column] = "T" 
#                             board[row+1][column] = "T"
#                             board[row+2][column] = "T"
#                             break
#                         elif user_choice == "2":
#                             board[row][column] = "T" 
#                             board[row][column+1] = "T"
#                             board[row][column+2] = "T"
#                             break
#                         elif user_choice == "3":
#                             board[row][column] = "T" 
#                             board[row-1][column] = "T"
#                             board[row-2][column] = "T"
#                             break
#                         elif user_choice == "4":
#                             board[row][column] = "T" 
#                             board[row][column-1] = "T"
#                             board[row][column-2] = "T"
#                             break

#                     else:
#                         print("Please make a valid input")

#                 spacing_ships(board)
#                 break

#             else:
#                 print("\nPlease try again, looks like there wasn't enough space for the ship to be placed.")

    
#     return board


def update_board_after_shoot(player_board, guess_board, board_size, ship):
    while True:
        row, column = get_coordinates(board_size)
        if player_board[row][column] in ["-", "Z"]:
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
            c = 0
            try:
                for i in ship:
                    if player_board[row+c][column] == "H":
                        player_board[row+c][column] = "S"
                        guess_board[row+c][column] = "S"
                    c += 1
                    return guess_board
            except IndexError:
                pass

            c = 0
            try:
                for i in ship:
                    if player_board[row-c][column] == "H":
                        player_board[row-c][column] = "S"
                        guess_board[row-c][column] = "S"
                    c -= 1
                    return guess_board
            except IndexError:
                pass

            c = 0
            try:
                for i in ship:
                    if player_board[row][column+c] == "H":
                        player_board[row][column+c] = "S"
                        guess_board[row][column+c] = "S"
                    c += 1
                    return guess_board
            except IndexError:
                pass

            c = 0
            try:
                for i in ship:
                    if player_board[row][column-c] == "H":
                        player_board[row][column-c] = "S"
                        guess_board[row][column-c] = "S"
                    c -= 1
                    return guess_board
            except IndexError:
                pass
            return guess_board
        else:
            print("Try another one, seems it wasn't a valid input")
