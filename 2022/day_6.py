# open the input file and read in the contents
f = open('input_6.txt')
# f = open('test_input.txt')
text = f.read()
f.close()

##### PART 1 #####
window = list(text[0:3])
index = 3
for char in list(text[3:]):
    window.append(char)
    if len(set(window)) == 4:
        print(index+1)
        break
    else:
        window = window[1:]
        index += 1


##### PART 2 #####
window = list(text[0:13])
index = 13
for char in list(text[13:]):
    window.append(char)
    if len(set(window)) == 14:
        print(index+1)
        break
    else:
        window = window[1:]
        index += 1