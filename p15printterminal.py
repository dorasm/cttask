
def printBoard(board):
    maxwidth = 3
    for row in board:
        for col in row:
            print("{:>{}}".format(str(col), maxwidth), end="")
        print()
    print()