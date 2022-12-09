
# Here we define a class to represent the file system
class dir:
    def __init__(self, parent):
        self.parent = parent
        self.dirs = {}
        self.size = 0
    
    def add_file(self, size):
        self.size += int(size)

    def add_dir(self, name):
        self.dirs[name] = dir(self)

    def get_size(self):
        total_size = self.size
        for _, Dir in self.dirs.items():
            total_size += Dir.get_size()
        return total_size


##### PART 1 #####
# We recursively traverse the tree and add the size of any dir smaller than 100000
def part_1(directory):
    total = 0
    size = directory.get_size()
    if size <= 100000:
        total += size
    for _, Dir in directory.dirs.items():
        total += part_1(Dir)

    return(total)

##### PART 2 #####
# We will again recursivily traverse the tree, but we will now keep track of the 
# smallest directory that will free up sufficient space, namely 30,000,000 - (70,000,000 - sizeof(/))
def part_2(directory):
    min_size = 30000000 - (70000000 - directory.get_size())
    return recursive_check(directory, min_size)


def recursive_check(directory, min_val):
    sizes = []
    for _, Dir in directory.dirs.items():
        sizes.append(recursive_check(Dir, min_val))
    
    size = directory.get_size()
    if size >= min_val:
        sizes.append(size)
    else:
        sizes.append(70000000)

    return min(sizes)



# Now we need to parse the input and create our dirrectory structure
f = open('input_7.txt')
# f = open('test_input.txt')
text = f.read()
f.close()

# some variables to help keep track of the current state
command = None
Dir = None
# the root of our file system 
root = dir(None)

for line in text.split('\n'):
    if line == "":
        continue
    args = line.split()
    if args[0] == "$":
        if args[1] == "cd":
            command = args[1]
            if args[2] == "/":
                Dir = root
            elif args[2] == "..":
                Dir = Dir.parent
            else:
                Dir = Dir.dirs[args[2]]

    elif args[0] == "dir":
        Dir.add_dir(args[1])

    else:
        Dir.add_file(args[0])



print(part_1(root))
print(part_2(root))

