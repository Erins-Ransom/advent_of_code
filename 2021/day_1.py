# open the input file and read in the contents
f = open('input_1.txt')
text = f.read()
f.close()

# parse the input by line and convet to integers
lines = text.split('\n')
numbers = [int(line) for line in lines]

####### PART 1 #######
# initialize the first value and our counter for increases
current_number = numbers[0]
increases = 0

# compare each value against the next and increment our
# counter if the next value is greater
for value in numbers:
    if value > current_number:
        increases += 1
    current_number = value

print("Total increases in detph:\t{}".format(increases))

####### PART 2 #######
# as before, but summing windows of 3 elements
current_sum = sum(numbers[:3])
increases = 0

for i in range(len(lines) - 2):
    next_sum = sum(numbers[i:i+3])
    if next_sum > current_sum:
        increases += 1
    current_sum = next_sum

print("Total window-sum increases:\t{}".format(increases))