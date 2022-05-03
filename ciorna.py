board_size = 5
board = []
for i in range(board_size):
    i = []
    board.append(i)
    for j in range(board_size):
        j = ["-"]
        i.append(j)


# board = []
# for i in range(0, board_size):
#     board.append(["-"]*board_size)


letters = " ABCDEFGHIJ"
first_row = "  "
n = 0
for i in range(1,board_size+1):
    first_row+= " "
    first_row+=(" ".join(str(i)))
    
print(f"\n{first_row}\n")
for i in board:
    n += 1
    print(str(letters[n])+ "  " + " ".join(i))
