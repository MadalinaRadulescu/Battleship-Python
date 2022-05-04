

board = [["-", "-", "-","-", "-"],["-", "-", "-","-", "-"],["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"]]
def print_board(board, board_size):

    letters = " ABCDEFGHIJ"
    first_row = "  "
    n = 0
    for i in range(1,board_size+1):
        first_row+= " "
        first_row+=(" ".join(str(i)))
        
    print(f"\n{first_row}")
    for i in board:
        n += 1
        print(str(letters[n])+ "  " + " ".join(i))


print_board(board, 5)