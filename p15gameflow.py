def handleGameFlow(board, boardDraw):
    
    boardDraw(board.getBoard())

    cmd = ""
    while cmd != "q":
        cmd = input("Move empty tile [u]p, [d]own, [l]eft or [r]ight, or [q]uit. ")
        
        if cmd in ["u", "d", "l", "r"]:         
            if  not board.move(cmd):
                print("\nIllegal move\n")
            boardDraw(board.getBoard())
            if board.isdone():
                print ("You won!!")
                break
        elif cmd == "q":
            break
        else:
            print("Unknown command, please try again")