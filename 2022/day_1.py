# open the input file and read in the contents
f = open('input_1.txt')
# f = open('test_input.txt')
text = f.read()
f.close()

# parse the input by line and convert to integers
lines = text.split('\n')

# All we have to do is sum up the values for each 
# run and keep track of the maximum
##### PART 1 #####
total = 0
max = 0
for value in lines:
    if value == "":
        if total > max:
            max = total
        # print(total)
        total = 0
    else:
        total += int(value)

# print(max)

# The only difference now is we need to keep track 
# of the top 3 values rather than the single highest. 
#### PART 2 ####
class Top3:
    def __init__ (self):
        self.values = [0] * 3
        self.count = 0
    
    def add(self, new_value):
        if self.count < 3 :
            self.values[self.count] = new_value
            self.count += 1
        else:
            for i in range(3):
                if self.values[i] < new_value:
                    temp = new_value
                    new_value = self.values[i]
                    self.values[i] = temp

total = 0
top3 = Top3()
for value in lines:
    if value == "":
        top3.add(total)
        # print(total, top3.values)
        total = 0
    else:
        total += int(value)

print(sum(top3.values), top3.values)
