import p15board
import p15gameflow
import p15printterminal

def main():

    # Set the board size
    row_size = 4

    # init the board
    board = p15board.Board(row_size)
    
    # play the game
    p15gameflow.handleGameFlow(board, p15printterminal.printBoard)

    
main()