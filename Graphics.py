import pygame

screen = pygame.display.set_mode((100,100))
pygame.font.init()
font = pygame.font.SysFont("Roboto Bold", 55)
smallfont = pygame.font.SysFont("Roboto Bold", 30)
difficultyFont = pygame.font.SysFont("Roboto Bold", 24)
text1 = font.render("1", True, (34, 120, 207))
text2 = font.render("2", True, (60, 141, 64))
text3 = font.render("3", True, (209, 49, 53))
text4 = font.render("4", True, (122, 39, 160))
text5 = font.render("5", True, (253, 146, 2))
text6 = font.render("6", True, (0, 151, 167))
text7 = font.render("7", True, (66, 66, 66))
text8 = font.render("8", True, (163, 156, 148))
textEasy = difficultyFont.render("Easy", True, (48, 48, 48))
textMedium = difficultyFont.render("Medium", True, (48, 48, 48))
textHard = difficultyFont.render("Hard", True, (48, 48, 48))
greenTiles = [".", "F"]

def initialise(sizeX,sizeY, mineCount):
    global screen
    screen = pygame.display.set_mode((sizeX * 45, sizeY * 45 + 60))
    pygame.display.set_caption("Minesweeper")
    screen.fill((74,117,44))
    for row in range(0, sizeY, 1):
        for column in range(0, sizeX, 1):
            if (row + column) % 2 == 0:
                pygame.draw.rect(screen, (170, 215, 81), (column * 45, row * 45 + 60, 45, 45))
            else:
                pygame.draw.rect(screen, (162, 209, 73), (column * 45, row * 45 + 60, 45, 45))
    
    flagCountText = smallfont.render(str(mineCount), True, (255, 255, 255))
    screen.blit(flagCountText, (203 - flagCountText.get_width() // 2, 30 - flagCountText.get_height() // 2))
    draw_flag(147, 13)
    
    pygame.draw.rect(screen, (255, 255, 255), (16, 15, 61, 30))
    screen.blit(textEasy, (23, 23))

    pygame.display.flip()
    
def update(board, mineCount):
    global screen
    for row in range(0, len(board), 1):
        for column in range(0, len(board[row]), 1):
            if (row + column) % 2 == 0 and board[row][column] in greenTiles:
                colour = (170, 215, 81)
            elif (row + column) % 2 != 0 and board[row][column] in greenTiles:
                colour = (162, 209, 73)
            elif (row + column) % 2 == 0 and not board[row][column] in greenTiles:
                colour = (229, 194, 159)
            else:
                colour = (215, 184, 153)
            pygame.draw.rect(screen, colour, (column * 45, row * 45 + 60, 45, 45))
            if board[row][column] == 1:
                screen.blit(text1, (column * 45 + 23 - text1.get_width() // 2,  row * 45 + 60 + 23 - text1.get_height() // 2))
            elif board[row][column] == 2:
                screen.blit(text2, (column * 45 + 23 - text2.get_width() // 2,  row * 45 + 60 + 23 - text2.get_height() // 2))
            elif board[row][column] == 3:
                screen.blit(text3, (column * 45 + 23 - text3.get_width() // 2,  row * 45 + 60 + 23 - text3.get_height() // 2))
            elif board[row][column] == 4:
                screen.blit(text4, (column * 45 + 23 - text4.get_width() // 2,  row * 45 + 60 + 23 - text4.get_height() // 2))
            elif board[row][column] == 5:
                screen.blit(text5, (column * 45 + 23 - text5.get_width() // 2,  row * 45 + 60 + 23 - text5.get_height() // 2))
            elif board[row][column] == 6:
                screen.blit(text6, (column * 45 + 23 - text6.get_width() // 2,  row * 45 + 60 + 23 - text6.get_height() // 2))
            elif board[row][column] == 7:
                screen.blit(text7, (column * 45 + 23 - text7.get_width() // 2,  row * 45 + 60 + 23 - text7.get_height() // 2))
            elif board[row][column] == 8:
                screen.blit(text8, (column * 45 + 23 - text8.get_width() // 2,  row * 45 + 60 + 23 - text8.get_height() // 2))
    for row in range(0, len(board), 1):
        for column in range(0, len(board[row]), 1):
            if (board[row][column] == 1 or 
                board[row][column] == 2 or
                board[row][column] == 3 or
                board[row][column] == 4 or
                board[row][column] == 5 or
                board[row][column] == 6 or
                board[row][column] == 7 or
                board[row][column] == 8):
                outlineWidth = 4
                for outlineRow in range(max(0,row-1), min(len(board), row + 2)):
                    for outlineColumn in range(max(0,column-1), min(len(board[row]) - 1, column + 1)):
                        if (board[outlineRow][outlineColumn] in greenTiles and not board[outlineRow][outlineColumn + 1] in greenTiles or
                            not board[outlineRow][outlineColumn] in greenTiles and board[outlineRow][outlineColumn + 1] in greenTiles):
                            pygame.draw.line(screen, (135, 175, 58), ((outlineColumn + 1) * 45 + 1 - outlineWidth // 2, outlineRow * 45 + 60 - outlineWidth // 2), ((outlineColumn + 1) * 45 + 1 - outlineWidth // 2, (outlineRow + 1) * 45 + 60 - 1 + outlineWidth // 2), outlineWidth)
                for outlineRow in range(max(0,row-1), min(len(board) - 1, row + 1)):
                    for outlineColumn in range(max(0,column-1), min(len(board[row]), column + 2)):
                        if (board[outlineRow][outlineColumn] in greenTiles and not board[outlineRow + 1][outlineColumn] in greenTiles or
                            not board[outlineRow][outlineColumn] in greenTiles and board[outlineRow + 1][outlineColumn] in greenTiles):
                            pygame.draw.line(screen, (135, 175, 58), (outlineColumn * 45 - outlineWidth // 2, (outlineRow + 1) * 45 + 60 + 1 - outlineWidth // 2), ((outlineColumn + 1) * 45 - 1 + outlineWidth // 2, (outlineRow + 1) * 45 + 60 + 1 - outlineWidth // 2), outlineWidth)
    flagCount = 0
    for row in range(0, len(board), 1):
        for column in range(0, len(board[row]), 1):
            if (board[row][column] == "F"):
                draw_flag_on_grid(column, row)
                flagCount += 1
                
    pygame.draw.rect(screen, (74, 117, 44), (0, 0, screen.get_width(), 60))
    flagCountText = smallfont.render(str(mineCount - flagCount), True, (255, 255, 255))
    screen.blit(flagCountText, (203 - flagCountText.get_width() // 2, 30 - flagCountText.get_height() // 2))
    draw_flag(147, 13)
    
    pygame.draw.rect(screen, (255, 255, 255), (16, 15, 61, 30))
    screen.blit(textEasy, (23, 23))

    pygame.display.flip()
    
def lost(board):
    global screen
    for row in range(0, len(board), 1):
        for column in range(0, len(board[row]), 1):
            if board[row][column] == "M":
                pygame.draw.rect(screen, (255, 255, 255), (column * 45, row * 45 + 60, 45, 45))
    pygame.display.flip()

def won(board):
    global screen
    for row in range(0, len(board), 1):
        for column in range(0, len(board[row]), 1):
            if board[row][column] == "M":
                pygame.draw.rect(screen, (255, 255, 255), (0, 0, 45, 45))
    textYouWon = font.render("You won!", True, (255,255,255))
    screen.blit(textYouWon, (0, 0))
    pygame.display.flip()
    
    
def await_click():
    clicked = False
    while not clicked:
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                return pos, event.button
            
def user_input(board):
    validClick = False
    while not validClick:
        clickPos, mouseButton = await_click()
        if clickPos[1] > 60:
            validClick = True
            clickPos = (clickPos[0] // 45, (clickPos[1] - 60) // 45)
            return clickPos[0], clickPos[1], mouseButton
    
def draw_flag(xPos, yPos):
    pygame.draw.rect(screen, (230, 51, 7), (xPos + 2, yPos, 5, 34))
    pygame.draw.rect(screen, (230, 51, 7), (xPos, yPos + 29, 9, 5))
    pygame.draw.polygon(screen, (242, 54, 7), ((xPos + 7, yPos + 2), (xPos + 32, yPos +11), (xPos + 7, yPos + 20)))
    
def draw_flag_on_grid(xPos, yPos):
    draw_flag(xPos * 45 + 7, yPos * 45 + 60 + 6)