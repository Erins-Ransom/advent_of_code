import numpy as np

##### PART 1 #####
# We'll do two passes over the grid, in the first we will check
# visibility from the north, east and west.  The second pass will 
# check visibility from the south. 
def part_1(grid: np.ndarray):
    vis = np.zeros(grid.shape, dtype=int)
    col_max = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0:
                vis[i][j] = 1
                col_max.append(grid[i][j])
            elif j == 0 or j == len(grid[0])-1:
                vis[i][j] = 1
                if grid[i][j] > col_max[j]:
                    col_max[j] = grid[i][j]
            elif grid[i][j] > col_max[j]:
                vis[i][j] = 1
                col_max[j] = grid[i][j]
            elif grid[i][j] > max(grid[i][0:j]) or grid[i][j] > max(grid[i][j+1:]):
                vis[i][j] = 1


    col_max = []
    for i in reversed(range(len(grid))):
        for j in range(len(grid[0])):
            if i == len(grid)-1:
                vis[i][j] = 1
                col_max.append(grid[i][j])
            elif grid[i][j] > col_max[j]:
                vis[i][j] = 1
                col_max[j] = grid[i][j]

    return vis.sum()

##### PART 2 ######
def part_2(grid: np.ndarray):
    best_score = 0
    for i in range(1,len(grid)-1):
        for j in range(1,len(grid[0])-1):
            s_score = score(grid, i, j)
            if s_score > best_score:
                best_score = s_score
    return best_score


# This is less efficient than the doulbe pass but easier to code, lol
def score(grid: np.ndarray, i: int,j: int):
    dist = 0
    for k in reversed(range(0,i)):
        if grid[i][j] > grid[k][j]:
            dist += 1
        else:
            dist +=1
            break
    val = dist
    dist = 0
    for k in range(i+1,len(grid)):
        if grid[i][j] > grid[k][j]:
            dist += 1
        else:
            dist += 1
            break
    val *= dist
    dist = 0
    for k in reversed(range(0,j)):
        if grid[i][j] > grid[i][k]:
            dist += 1
        else:
            dist += 1
            break
    val *= dist
    dist = 0
    for k in range(j+1,len(grid[0])):
        if grid[i][j] > grid[i][k]:
            dist += 1
        else:
            dist += 1
            break
    return val*dist




f = open('input_8.txt')
# f = open('test_input.txt')
text = f.read()
f.close()

# Parse our input into a 2D array of ints
grid = np.array([[int(c) for c in line] for line in text.split('\n')])

print(part_1(grid))
print(part_2(grid))




