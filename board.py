from tetrimino import get_tetrimino#, get_y_coords

def initialise_board():
    return dict(
        width_in_blocks = 10, 
        height_in_blocks = 20,
        active = get_tetrimino(),
        committed = []
    )

# def get_committed_y_coords(coords):
#     committed_y_coords = []
#     for i in range(0, len(coords)):
#             for j in range(0, 4):
#                 if all(v != coords[i][j][1] for v in committed_y_coords):
#                     committed_y_coords.append(coords[i][j][1])
    
#     return committed_y_coords

# def delete_row(committed, y_coords):
#     for i in range(0, len(committed)):
#         for j in range(0, 4):
#             for k in range(0, len(y_coords)):
#                 number_of_cells = 0
#                 for l in range(0, 10):
#                     if committed[i][j][1] == y_coords[k]:
#                         number_of_cells += 1
                
#                 if number_of_cells == 10:
#                     # import pdb; pdb.set_trace()
#                     for l in range(0, 10):
#                         committed.remove(committed[i][j])