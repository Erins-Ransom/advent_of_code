# open the input file and read in the contents
f = open('input_4.txt')
# f = open('test_input.txt')
text = f.read()
f.close()

# parse the input into a 3-dim list of numbers
ranges = [[[int(x) for x in pair.split('-')] for pair in line.split(',')] for line in text.split('\n')]


##### PART 1 #####
total = 0
for range1, range2 in ranges:
    if (range1[0] <= range2[0] and range1[1] >= range2[1]) or (range1[0] >= range2[0] and range1[1] <= range2[1]):
        total += 1

print(total)


##### PART 2 #####
total = 0
for range1, range2 in ranges:
    if not (range1[1] < range2[0] or range2[1] < range1[0]):
        total += 1

print(total)
