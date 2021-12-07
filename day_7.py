import numpy as np

counts = np.zeros(2000, dtype=int)
max_pos = 0

for value in open("input_7.txt").read().strip().split(','):
    counts[int(value)] += 1
    #print(int(value))
    if int(value) > max_pos:
        max_pos = int(value)

# Small Test Example
# part 1: 37 fuel at pos 2, part 2: 168 fuel at pos 5
# for value in [16,1,2,0,4,2,7,1,2,14]:
#     counts[value] += 1
#     if value > max_pos:
#         max_pos = value

r_count, r_cost, r_penalty = 0, 0, 0
# print("Counts:\n{}".format(counts[:max_pos+1]))
# print("Forward pass:")
for i in range(max_pos+1):
    r_cost += r_penalty 
    # r_penalty += counts[i]    ### PART 1 ###
    r_count += counts[i]        ### PART 2 ###
    r_penalty += r_count        ### PART 2 ###
    # print("pos: {}, r_cost: {}, r_penalty: {}, r_count: {}".format(i, r_cost, r_penalty, r_count))

l_count, l_cost, l_penalty = counts[max_pos], 0, counts[max_pos]
min_cost, min_pos = r_cost, -1
# r_penalty -= counts[max_pos]  ### PART 1 ###
r_penalty -= r_count            ### PART 2 ###
r_count -= counts[max_pos]      ### PART 2 ###
# print("Counts:\n{}".format(counts[:max_pos+1]))
# print("Backward pass:\npos: {}, l_cost: 0, l_penalty: {}, l_count: {}, r_cost: {}, r_penalty: {}, r_count: {}".format(max_pos, l_penalty, l_count, r_cost, r_penalty, r_count))
for i in reversed(range(max_pos)):
    r_cost -= r_penalty
    l_cost += l_penalty
    # l_penalty += counts[i]    ### PART 1 ###
    # r_penalty -= counts[i]    ### PART 1 ###
    l_count += counts[i]        ### PART 2 ###
    l_penalty += l_count        ### PART 2 ###
    r_penalty -= r_count        ### PART 2 ###
    r_count -= counts[i]        ### PART 2 ###
    # print("pos: {}, l_cost: {}, l_penalty: {}, l_count: {}, r_cost: {}, r_penalty: {}, r_count: {}".format(i, l_cost, l_penalty, l_count, r_cost, r_penalty, r_count))
    if l_cost + r_cost < min_cost:
        min_cost = l_cost + r_cost
        min_pos = i

print("Minimal fuel cost of {} at position {}".format(min_cost, min_pos))
