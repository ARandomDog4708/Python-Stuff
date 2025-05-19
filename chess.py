import sys, pygame, random # Importing the necessary modules
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


black = (165, 42, 42) # Setting the color black to a dark red for the pieces
white = (255, 228, 196) #  Setting the color white to a light brown for the pieces

class Board():
    def __init__(self):
        self.boardpieces = [] # creates a list of boardpieces in the board object
        self.pieces = [] # creates a list of pieces in the board object
        for i in range(64):
            self.boardpieces.append(BoardPiece(i)) # creates a boardpiece object for each number from 0 to 63 and appends it to the boardpieces list, so 64 boardpieces
        for i in range(32):
            self.pieces.append(Piece(i, self)) # creates a piece object for each number from 0 to 31 and appends it to the pieces list, so 32 pieces
        for piece in self.pieces: # for each piece in the pieces list
            for boardpiece in self.boardpieces: # for each boardpiece in the boardpieces list
                if boardpiece.position == piece.boardspot:  # if the position of the boardpiece is equal to the boardspot of the piece does boardspot because
                    #the boardspot is equal to the position of the board  piece.position is the postion to draw when your drawing it
                    boardpiece.piece = piece #sets the boardpieces piece attribute equal to whatever piece is on the square
        self.somethingSelected = False

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

            
                




    def updatePosition(self):
        for boardpiece in board.boardpieces: # loops through the boardpieces
                        if board.somethingSelected == False: # if nothing is selected
                            if pygame.Rect(boardpiece.position, boardpiece.size).collidepoint(pygame.mouse.get_pos()): #draws a rect on every boardpiece until it hits the mouse selected one
                                print(boardpiece.piece)
                                if boardpiece.piece != None: # if the boardpiece has a piece
                                    boardpiece.piece.selected = True # select the piece
                                    board.somethingSelected = True # Set the selection state
                        else: # if something is selected
                            if pygame.Rect(boardpiece.position, boardpiece.size).collidepoint(pygame.mouse.get_pos()): #draws a rect on every boardpiece until it hits the mouse selected one
                                if boardpiece.piece is None: #makes sure the boardpiece they clicked on is empty
                                    for bp in board.boardpieces: # loops through every boardpiece with different variable name because boardpiece is already used in the first loop
                                        if bp.piece and bp.piece.selected: # checks if the current boardpiece in the loop iteration has a piece and then checks if that piece is selected
                                            bp.piece.selected = False  # Deselect the current piece
                                            bp.piece.position = (boardpiece.position[0] + 12.5, boardpiece.position[1] + 12.5) # sets the pieces position to the new boardpiece
                                            # Place the piece in the new boardpiece
                                            boardpiece.piece = bp.piece # sets the new board piece's piece attribute equal to the old boardpiece's piece
                                            bp.piece = None  # Clear the previous boardpiece's piece because bp is the old square
                                            board.somethingSelected = False  # Reset selection state
                                        
                                elif boardpiece.piece:
                                    for bp in board.boardpieces:
                                        if bp.piece and bp.piece.selected:
                                            if boardpiece.piece.color != bp.piece.color:
                                                bp.piece.selected = False
                                                bp.piece.position = (boardpiece.position[0] + 12.5, boardpiece.position[1] + 12.5)
                                                board.pieces.remove(boardpiece.piece)
                                                boardpiece.piece = bp.piece
                                                bp.piece = None
                                                board.somethingSelected = False
                                            else:
                                                board.somethingSelected = False
                                                bp.piece.selected = False
                                            









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
                self.color = (255, 255, 255)
            else: 
                self.color = (0,0,0)
        else: 
            if self.column % 2 == 0:
                self.color = (0,0,0)
            else:
                self.color = (255, 255, 255)

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
        #self.movelogic = {'pawn':} FINISH LATER

        #THIS IS JSUT SO I CAN PRINT TO DEBUG
    def __repr__(self):
        return f'{self.name} {self.color} {self.position}' 





board = Board()







while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.VIDEORESIZE:
            width, height = event.w, event.h
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: sys.exit()

        if event.type ==pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button click
                board.updatePosition()
               
                                 
                                            
                                                                           
                                            

                    
                    


    

    screen.fill(black)
    board.drawBoard()
    board.drawPieces()
    scaledSurface = pygame.transform.scale(internalsurface, (width, height))
    screen.blit(scaledSurface, (0, 0))
    pygame.display.flip()