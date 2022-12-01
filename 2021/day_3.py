import numpy as np

# open the input file and read in the contents
f = open('input_3.txt')
text = f.read()
f.close()

# parse the input into a 2D array (we also transpose the input)
lines = text.split('\n')
data_t = np.ndarray((len(lines[0]), len(lines)), dtype=int)
for i, line in enumerate(lines):
    for j, value in enumerate(line):
        data_t[j][i] = int(value)

###### PART 1 #######
# Now we need to decode gamma and epsilon.  We find the most common 
# bit of each column by suming over it and then updating alpha and gamma
# with the appropriate power of 2
gamma = 0
epsilon = 0
power = 0
for input_column in reversed(data_t):
    if input_column.sum() / len(input_column) >= 0.5:
        gamma += 2**power
    else:
        epsilon += 2**power
    power += 1
print(gamma, epsilon)
print(gamma*epsilon)

###### PART 2 ######
# First, we identify the value for the oxygen rate and co2 rate
ox_list = range(len(data_t[0]))
co_list = range(len(data_t[0]))
ox_index = -1
co_index = -1

for input_column in data_t:
    temp_list = []
    if (ox_index == -1):
        common_value = (1, 0)[input_column[ox_list].sum() / len(ox_list) < 0.5]
        for i in ox_list:
            if input_column[i] == common_value:
                temp_list.append(i)
    ox_list = temp_list
    if len(ox_list) == 1:
        ox_index = ox_list[0]

    temp_list = []
    if (co_index == -1):
        common_value = (0, 1)[input_column[co_list].sum() / len(co_list) < 0.5]
        for i in co_list:
            if input_column[i] == common_value:
                temp_list.append(i)
    co_list = temp_list
    if len(co_list) == 1:
        co_index = co_list[0]

# then we need to decode them
ox_rate = 0
co_rate = 0
power = 0
for input_column in reversed(data_t):
    ox_rate += input_column[ox_index] * 2**power
    co_rate += input_column[co_index] * 2**power
    power += 1

print(ox_rate, co_rate)
print(ox_rate * co_rate)







