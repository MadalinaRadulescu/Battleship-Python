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


def generate_board(board_size):
    
    board = []
    for i in range(board_size):
        i = []
        board.append(i)
        for j in range(board_size):
            j = "-"
            i.append(j)

    return board

def print_paralel_board(board_size, player_one_guess_board, player_two_guess_board):

    letters = " ABCDEFGHIJ"
    first_row = "  "
    new_str = " "
    space_var = " "* (board_size-1)
    space_var2 = " "* (board_size-2)
    n = 0
    for i in range(1,board_size+1):
        first_row+= " "
        first_row+=(" ".join(str(i)))
        
    c = 0
    for i in new_str:
        print(f"{space_var}Player One{space_var}Player Two\n{first_row}   {first_row}")
    for i in player_one_guess_board:
        c += 1
        print(str(letters[c])+ "  " + " ".join(player_one_guess_board[n])+ "   " + str(letters[c])+ "  " + " ".join(player_two_guess_board[n]))
        n += 1
# printeazaz boardul


board_size = get_board_size()
player_one_board = generate_board(board_size)
player_one_guess_board = generate_board(board_size)
player_two_board = generate_board(board_size)
player_two_guess_board = generate_board(board_size)

print_paralel_board(board_size, player_one_guess_board, player_two_guess_board)





