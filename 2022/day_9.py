import numpy as np

##### PART 1 #####
def part_1(moves):
    path = set({(0,0)})
    head = np.zeros(2, dtype=int)
    tail = np.zeros(2, dtype=int)
    for a,b in moves:
        for _ in range(int(b)):
            move(head, tail, a)
            path.add((tail[0],tail[1]))
    return len(path)


def move(head, tail, direction):
    m = np.zeros(2, dtype=int)
    match direction:
        case "L":
            m[1] = -1
        case "R":
            m[1] = 1
        case "U":
            m[0] = 1
        case "D":
            m[0] = -1
        case _:
            print("Bad input {}".format(direction))
    head += m
    delta = head - tail
    if abs(delta).max() > 1:
        if delta[0] == 0 or delta[1] == 0:
            tail += m
        else:
            tail += delta - m


##### PART 2 #####
def part_2(moves):
    path = set({(0,0)})
    knots = np.zeros((10,2), dtype=int)
    for a,b in moves:
        for _ in range(int(b)):
            move_chain(knots, a)
            path.add((knots[9][0],knots[9][1]))
        # draw(knots, path)
    return len(path)


def move_chain(knots, direction):
    m = np.zeros(2, dtype=int)
    match direction:
        case "L":
            m[1] = -1
        case "R":
            m[1] = 1
        case "U":
            m[0] = 1
        case "D":
            m[0] = -1
        case _:
            print("Bad input {}".format(direction))
    knots[0] += m
    diag = False
    for i in range(1,10):
        delta = knots[i-1] - knots[i]
        # our stopping condition
        if abs(delta).max() < 2:
            break
        # our condition to switch between diagonal/orthogonal moves
        if delta[0] == 0 or delta[1] == 0:
            m = delta//2
            diag = False
        elif not diag:
            m = delta - m
            diag = True
        knots[i] += m
        i += 1

# visualization function for verification
def draw(knots, path):
    lines = []
    origin = [15,15]
    for i in range(35):
        line = []
        for j in range(35):
            line.append('.')
        lines.append(line)
    for a,b in path:
        lines[a + origin[0]][b + origin[1]] = '#'
    lines[origin[0]][origin[1]] = 's'
    for i in reversed(range(10)):
        lines[knots[i][0] + origin[0]][knots[i][1] + origin[1]] = str(i) 
    for line in reversed(lines):
        print("".join(line))



f = open('input_9.txt')
# f = open('test_input.txt')
text = f.read()
f.close()

# Parse our input instructions
moves = [line.split() for line in text.split('\n')]

print(part_1(moves))
print(part_2(moves))

