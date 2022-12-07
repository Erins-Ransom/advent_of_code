# open the input file and read in the contents
f = open('input_5.txt')
# f = open('test_input.txt')
text = f.read()
f.close()

# parsing the input is honestly the hardest part here, the rest is just maintaining a few stacks
lines = text.split('\n')
i = 0
j = 0
while (not lines[i] == "") :
    i += 1

setup = lines[0:i]
# first we extract the needed infor from our instructions
instructions = [[int(x) for x in line.split()[1::2]] for line in lines[i+1:]]
stack_count =  int(setup[-1].split()[-1])

# then we parse the initial setup of the crates into a list of stacks
stacks = []
stack_index = 0
for i in range(len(setup[-1])):
    if setup[-1][i] == ' ':
        continue
    stacks.append([])
    for j in reversed(range(len(setup)-1)):
        if len(setup[j]) > i and setup[j][i] != ' ':
            stacks[stack_index].append(setup[j][i])
            # print(stacks)
    stack_index += 1

print(stacks)

# lastly, we carry out the instructions on our stacks
##### PART 1 #####
# for a,b,c in instructions:
#     for i in range(a):
#         stacks[c-1].append(stacks[b-1].pop())

# tops = []
# for stack in stacks:
#     tops.append(stack[-1])
# print("".join(tops))

# for part 2 we no longer have standard stack behavior, but 
# rather we move x items without reversing their order. 
##### PART 2 #####
for a,b,c in instructions:
    for i in reversed(range(1, a+1)):
        stacks[c-1].append(stacks[b-1][-i])
    stacks[b-1] = stacks[b-1][0:-a]
    # print(stacks)

tops = []
for stack in stacks:
    tops.append(stack[-1])
print("".join(tops))

