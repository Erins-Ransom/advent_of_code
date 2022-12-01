
###### PART 1 ######
count = 0
for output in [line.split('| ')[-1] for line in open("input_8.txt").read().split('\n')]:
    for string in output.split(' '):
        if len(string) in [2,3,4,7]:
            count += 1
print(count)

###### PART 2 ######
class decoder:
    def __init__(self, codes_string):
        codes = [frozenset(code) for code in codes_string.split(' ')]
        self.f = dict({})
        self.inv = dict({})
        # first we decode unique length values: 1,4,7,8
        for code in codes:
            if len(code) == 2:
                self.f[code] = 1
                self.inv[1] = code
            elif len(code) == 3:
                self.f[code] = 7
                self.inv[7] = code
            elif len(code) == 4:
                self.f[code] = 4
                self.inv[4] = code
            elif len(code) == 7:
                self.f[code] = 8
                self.inv[8] = code
        # then we decode the remaing values based on the previous
        # using set comparisons on the codes
        while len(self.f) < 10:
            for code in codes:
                if len(code) == 5: # codes of length 5: 2,3,5
                    if code >= self.inv[1]:
                        self.f[code] = 3
                        self.inv[3] = code
                    # we need 9 in order to distinguish between 2 and 5
                    elif 9 in self.inv:
                        if code <= self.inv[9]:
                            self.f[code] = 5
                            self.inv[5] = code
                        else:
                            self.f[code] = 2
                            self.inv[2] = code
                if len(code) == 6:  # codes of length 6: 9,0,6
                    if code >= self.inv[4]:
                        self.f[code] = 9
                        self.inv[9] = code
                    elif code >= self.inv[7]:
                        self.f[code] = 0
                        self.inv[0] = code
                    else:
                        self.f[code] = 6
                        self.inv[6] = code

    def __call__(self, string_code):
        result = 0
        power = 0
        for value in reversed(string_code.split(' ')):
            result += self.f[frozenset(value)] * 10 ** power
            power += 1
        return result

    def inv(self, int_value):
        return self.inv[int_value]

total = 0
for codes, output in [(line.split(' | ')[0], line.split(' | ')[-1]) for line in open("input_8.txt").read().split('\n')]:
    total += decoder(codes)(output)

print(total)