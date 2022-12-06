
values = {'(':1, ')':3, '[':2, ']':57, '{':3, '}':1197, '<':4, '>':25137}
closer = {'{':'}', '(':')', '[':']', '<':'>'}
points = 0
line_scores = []
for line in open("input_10.txt").read().split('\n'):
    stack = []
    for char in line:
        if char in ['(', '[', '{', '<']:
            stack.append(char)
        elif closer[stack.pop()] != char:
            points += values[char]
            stack = []
            break
    if len(stack) > 0:
        score = 0
        for char in reversed(stack):
            score = score*5 + values[char]
        line_scores.append(score)

line_scores.sort()
print(points, line_scores[len(line_scores)//2])
