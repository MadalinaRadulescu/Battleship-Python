reseted_counter = 0
kept_counter = 0
def play_with_AI(board_size,reseted_counter=1,kept_counter=1, player_one_guess_board=5):
    
    reseted_counter = 0
    for row in player_one_guess_board:
        for space in row:
            if space == "H":
                reseted_counter += 1
    if reseted_counter < kept_counter:
        kept_counter = reseted_counter
        



