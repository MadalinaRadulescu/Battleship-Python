if outside_hits_counter > inside_hits_counter and column+1<len(board_size[0]):
    inside_hits_counter = outside_hits_counter
    row,column = coordinates_validation_list[-1]
    coordinaes = row+1,column   
    turns_without_hit += 1

elif turns_without_hit == 1 and row+1<len(board_size[0]):
    row,column = coordinates_validation_list[-2]
    coordinaes = row,column+1
elif turns_without_hit == 2 and column-1>=0:
    row,column = coordinates_validation_list[-3]
    coordinaes = row-1,column

if turns_without_hit == 3 and row-1>=0:
    row,column = coordinates_validation_list[-4]
    coordinaes = row,column-1