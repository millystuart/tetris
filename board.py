from tetrimino import get_tetrimino

def initialise_board():
    return dict(
        width_in_blocks = 10, 
        height_in_blocks = 20,
        active = get_tetrimino(),
        committed = []
    )

def max_point_on_board(coords, largest_y_coords):
    to_compare = []

    if coords == []:
        return 19

    else:
        point = 20
        # looking for all points with same x-coordinate
        for i in range(0, len(coords)): # to loop through each group of coordinates
            for j in range(0, 4): # to loop through each coordinate
                for k in range(0, len(largest_y_coords)):
                        if coords[i][j][0] == largest_y_coords[k][0]:
                            to_compare.append(coords[i][j]) # add valid coordinates to to_compare[]
        
        if to_compare == []:
            return 19
        else:
            for i in range(0, len(to_compare)): # to loop through each group of coordinates
                if to_compare[i][1] < point: # we want less than!!!
                    point = to_compare[i][1]
            
            return point - 1