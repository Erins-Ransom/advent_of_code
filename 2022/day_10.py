



##### PART 1 #####
def part_1(instructions):
    X = 1
    cycle = 0
    signal_strength = 0
    op_counter = 0
    instr_index = 0
    val = 0
    while cycle <= 220:
        
        if op_counter > 0:
            op_counter -= 1
            cycle += 1
            if (cycle - 20) % 40 == 0:
                signal_strength += cycle * X
                # print("Cycle: {}, signal strength: {}".format(cycle, signal_strength))
            continue
        
        # only hit this code when op_counter == 0
        X += val
        match instructions[instr_index][0]:
            case "addx":
                op_counter = 2
                val = int(instructions[instr_index][1])
            case "noop":
                op_counter = 1
                val = 0
            case _:
                print("Bad input: {}".format(instructions[instr_index][0]))
        instr_index += 1
    
    return signal_strength
                
        
            
##### PART 2 #####
def part_2(instructions):
    X = 1
    cycle = 0
    signal_strength = 0
    op_counter = 0
    instr_index = 0
    val = 0
    CRT = ""
    while cycle < 240:
        
        if op_counter > 0:
            if cycle % 40 <= X+1 and cycle % 40 >= X-1:
                CRT += "#"
            else:
                CRT += "."
            op_counter -= 1
            cycle += 1
            if cycle % 40 == 0:
                CRT += "\n"
            if (cycle - 20) % 40 == 0:
                signal_strength += cycle * X
            continue
        
        # only hit this code when op_counter == 0
        X += val
        match instructions[instr_index][0]:
            case "addx":
                op_counter = 2
                val = int(instructions[instr_index][1])
            case "noop":
                op_counter = 1
                val = 0
            case _:
                print("Bad input: {}".format(instructions[instr_index][0]))
        instr_index += 1
    
    print(CRT)










f = open('input_10.txt')
# f = open('test_input.txt')
text = f.read()
f.close()

# Parse our input instructions
instructions = [line.split() for line in text.split('\n')]

print(part_1(instructions))
part_2(instructions)
