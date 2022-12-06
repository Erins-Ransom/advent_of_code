# open the input file and read in the contents
f = open('input_2.txt')
# f = open('test_input.txt')
text = f.read()
f.close()

# parse the input by line
lines = text.split('\n')

# Most cases have a unique score, so we use 
# a switch statment to match them 
##### PART 1 #####
score = 0
for line in lines:
    match line:
        case "A X":
            score += 1 + 3
        case "A Y":
            score += 2 + 6
        case "A Z":
            score += 3 + 0
        case "B X":
            score += 1 + 0
        case "B Y":
            score += 2 + 3
        case "B Z":
            score += 3 + 6
        case "C X":
            score += 1 + 6
        case "C Y":
            score += 2 + 0
        case "C Z":
            score += 3 + 3
        case _:
            print("Bad input: {}".format(line))

print(score)

# Same as before, we just need to re-map
# which scores correspond to which case.
##### PART 2 #####
score = 0
for line in lines:
    match line:
        case "A X":
            score += 3 + 0
        case "A Y":
            score += 1 + 3
        case "A Z":
            score += 2 + 6
        case "B X":
            score += 1 + 0
        case "B Y":
            score += 2 + 3
        case "B Z":
            score += 3 + 6
        case "C X":
            score += 2 + 0
        case "C Y":
            score += 3 + 3
        case "C Z":
            score += 1 + 6
        case _:
            print("Bad input: {}".format(line))

print(score)
