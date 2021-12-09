import numpy as np


def get_surrounding_values(i,j, h_map):
    """ 
    This function returns a list of the values surrounding the 
    indicated point in the height map.
    """
    result = []
    if i > 0:
        result.append(h_map[i-1][j])
    if i < 99:
        result.append(h_map[i+1][j])
    if j > 0:
        result.append(h_map[i][j-1])
    if j < 99:
        result.append(h_map[i][j+1])
    return result

def basin_size(i,j, h_map):
    """
    This is a recursive function that counts the cells in the 
    basin contiaining the indicated point.  It also marks all 
    cells in that basin as "already counted" with a -1. 
    """
    if h_map[i][j] in [-1,9]:
        return 0
    h_map[i][j] = -1
    count = 1
    if i > 0:
        count += basin_size(i-1,j, h_map)
    if i < 99:
        count += basin_size(i+1,j, h_map)
    if j > 0:
        count += basin_size(i,j-1, h_map)
    if j < 99:
        count += basin_size(i,j+1, h_map)
    return count

h_map = np.ndarray((100,100), dtype=int)
for i,x in enumerate(open("input_9.txt").read().replace('\n', '')):
    h_map[i // 100][i % 100] = int(x)

###### PART 1 ######
total_risk = 0
for i in range(100):
    for j in range(100):
        if h_map[i][j] < min(get_surrounding_values(i,j, h_map)):
            total_risk += h_map[i][j] + 1

print(total_risk)

###### PART 2 ######
largest_sizes = [0,0,0]
for i in range(100):
    for j in range(100):
        if h_map[i][j] not in [-1,9]:
            size = basin_size(i,j,h_map)
            if size > min(largest_sizes):
                largest_sizes.remove(min(largest_sizes))
                largest_sizes.append(size)

print(largest_sizes[0]*largest_sizes[1]*largest_sizes[2])