import sys, os, random # Importing the necessary modules
try:
    os.system('pip install pygame-ce')
finally:
    pass
import pygame
pygame.init() # Initializing pygame
displayinfo = pygame.display.Info() # Getting the display info
# Setting the width and height of the screen to the current width and height of the display
width, height = displayinfo.current_w, displayinfo.current_h  
width, height = 800, 600 # Setting the width and height of the screen to 800 and 600 this is what the fixed screen gets scaled to
fixedWidth, fixedHeight = 800, 600 # Setting the fixed width and height of the screen to 800 and 600 this is what actually gets drawn on 

screen = pygame.display.set_mode((width, height), pygame.RESIZABLE) # Setting the screen to a resizable screen with the width and height of the screen
pygame.display.set_caption('Chess') # Setting the caption of the screen to Chess
internalsurface = pygame.Surface((fixedWidth, fixedHeight)) # Creating a surface that is the fixed width and height of the screen this is the internal
# surface that gets drawn on


black = (119, 149, 86) # Setting the color black to a dark red for the pieces
white = (235, 236, 208) #  Setting the color white to a light brown for the pieces

class Board():
    def __init__(self):
        self.boardpieces = [] # creates a list of boardpieces in the board object
        self.pieces = [] # creates a list of pieces in the board object
        self.pastPositions = []
        self.somethingSelected = False

        self.whiteTurn = True
        self.gameGo = True
    def createBoard(self):
        for i in range(64):
            self.boardpieces.append(BoardPiece(i))
    def createPieces(self):
        for i in range(32):
            self.pieces.append(Piece(i, self))
    def putPiecesOnBoard(self):
         for piece in self.pieces: # for each piece in the pieces list
            for boardpiece in self.boardpieces: # for each boardpiece in the boardpieces list
                if boardpiece.position == piece.boardspot:  # if the position of the boardpiece is equal to the boardspot of the piece does boardspot because
                    #the boardspot is equal to the position of the board  piece.position is the postion to draw when your drawing it
                    boardpiece.piece = piece #sets the boardpieces piece attribute equal to whatever piece is on the square
    def drawPieces(self): # DRAWS EVERY PIECE IN THE BOARDS LIST OF PIECES
        for piece in self.pieces:
           # pygame.draw.rect(internalsurface, piece.color, (piece.position, piece.size))
            if piece.color == white:

                if piece.name == 'pawn':
                    whitepawn = pygame.image.load('whitepawn.png')
                    whitepawn = pygame.transform.scale(whitepawn, piece.size)
                    internalsurface.blit(whitepawn, piece.position)
                elif piece.name == 'rook':
                    whiterook = pygame.image.load('whiterook.png')
                    whiterook = pygame.transform.scale(whiterook, piece.size)
                    internalsurface.blit(whiterook, piece.position)
                elif piece.name == 'knight':
                    whiteknight = pygame.image.load('whiteknight.png')
                    whiteknight = pygame.transform.scale(whiteknight, piece.size)
                    internalsurface.blit(whiteknight, piece.position)
                elif piece.name == 'bishop':
                    whitebishop = pygame.image.load('whitebishop.png')
                    whitebishop = pygame.transform.scale(whitebishop, piece.size)
                    internalsurface.blit(whitebishop, piece.position)
                elif piece.name == 'queen':
                    whitequeen = pygame.image.load('whitequeen.png')
                    whitequeen = pygame.transform.scale(whitequeen, piece.size)
                    internalsurface.blit(whitequeen, piece.position)
                elif piece.name == 'king':
                    whiteking = pygame.image.load('whiteking.png')
                    whiteking = pygame.transform.scale(whiteking, piece.size)
                    internalsurface.blit(whiteking, piece.position)
            else:
                if piece.name == 'pawn':
                    blackpawn = pygame.image.load('blackpawn.png')
                    blackpawn = pygame.transform.scale(blackpawn, piece.size)
                    internalsurface.blit(blackpawn, piece.position)
                elif piece.name == 'rook':
                    blackrook = pygame.image.load('blackrook.png')
                    blackrook = pygame.transform.scale(blackrook, piece.size)
                    internalsurface.blit(blackrook, piece.position)
                elif piece.name == 'knight':
                    blackknight = pygame.image.load('blackknight.png')
                    blackknight = pygame.transform.scale(blackknight, piece.size)
                    internalsurface.blit(blackknight, piece.position)
                elif piece.name == 'bishop':
                    blackbishop = pygame.image.load('blackbishop.png')
                    blackbishop = pygame.transform.scale(blackbishop, piece.size)
                    internalsurface.blit(blackbishop, piece.position)
                elif piece.name == 'queen':
                    blackqueen = pygame.image.load('blackqueen.png')
                    blackqueen = pygame.transform.scale(blackqueen, piece.size)
                    internalsurface.blit(blackqueen, piece.position)
                elif piece.name == 'king':
                    blackking = pygame.image.load('blackking.png')
                    blackking = pygame.transform.scale(blackking, piece.size)
                    internalsurface.blit(blackking, piece.position)
    def drawBoard(self): # DRAWS EVERY PIECE IN THE BOARDS LIST OF BOARDPIECES
        for piece in self.boardpieces:
            pygame.draw.rect(internalsurface, piece.color, (piece.position, piece.size))

    def drawTurn(self):
        if board.whiteTurn == True:
            pygame.draw.rect(internalsurface, (255, 255, 255), (675, 275, 50, 50))
        else:
            pygame.draw.rect(internalsurface, (60, 20, 20), (675, 275, 50, 50))       
                
    def savePosition(self):
        self.pastPositions += [(self.boardpieces, self.pieces)]
    def undo(self):
        lastState = self.pastPositions.pop()
        self.boardpieces = lastState[0]
        self.pieces = lastState[1]
        self.whiteTurn = not self.whiteTurn
        for boardpiece in self.boardpieces:
            boardpiece.piece = None
        self.putPiecesOnBoard()
        #screen.fill(black)
        #self.drawBoard()
        #self.drawPieces()
        for piece in self.pieces:
            for boardpiece in self.boardpieces:
                if boardpiece.piece == piece:
                    piece.position = (boardpiece.position[0] + 12.5, boardpiece.position[1] + 12.5)

    def clearSelection(self):
        if board.somethingSelected == True:
            board.somethingSelected = False
            for boardpiece in board.boardpieces:
                if boardpiece.piece != None:
                    if boardpiece.piece.selected == True:
                        boardpiece.piece.selected = False
            

#Heres the clicking and moving stuff. boardpiece is the boardpiece that you click on bp is the old piece
    def updatePosition(self):
        for boardpiece in board.boardpieces: # loops through the boardpieces
            if board.somethingSelected == False: # if nothing is selected
                if pygame.Rect(boardpiece.position, boardpiece.size).collidepoint(pygame.mouse.get_pos()): #draws a rect on every boardpiece until it hits the mouse selected one
                    print(boardpiece.piece)
                    if boardpiece.piece != None: # if the boardpiece has a piece
                        if self.whiteTurn == True:
                            if boardpiece.piece.color == white:
                                boardpiece.piece.selected = True # select the piece
                                board.somethingSelected = True # Set the selection state
                                #self.whiteTurn = not self.whiteTurn
                            else:
                                pass
                        elif self.whiteTurn == False:
                            if boardpiece.piece.color == black:
                                boardpiece.piece.selected = True
                                board.somethingSelected = True
                                #self.whiteTurn = not self.whiteTurn


                        #if what they want to move to is empty, boardpiece is new tile, bp is old tile
            else: # if something is selected
                if pygame.Rect(boardpiece.position, boardpiece.size).collidepoint(pygame.mouse.get_pos()): #draws a rect on every boardpiece until it hits the mouse selected one
                    if boardpiece.piece is None: #makes sure the boardpiece they clicked on is empty
                        for bp in board.boardpieces: # loops through every boardpiece with different variable name because boardpiece is already used in the first loop
                            if bp.piece and bp.piece.selected: # checks if the current boardpiece in the loop iteration has a piece and then checks if that piece is selected
                                if bp.piece.moveLogic(bp, boardpiece, self) == True:
                                    bp.piece.selected = False  # Deselect the current piece
                                    if hasattr(bp.piece, 'firstmove'):
                                       bp.piece.firstmove = False
                                       
                                    bp.piece.position = (boardpiece.position[0] + 12.5, boardpiece.position[1] + 12.5) # sets the pieces position to the new boardpiece
                                    # Place the piece in the new boardpiece
                                    boardpiece.piece = bp.piece # sets the new board piece's piece attribute equal to the old boardpiece's piece
                                    bp.piece = None  # Clear the previous boardpiece's piece because bp is the old square
                                    board.somethingSelected = False  # Reset selection state
                                    self.whiteTurn = not self.whiteTurn
                            #if what they want to move to is empty, boardpiece is new tile, bp is old tile
                    elif boardpiece.piece:
                        for bp in board.boardpieces:
                            if bp.piece and bp.piece.selected:
                                if boardpiece.piece.color != bp.piece.color:
                                    if bp.piece.moveLogic(bp, boardpiece, self) == True:
                                        bp.piece.selected = False
                                        if hasattr(bp.piece, 'firstmove'):
                                            bp.piece.firstmove = False
                                        bp.piece.position = (boardpiece.position[0] + 12.5, boardpiece.position[1] + 12.5)
                                        if boardpiece.piece.name == 'king':
                                            self.gameGo = False
                                        board.pieces.remove(boardpiece.piece)
                                        boardpiece.piece = bp.piece
                                        bp.piece = None
                                        board.somethingSelected = False
                                        self.whiteTurn = not self.whiteTurn
                                        if boardpiece.row == 0 or boardpiece.row == 7:
                                            if boardpiece.piece.name == 'pawn':
                                                print(boardpiece.piece.name)
                                                boardpiece.piece.name = 'queen'
                                elif boardpiece.piece.color == bp.piece.color and boardpiece.piece.name == 'rook': # or boardpiece.piece.name == 'king':
                                    if bp.piece.moveLogic(bp, boardpiece, self) == True:#bp is oldtile, boardpiece is new tile
                                        bp.piece.selected = False
                                        if  bp.column - boardpiece.column < 0:
                                            movedRight = True
                                        else:
                                            movedRight = False
                                        if hasattr(bp.piece, 'firstmove'):
                                            bp.piece.firstmove = False
                                        if hasattr(boardpiece.piece, 'firstmove'):
                                            boardpiece.piece.firstmove = False
                                        if movedRight == True:
                                            for newKingSquare in board.boardpieces:
                                                if bp.column + 2 == newKingSquare.column and bp.row == newKingSquare.row:
                                                    bp.piece.position = (newKingSquare.position[0] + 12.5, newKingSquare.position[1] + 12.5)
                                                    newKingSquare.piece = bp.piece
                                                    bp.piece = None
                                            for newRookSquare in board.boardpieces:
                                                if boardpiece.column - 2 == newRookSquare.column and boardpiece.row == newRookSquare.row:
                                                    boardpiece.piece.position = (newRookSquare.position[0] + 12.5, newRookSquare.position[1] + 12.5)
                                                    newRookSquare.piece = boardpiece.piece
                                                    boardpiece.piece = None
                                        elif movedRight == False:
                                            for newKingSquare in board.boardpieces:
                                                if bp.column - 2 == newKingSquare.column and bp.row == newKingSquare.row:
                                                    bp.piece.position = (newKingSquare.position[0] + 12.5, newKingSquare.position[1] + 12.5)
                                                    newKingSquare.piece = bp.piece
                                                    bp.piece = None
                                            for newRookSquare in board.boardpieces:
                                                if boardpiece.column + 3 == newRookSquare.column and boardpiece.row == newRookSquare.row:
                                                    boardpiece.piece.position = (newRookSquare.position[0] + 12.5, newRookSquare.position[1] + 12.5)
                                                    newRookSquare.piece = boardpiece.piece
                                                    boardpiece.piece = None
                                        board.somethingSelected = False
                                        self.whiteTurn = not self.whiteTurn
                                    else:
                                        pass
                                    #board.somethingSelected = False
                                    #bp.piece.selected = False
                                            









class BoardPiece():
    def __init__(self, number):
        #SIZE OF BOARDPIECE
        self.size = (75, 75)
        #DETEREMINES THE COLUMN AND ROW
        self.column = number % 8 
        self.row = number // 8 

        #COLOR LOGIC
        if self.row % 2 == 0:
            if self.column % 2 == 0:
                self.color = (235, 236, 208)
            else: 
                self.color = (119, 149, 86)
        else: 
            if self.column % 2 == 0:
                self.color = (119, 149, 86)
            else:
                self.color = (235, 236, 208)

        #POSITION OF THE BOARDPIECE
        self.position = (self.column * 75, self.row * 75)
        #WHAT PIECE THE BOARDPIECE HOLDS
        self.piece = None
        self.number = number
    #DEBUG PRINTINT STUFF
    def __repr__(self):
        return f'{self.column} {self.row} {self.piece}'






class Piece():
    def __init__(self, number, board):
        self.number = number

        #COLOR LOGIC
        if number < 16:
            self.color = black
        else:
            self.color = white
        #INITIAL POSITION LOGIC
        if self.number < 16:
            self.position = board.boardpieces[self.number].position[0] + 12.5, board.boardpieces[self.number].position[1] + 12.5
            self.boardspot = board.boardpieces[self.number].position
        else:
            self.position = board.boardpieces[self.number - 32].position[0] + 12.5, board.boardpieces[self.number - 32].position[1] + 12.5
            self.boardspot = board.boardpieces[self.number - 32].position

        self.size = (50, 50)
        #NAMING LOGIC
        if self.number < 8 or self.number > 23:  
            if self.number == 0 or self.number == 7 or self.number == 24 or self.number == 31:
                self.name = 'rook'
                self.firstmove = True
            elif self.number == 1 or self.number == 6 or self.number == 25 or self.number == 30:
                self.name = 'knight'
            elif self.number == 2 or self.number == 5 or self.number == 26 or self.number == 29:
                self.name = 'bishop'
            elif self.number == 3 or self.number == 27:
                self.name = 'queen'
            elif self.number == 4 or self.number == 28:
                self.name = 'king'
                self.firstmove = True
        else:  
            self.name = 'pawn'
            self.firstmove = True

        #IF ITS SELECTED THEN FUTURE MOVEMENT LOGIC
        self.selected = False
        #MOVEMENT LOGIC, equations baby
        #false means no move true means legal move and move will get played
    def moveLogic(self, oldTile, newTile, board):
        
        if self.name == 'pawn':
            if self.firstmove == True:
                if oldTile.column == newTile.column and newTile.piece is None:
                    if self.color == black and newTile.row == oldTile.row + 1 or newTile.row == oldTile.row + 2:
                        return True
                    elif self.color == white and newTile.row == oldTile.row - 1 or newTile.row == oldTile.row - 2:
                        return True
                    else:
                        return False
                elif (
                    abs(oldTile.column - newTile.column) == 1
                    and abs(oldTile.row - newTile.row) == 1
                    and newTile.piece is not None
                ):

                    if self.color == black and newTile.row == oldTile.row + 1:  # Black captures diagonally down
                        return True
                    elif self.color == white and newTile.row == oldTile.row - 1:  # White captures diagonally up
                        return True
                    else:
                        return False  # Invalid capture
                else:
                    return False 

            elif self.firstmove == False:
                if oldTile.column == newTile.column and newTile.piece is None:

                    if self.color == black and newTile.row == oldTile.row + 1:  # Black moves down
                        return True
                    elif self.color == white and newTile.row == oldTile.row - 1:  # White moves up
                        return True
                    else:
                        return False  # Invalid forward move
        
        # Diagonal capture (EXACTLY one column and one row away)
                elif (
                    abs(oldTile.column - newTile.column) == 1
                    and abs(oldTile.row - newTile.row) == 1
                    and newTile.piece is not None
                ):

                    if self.color == black and newTile.row == oldTile.row + 1:  # Black captures diagonally down
                        return True
                    elif self.color == white and newTile.row == oldTile.row - 1:  # White captures diagonally up
                        return True
                    else:
                        return False  # Invalid capture

                    # If no valid move was found, return False explicitly
                else:
                    return False  # Explicitly returning False
        elif self.name == 'rook':
            if oldTile.column == newTile.column or oldTile.row == newTile.row:
                if oldTile.column != newTile.column: #horizontal move
                    spacesMoved = abs(oldTile.column - newTile.column)
                    if  oldTile.column - newTile.column < 0:
                        movedRight = True
                    else:
                        movedRight = False

                    for i in range(1, spacesMoved):
                        for boardpiece in board.boardpieces:
                            if movedRight:    
                                if oldTile.column + i == boardpiece.column and oldTile.row == boardpiece.row:
                                    if boardpiece.piece != None:
                                        return False
                            elif movedRight == False:
                                if oldTile.column - i == boardpiece.column and oldTile.row == boardpiece.row:
                                    if boardpiece.piece != None:
                                        return False
                                    
                    
                    return True
                                    
                
                elif oldTile.row != newTile.row: #vertical move
                    spacesMoved = abs(oldTile.row - newTile.row)
                    if  oldTile.row - newTile.row < 0:
                        movedDown = True
                    else:
                        movedDown = False
                    

                    for i in range(1, spacesMoved):
                        for boardpiece in board.boardpieces:
                            if movedDown == True:
                                if oldTile.row + i == boardpiece.row and oldTile.column == boardpiece.column:
                                    if boardpiece.piece != None:
                                        return False
                            elif movedDown == False:
                                if oldTile.row - i == boardpiece.row and oldTile.column == boardpiece.column:
                                    if boardpiece.piece != None:
                                        return False
                    return True
            elif newTile.piece.name == 'rook':
                if  oldTile.column - newTile.column < 0:
                    movedRight = True
                else:
                    movedRight = False
                if movedRight == True:
                    for i in range (1, 3):
                        for boardpiece in board.boardpieces:
                            if oldTile.column + i == boardpiece.column and oldTile.row == boardpiece.row:
                                if boardpiece.piece != None:
                                    return False
                    return True 
                elif movedRight == False:
                    for i in range (1, 4):
                        for boardpiece in board.boardpieces:
                            if oldTile.column - i == boardpiece.column and oldTile.row == boardpiece.row:
                                if boardpiece.piece != None:
                                    return False
                    return True

        #BISHOP LOGIC
        elif self.name == 'bishop':
            if oldTile.row == newTile.row or oldTile.column == newTile.column:
                return False
            else:
                if abs(oldTile.row - newTile.row) == abs(oldTile.column - newTile.column): # checks if valid bishop move
                    if  oldTile.row - newTile.row < 0:
                        movedDown = True
                    else:
                        movedDown = False
                    if  oldTile.column - newTile.column < 0:
                        movedRight = True
                    else:
                        movedRight = False
                    spacesMoved = abs(oldTile.row - newTile.row)
                    for i in range(1, spacesMoved):
                        for boardpiece in board.boardpieces:
                            if movedRight == True and movedDown == True:
                                if oldTile.column + i == boardpiece.column and oldTile.row + i == boardpiece.row:
                                    if boardpiece.piece != None:
                                        return False 
                            if movedRight == True and movedDown == False:
                                if oldTile.column + i == boardpiece.column and oldTile.row - i == boardpiece.row:
                                    if boardpiece.piece != None:
                                        return False
                            if movedRight == False and movedDown == True:
                                if oldTile.column - i == boardpiece.column and oldTile.row + i == boardpiece.row:
                                    if boardpiece.piece != None:
                                        return False
                            if movedRight == False and movedDown == False:
                                if oldTile.column - i == boardpiece.column and oldTile.row - i == boardpiece.row:
                                    if boardpiece.piece != None:
                                        return False
                    return True
                else:
                    return False
        
        elif self.name == 'queen':
            if oldTile.column == newTile.column or oldTile.row == newTile.row:
                if oldTile.column != newTile.column: #horizontal move
                    spacesMoved = abs(oldTile.column - newTile.column)
                    if  oldTile.column - newTile.column < 0:
                        movedRight = True
                    else:
                        movedRight = False

                    for i in range(1, spacesMoved):
                        for boardpiece in board.boardpieces:
                            if movedRight:    
                                if oldTile.column + i == boardpiece.column and oldTile.row == boardpiece.row:
                                    if boardpiece.piece != None:
                                        return False
                            elif movedRight == False:
                                if oldTile.column - i == boardpiece.column and oldTile.row == boardpiece.row:
                                    if boardpiece.piece != None:
                                        return False
                    return True
                                    
                
                elif oldTile.row != newTile.row: #vertical move
                    spacesMoved = abs(oldTile.row - newTile.row)
                    if  oldTile.row - newTile.row < 0:
                        movedDown = True
                    else:
                        movedDown = False
                    
                    for i in range(1, spacesMoved):
                        for boardpiece in board.boardpieces:
                            if movedDown == True:
                                if oldTile.row + i == boardpiece.row and oldTile.column == boardpiece.column:
                                    if boardpiece.piece != None:
                                        return False
                            elif movedDown == False:
                                if oldTile.row - i == boardpiece.row and oldTile.column == boardpiece.column:
                                    if boardpiece.piece != None:
                                        return False
                    return True
            elif abs(oldTile.row - newTile.row) == abs(oldTile.column - newTile.column):
                if  oldTile.row - newTile.row < 0:
                    movedDown = True
                else:
                    movedDown = False
                if  oldTile.column - newTile.column < 0:
                    movedRight = True
                else:
                    movedRight = False
                spacesMoved = abs(oldTile.row - newTile.row)
                for i in range(1, spacesMoved):
                    for boardpiece in board.boardpieces:
                        if movedRight == True and movedDown == True:
                            if oldTile.column + i == boardpiece.column and oldTile.row + i == boardpiece.row:
                                if boardpiece.piece != None:
                                    return False 
                        if movedRight == True and movedDown == False:
                            if oldTile.column + i == boardpiece.column and oldTile.row - i == boardpiece.row:
                                if boardpiece.piece != None:
                                    return False
                        if movedRight == False and movedDown == True:
                            if oldTile.column - i == boardpiece.column and oldTile.row + i == boardpiece.row:
                                if boardpiece.piece != None:
                                    return False
                        if movedRight == False and movedDown == False:
                            if oldTile.column - i == boardpiece.column and oldTile.row - i == boardpiece.row:
                                if boardpiece.piece != None:
                                    return False
                return True


        elif self.name == 'king':
           
            print(newTile.piece, oldTile.piece)
            if newTile.piece != None:
                if oldTile.piece.color == newTile.piece.color:
                    if newTile.piece.firstmove == False or oldTile.piece.firstmove == False:
                     
                        return False

                    if  oldTile.column - newTile.column < 0:
                        movedRight = True
                    else:
                        movedRight = False
                    if movedRight == True:
                        for i in range (1, 3):
                            for boardpiece in board.boardpieces:
                                if oldTile.column + i == boardpiece.column and oldTile.row == boardpiece.row:
                                    if boardpiece.piece != None:
                                        return False
                        return True 
                    elif movedRight == False:
                        for i in range (1, 4):
                            for boardpiece in board.boardpieces:
                                if oldTile.column - i == boardpiece.column and oldTile.row == boardpiece.row:
                                    if boardpiece.piece != None:
                                        return False
                        return True
            elif abs(oldTile.column - newTile.column) > 1 or abs(oldTile.row - newTile.row) > 1:
                return False
            else:
                return True
        elif self.name == 'knight':
            if abs(oldTile.column - newTile.column) == 1 or abs(oldTile.column - newTile.column) == 2 and abs(oldTile.row - newTile.row) == 1 or abs(oldTile.row - newTile.row) == 2:
                if abs(oldTile.column - newTile.column) > 1 or abs(oldTile.row - newTile.row) > 1:
                    return True
            else:
                return False
        #THIS IS JSUT SO I CAN PRINT TO DEBUG
    def __repr__(self):
        return f'{self.name} {self.color} {self.position}' 





board = Board()

board.createBoard()
board.createPieces()
board.putPiecesOnBoard()
board.savePosition()






while board.gameGo == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.VIDEORESIZE:
            width, height = event.w, event.h
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: sys.exit()
            if event.key == pygame.K_LEFT:
                board.undo()
 

        if event.type ==pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button click
                board.savePosition()
                board.updatePosition()
            if event.button == 3: #right mouse, going to clear selection
               board.clearSelection()
                                 
                                            
                                                                           
                                            

                    
                    
    

    

    screen.fill(black)
    board.drawTurn()
    board.drawBoard()
    board.drawPieces()
    scaledSurface = pygame.transform.scale(internalsurface, (width, height))
    screen.blit(scaledSurface, (0, 0))
    pygame.display.flip()