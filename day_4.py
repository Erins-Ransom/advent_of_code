import numpy as np

class game_board:
    """ A class representing an individual game board and it's game state. """
    def __init__(self, row_strings):
        self.board = np.ndarray((5,5), dtype=int)
        self.marked = np.zeros((5,5), dtype=int)
        for i,line in enumerate(row_strings):
            for j,value in enumerate([value for value in line.split(' ') if value.strip() != ""]):
                self.board[i][j] = int(value)

    def update_board(self, value):
        """ Marks the given value on the board and returns the score 
            if the board has won and 0 otherwise. """
        occurences = np.where(self.board == value)
        if (len(occurences[0]) > 0):
            for i in range(len(occurences[0])):
                self.marked[occurences[0][i]][occurences[1][i]] = 1
            if self.check_win():
                return sum([row[np.where(self.marked[i] == 0)[0]].sum() for i,row in enumerate(self.board)]) * value
        return 0
        
    def check_win(self):
        """ Returns whether the game sate is terminal. """
        return 5 in self.marked.sum(0) or 5 in self.marked.sum(1)

    def reset(self):
        """" Resets the game state. """
        self.marked = np.zeros((5,5), dtype=int)

def winning_score(board_list, number_list):
    ###### PART 1 ######
    for value in number_list:
        for board in board_list:
            result = board.update_board(value)
            if result > 0:
                return result

def losing_score(board_list, number_list):
    ###### PART 2 ######
    for value in number_list:
        complete_boards = []
        for i,board in enumerate(board_list):
            result = board.update_board(value)
            if result > 0:
                complete_boards.append(i)
                if len(board_list) == 1:
                    return result
        for i in reversed(complete_boards):
            del board_list[i]




# open up our file and read in the contents as a string
f = open("input_4.txt")
text = f.read()
f.close()

# then we parse our input into lines, getting rid of empty lines,
# parse the first line into our list of numbers and then create 
# each of our game boards
lines = [line for line in text.split('\n') if line.strip() != ""]
number_list = [int(value) for value in lines[0].split(',')]
lines = lines[1:]
board_list = [game_board(lines[i*5:i*5+5]) for i in range(int(len(lines)/5))]

print(winning_score(board_list, number_list))

for board in board_list:
    board.reset()

print(losing_score(board_list, number_list)) 