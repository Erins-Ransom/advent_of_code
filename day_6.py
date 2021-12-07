import numpy as np

def vizualize(day, young, old):
    print("Day {}".format(day))
    print("Young fish:\t{}".format([{value} if i == day % 9 else value for i,value in enumerate(young)])) 
    print("Old fish:\t{}".format([{value} if i == day % 7 else value for i,value in enumerate(old)]))

old = np.zeros(7, dtype=int)
young = np.zeros(9, dtype=int)

for value in open("input_6.txt").read().strip().split(','):
    if int(value) <= 8:
        young[int(value)] += 1

for day in range(256):
    i = day % 7
    j = day % 9
    temp = young[j]
    young[j] += old[i]
    old[i] += temp
    vizualize(day, young, old)

print(old.sum() + young.sum())


