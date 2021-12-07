import numpy as np

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
    print("Day {}\nYoung fish:\t{}{}\nOld fish:\t{}{}".format(day, young, j, old, i))

print(old.sum() + young.sum())

