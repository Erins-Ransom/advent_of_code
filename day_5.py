import numpy as np

# first we read in the input as a string and parse it by line
f = open("input_5.txt")
text = f.read()
f.close()
lines = text.split('\n')

# we will keep track of single points and overlapping points
# in two different 2d arrays, or "maps"
single_points = np.zeros((1000,1000), dtype=int)
overlapping_points = np.zeros((1000,1000), dtype=int)

# We then parse each line and add the corresponding points to our maps
# if the point has already been added to the single_points map, then 
# we add it to the overlapping_points map
for line in lines:
    ###### PART 1 ######
    # parse the line into a 2d array [[x1,y1], [x2,y2]]
    # so values[0] = start_point and values[1] = end_point
    # values[0][0] = x1, values[1][1] = y2, etc.
    values = np.array([[int(value) for value in point.split(',')] for point in line.split(" -> ")], dtype=int)
    # here we deal with vetical lines
    if values[0][0] == values[1][0]:
        for i in range(abs(values[1][1] - values[0][1])+1):
            if values[0][1] < values[1][1]:
                point = values[0] + [0, i]
            else:
                point = values[0] - [0, i]
            if single_points[point[0]][point[1]] == 1:
                overlapping_points[point[0]][point[1]] = 1
            else:
                single_points[point[0]][point[1]] = 1
    # here we deal with horizontal lines
    elif values[0][1] == values[1][1]:
        for i in range(abs(values[1][0] - values[0][0])+1):
            if values[0][0] < values[1][0]:
                point = values[0] + [i, 0]
            else:
                point = values[0] - [i, 0]
            if single_points[point[0]][point[1]] == 1:
                overlapping_points[point[0]][point[1]] = 1
            else:
                single_points[point[0]][point[1]] = 1

    ###### PART 2 ######
    # here we deal with lines going from top left to bottom right (or opposite)
    elif values[0][1] - values[1][1] == values[0][0] - values[1][0]:
        for i in range(abs(values[1][0] - values[0][0])+1):
            if values[0][0] < values[1][0]:
                point = values[0] + [i, i]
            else:
                point = values[0] - [i, i]
            if single_points[point[0]][point[1]] == 1:
                overlapping_points[point[0]][point[1]] = 1
            else:
                single_points[point[0]][point[1]] = 1
    # here we deal with lines going from bottom left to top right (or opposite)
    else:
        for i in range(abs(values[1][0] - values[0][0])+1):
            if values[0][0] < values[1][0]:
                point = values[0] + [i, i*(-1)]
            else:
                point = values[0] + [i*(-1), i]
            if single_points[point[0]][point[1]] == 1:
                overlapping_points[point[0]][point[1]] = 1
            else:
                single_points[point[0]][point[1]] = 1

# our final result is the number of points in overlapping_points
print(overlapping_points.sum(0).sum())