# random is required for the board init
import random

# String used to represent the empty tile.
EMPTYSTRING = "_"

# Moves are stored in a dictionary to access them easily.
MOVES = {
    "u": [-1, 0],
    "d": [1, 0],
    "l": [0, -1],
    "r": [0, 1]
}

class Board:
    def __init__(self, row_size):
        self.__rows_size = row_size
        self.__size = row_size * row_size

        # Initialize the board data structure as a list of lists.
        self.__board = []
        self.initboard()

    # Fill the board with random tiles and set the empty tile
    def initboard(self):
        
        # create a vector with all the tiles types
        random.seed()
        inputarray = [i for i in range(self.__size)]

        for row in range(self.__rows_size):
            self.__board.append([])
            for col in range(self.__rows_size):
                # choose random number for the reamining list
                curr = random.choice(range(0,len(inputarray)))
                tilecount = inputarray[curr]
                inputarray.pop(curr)
                if tilecount == 0:
                    # The last tile is the empty tile.
                    self.__board[row].append(EMPTYSTRING)

                    # Remember the location of the empty tile
                    self.__empty = [row, col]
                else:
                    self.__board[row].append(tilecount)
        
        #for the very low odds that the random will yield a completed board
        if (self.isdone()):
            self.initboard()

    #needed mainly for prining purpose    
    def getBoard(self):
        return self.__board

    # Return a list of all legal moves for the empty tile.
    # u = up, d = down, l = left, r = right
    def legalmoves(self):
        moves = []
        if self.__empty[0] > 0:
            moves.append("u")
        if self.__empty[0] < self.__rows_size - 1:
            moves.append("d")
        if self.__empty[1] > 0:
            moves.append("l")
        if self.__empty[1] < self.__rows_size - 1:
            moves.append("r")
        return moves

    # Move the empty tile in the wanted direction
    # u = up, d = down, l = left, r = right
    def move(self, direction):
        if direction in self.legalmoves():

            # Store the current position of the empty tile
            empty_x, empty_y = self.__empty

            # Calculate the new position of the empty tile
            new_x = self.__empty[0] + MOVES[direction][0]
            new_y = self.__empty[1] + MOVES[direction][1]

            # Copy the tile in new empty position to current empty position.
            self.__board[empty_x][empty_y] = self.__board[new_x][new_y]

            # Move empty tile to new empty position.
            self.__empty = [new_x, new_y]
            self.__board[new_x][new_y] = EMPTYSTRING
            return True
        else: #illegal move
            return False

    def isdone(self):
        idx = 1
        match = True
        # go over the board and validate the location of each tile
        for row in self.__board:
            for col in row:
                if idx != col and idx < self.__size:
                    return False
                idx += 1

        return True