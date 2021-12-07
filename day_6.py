import numpy as np

# This function prints a vizulization of each step in the algorithm
def vizualize(day, young, old):
    print("Day {}".format(day))
    print("Young fish:\t{}".format([{value} if i == day % 9 else value for i,value in enumerate(young)])) 
    print("Old fish:\t{}".format([{value} if i == day % 7 else value for i,value in enumerate(old)]))

# We will keep track of the fish by grouping them by their
# breeding cycles.  Since youg fish have 2 extra days in their
# cycle, we must keep track of these separately. 
old = np.zeros(7, dtype=int)
young = np.zeros(9, dtype=int)

# We read in our input and add each fish to the count for the 
# day of the cyle on which they will reproduce.  Here we assume 
# that the population starts young; however, this does not actually 
# effect the outcome so long as no fish with more than 7 days in 
# their cycle is added to the 'old' cycle.  Consider that, after 
# one cycle, the new young and old counts for that day will be the 
# same regardless of which array they start in as at least one 
# would start empty.
for value in open("input_6.txt").read().strip().split(','):
    young[int(value)] += 1

# For each day, the number of new fish bred will be the sum of 
# the young and old fish breeing on that day, while the young 
# fish that breed will then mature and become old fish.  day % 7.e.
#   young[day % 9] -> young[day % 9] + old[day % y]
for day in range(256):
    temp = young[day % 9]
    young[day % 9] += old[day % 7]
    old[day % 7] += temp
    vizualize(day, young, old)

print("There are {} fish after 256 days".format(old.sum() + young.sum()))


