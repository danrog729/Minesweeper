from random import randint
import Graphics

printedBoard = []
board = []


blankSpots = 0
flagCount = 0

# generate the board
def generate_board():
    global printedBoard
    global board
    global blankSpots
    printedBoard = []
    board = []
    for x in range(0,8,1):
        printedLine = []
        line = []
        flagLine = []
        for y in range(0,10,1):
            printedLine.append(".")
            line.append(".")
            blankSpots += 1
        board.append(line)
        printedBoard.append(printedLine)

# place the mines
def place_mines(avoidX, avoidY):
    global blankSpots
    for mine in range(0,10,1):
        valid = False
        while not valid:
            x = randint(0,len(board) - 1)
            y = randint(0,len(board[x]) - 1)
            if (x < avoidX - 1 or x > avoidX + 1 or y < avoidY - 1 or y > avoidY + 1) and board[x][y] != "M":
                valid = True
        board[x][y] = "M"
        blankSpots -= 1
   
# print the board
def print_board(printBoard):
    for x in range(0,len(printBoard),1):
        for y in range(0,len(printBoard[x]),1):
            print(printBoard[x][y],end=" ")
        print()
        
# update printed board
def update_printedBoard(xPos, yPos):
    global blankSpots
    if (printedBoard[xPos][yPos] != "."):
        return True
    if (board[xPos][yPos] == "M"):
        return False
    mineCount = 0
    xLowerBound = max(0, xPos - 1)
    xUpperBound = min(len(board), xPos+2)
    yLowerBound = max(0, yPos - 1)
    yUpperBound = min(len(board[xPos]), yPos+2)
    for row in range(xLowerBound, xUpperBound, 1):
        for column in range(yLowerBound, yUpperBound, 1):
            if board[row][column] == "M":
                mineCount += 1
    printedBoard[xPos][yPos] = mineCount
    blankSpots -= 1
    if mineCount == 0:
        for row in range(xLowerBound, xUpperBound, 1):
            for column in range(yLowerBound, yUpperBound, 1):
                if (row != xPos or column != yPos) and printedBoard[row][column] == ".":
                    update_printedBoard(row, column)
    return True

#Graphics.initialise(10,8,10)

gameOpen = True
while gameOpen:
    Graphics.initialise(10,8,10)
    generate_board()
    button = 3
    while button != 1:
        startingX, startingY, button = Graphics.user_input(printedBoard)
        if button == 3:
            if printedBoard[startingY][startingX] == ".":
                printedBoard[startingY][startingX] = "F"  
            elif printedBoard[startingY][startingX] == "F":
                printedBoard[startingY][startingX] = "."
        if (printedBoard[startingY][startingX] == "F"):
            button = 3
        Graphics.update(printedBoard, 10)
    for row in range(0, len(printedBoard), 1):
        for column in range(0, len(printedBoard[row]), 1):
            printedBoard[row][column] = "."
    place_mines(startingY, startingX)
    update_printedBoard(startingY, startingX)
    ended = False
    while not ended:
        Graphics.update(printedBoard, 10)
        button = 3
        while button != 1:
            playerX, playerY, button = Graphics.user_input(printedBoard)
            if button == 3:
                if printedBoard[playerY][playerX] == ".":
                    printedBoard[playerY][playerX] = "F"
                elif printedBoard[playerY][playerX] == "F":
                    printedBoard[playerY][playerX] = "."
            Graphics.update(printedBoard, 10)
            if (printedBoard[playerY][playerX] == "F"):
                button = 3
        if not update_printedBoard(playerY, playerX):
            Graphics.lost(board, printedBoard)
            ended = True
        if blankSpots == 0:
            Graphics.won(board, printedBoard)
            ended = True
    Graphics.await_click()