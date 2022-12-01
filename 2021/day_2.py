# We're gonna use numpy arrays for some variety
import numpy as np

# First we open the file and load the contents
f = open("input_2.txt")
text = f.read()
f.close()

# Next we parse our input by line
lines = text.split('\n')

###### PART 1 ######
# we'll be tracking our position as an [horizontal pos, depth] vector
pos = [0, 0]

for line in lines:
    (direction, value) = line.split(' ', 1)
    if direction == "forward":
        pos[0] += int(value)
    elif direction == "up":
        pos[1] -= int(value)
    else:
        pos[1] += int(value)

print(pos[0]*pos[1])

###### PART 2 ######
# we add aim as the third dimension of our vector
pos = [0, 0, 0]

for line in lines:
    (direction, value) = line.split(' ', 1)
    if direction == "forward":
        pos[0] += int(value)
        pos[1] += int(value) * pos[2]
    elif direction == "up":
        pos[2] -= int(value)
    else:
        pos[2] += int(value)

print(pos[0]*pos[1])


