# open the input file and read in the contents
f = open('input_3.txt')
# f = open('test_input.txt')
text = f.read()
f.close()

# parse the input by line
lines = text.split('\n')


##### PART 1 #####
score = 0
for line in lines:
    mid = int(len(line)/2)
    for value in line[0:mid]:
        if value in line[mid:len(line)]:
            if ord(value) >= ord('a') and ord(value) <= ord('z'):
                score += 1 + ord(value) - ord('a')
            elif ord(value) >= ord('A') and ord(value) <= ord('Z'):
                score += 27 + ord(value) - ord('A')
            break

print(score)

##### PART 2 #####
set1 = set({})
set2 = set({})
score = 0
group_counter = 0
for line in lines:
    match group_counter:
        case 0:
            set1 = set({})
            for value in line:
                set1.add(value)
            group_counter += 1
        case 1:
            set2 = set({})
            for value in line:
                set2.add(value)
            group_counter += 1
        case 2:
            for value in line:
                if value in set1 and value in set2:
                    if ord(value) >= ord('a') and ord(value) <= ord('z'):
                        score += 1 + ord(value) - ord('a')
                    elif ord(value) >= ord('A') and ord(value) <= ord('Z'):
                        score += 27 + ord(value) - ord('A')
                    break
            group_counter = 0

print(score)

