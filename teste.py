
board = [["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"]]

def get_coordinate_AI(board):
    import random
    from random import randint 
    ai_coordinates =[]
    while True:
        x, y = randint(0, len(board)), randint(0, len(board))
        if tuple((x,y)) not in ai_coordinates:
            ai_coordinates.append(tuple((x, y)))
            continue
        return random.choice(ai_coordinates)
    

print(get_coordinate_AI(board))

def place_ships(ships, board, board_size):

    for ship in ships:
        while True:
            #print_board(board, board_size)
            ship_coordinates = get_coordinate_AI(board_size)
            row = ord(ship_coordinates[0]) - ord("a")
            column = int(ship_coordinates[1])-1
            ship_direction, valid_directions = validate_ship_position(row, column, board)
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
                break

            else:
                print("\nPlease try again, looks like there wasn't enough space for the ship to be placed.")            
    
    return board

