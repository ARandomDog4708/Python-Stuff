import sys, pygame, random  #importing pygame and sys, sys is just to exit the thing

pygame.init() #intializing pygame and every module in it

displayinfo = pygame.display.Info() #gets the display info of the computer, like the resolution and stuff
width, height = displayinfo.current_w, displayinfo.current_h  # Get screen dimensions the width and height of the screen
#the width and height of the screen are stored in the variables width and height, these are the dimensions of the screen

size = width, height = width, height #sets the size variable equal to the variable width and height which are the dimensions of the screen
#these dimensions are also basically the coordinates of the screen 0,0 is the top left corner 
#the bottom right corner is width, height which is just the dimensions of the screen


dvdspeed = [5, 5] #speed of the dvd, moves 1 pixel in the x and 1 pixel in the y direction, x goes right, and the y goes down due to the coordinate system
#the speed goes 1 pixel per frame, so if the frame rate is 60 then the dvd moves 60 pixels per second

ballspeed = [-8, -8] #speed of the ball, moves -5 pixels in the x and -5 pixels in the y direction, x goes left, and the y goes up due to the coordinate system
#the speed goes 5 pixels per frame, so if the frame rate is 60 then the ball moves 60 pixels per second

black = 0, 0, 0 #color of the screen, black nothing more to it change these values, change color on 255 scale

screen = pygame.display.set_mode(size)#sets the screen to the size variable the screen is just a surface that is basically the backround, 
#the screen is what gets drawn on when bliting(drawing) stuff

dvd = pygame.image.load("dvd.jpg") #loads the image of the dvd in the desktop folder to a variable called dvd which is a object which is a surface
#this dvd will be drawn on the screen which is another surface

dvd = pygame.transform.scale(dvd, (160, 106.6666)) #transforms the image of the dvd, and scales it to 60 by 60 pixels 

dvdrect = dvd.get_rect(center=(random.randint(160, width/2), random.randint(107, height-107))) # gets the rectangle hitbox of the dvd using the dvd variable.get_rect() method, and then center is a keyword variable
#that changes the center value from the default top left corner to the center of the screen

ball = pygame.image.load("intro_ball.gif") #loads the image of the ball in the desktop folder to a variable called ball which is a object which is a surface
#this ball will be drawn on the screen which is another surface
ball = pygame.transform.scale(ball, (60, 60)) #transforms the image of the ball, and scales it to 60 by 60 pixels 

ballrect = ball.get_rect(center=(random.randint(width/2+60, width-60), random.randint(60, height-60))) # gets the rectangle hitbox of the ball using the ball variable.get_rect() method, and then center is a keyword variable
#that makes it so only spawns on the right side but not where it would clip into the wall


clock = pygame.time.Clock() #creates a clock object that will be used to control the frame rate of the game so that the game runs at a constant 60 frames per second
#instead of just running as fast as it can


while True: #main game loop, this loop will run forever until the game is exited through clicking X on the window

    for event in pygame.event.get(): #gets every even that is happening in the game, like key presses, mouse clicks, and window closing
        if event.type == pygame.QUIT: sys.exit() #if the event is the user pressing the x button on the window, then the program will exit
        if event.type == pygame.KEYDOWN: #if the event is the user pressing a key on the keyboard
            if event.key == pygame.K_ESCAPE: #if the key pressed is the escape key
                sys.exit() #exit the program

        #DVD SPEED CONTROL
            if event.key == pygame.K_UP:
                if dvdspeed[0] > 0: #if the x speed is greater than 0, then add 1 to the x speed
                    dvdspeed[0] += 1
                else:
                    dvdspeed[0] -= 1 #if the x speed is less than 0, then subtract 1 from the x speed
                if dvdspeed[1] > 0: #if the y speed is greater than 0, then add 1 to the y speed
                    dvdspeed[1] += 1
                else:
                    dvdspeed[1] -= 1 #if the y speed is less than 0, then subtract 1 from the y speed
                

            if event.key == pygame.K_DOWN:
                if dvdspeed[0] > 0: #if the x speed is greater than 0, then add 1 to the x speed
                    dvdspeed[0] -= 1
                else:
                    dvdspeed[0] += 1 #if the x speed is less than 0, then subtract 1 from the x speed
                if dvdspeed[1] > 0: #if the y speed is greater than 0, then add 1 to the y speed
                    dvdspeed[1] -= 1
                else:
                    dvdspeed[1] += 1 #if the y speed is less than 0, then subtract 1 from the y speed



        #BALL SPEED CONTROL
            if event.key == pygame.K_RIGHT:
                if ballspeed[0] > 0: #if the x speed is greater than 0, then add 1 to the x speed
                    ballspeed[0] += 1
                else:
                    ballspeed[0] -= 1 #if the x speed is less than 0, then subtract 1 from the x speed
                if ballspeed[1] > 0: #if the y speed is greater than 0, then add 1 to the y speed
                    ballspeed[1] += 1
                else:
                    ballspeed[1] -= 1 #if the y speed is less than 0, then subtract 1 from the y speed
                

            if event.key == pygame.K_LEFT:
                if ballspeed[0] > 0: #if the x speed is greater than 0, then add 1 to the x speed
                    ballspeed[0] -= 1
                else:
                    ballspeed[0] += 1 #if the x speed is less than 0, then subtract 1 from the x speed
                if ballspeed[1] > 0: #if the y speed is greater than 0, then add 1 to the y speed
                    ballspeed[1] -= 1
                else:
                    ballspeed[1] += 1 #if the y speed is less than 0, then subtract 1 from the y speed

    #HERES THE dvd MOVEMENT CODE
    dvdrect = dvdrect.move(dvdspeed) #changes the position of the dvdrect by the speed list variable, 
    #so it moves 5 pixel in the x and 5 pixel in the y direction which is right and down

    #HERES THE dvd BOUNCING CODE
    if dvdrect.left < 0 or dvdrect.right > width: #checks if the left side of the dvd is less than 0 or the right side of the dvd is greater than the width of the screen

        dvdspeed[0] = -dvdspeed[0] #if the dvd hits the left or right side of the screen, then the x speed is reversed so that the dvd moves in the opposite direction

    if dvdrect.top < 0 or dvdrect.bottom > height: #checks if the top of the dvd is less than 0 or the bottom of the dvd is greater than the height of the screen

        dvdspeed[1] = -dvdspeed[1] #if the dvd hits the top or bottom of the screen, then the y speed is reversed so that the dvd moves in the opposite direction
    
    
    #HERES THE ball MOVEMENT CODE
    ballrect = ballrect.move(ballspeed) #changes the position of the ballrect by the speed list variable,

    #HERES THE ball BOUNCING CODE
    if ballrect.left < 0 or ballrect.right > width:
        ballspeed[0] = -ballspeed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        ballspeed[1] = -ballspeed[1]
    

    if ballrect.colliderect(dvdrect):
    # Left side collision
        if ballrect.right >= dvdrect.left and ballrect.left < dvdrect.left:
            ballspeed[0] = -abs(ballspeed[0])  # Bounce left
            if dvdspeed[0] < ballspeed[0]:
                ballspeed[0] += dvdspeed[0] + 1
            if ballrect.left < 0:
                ballrect.left = dvdrect.right

    # Right side collision
        elif ballrect.left <= dvdrect.right and ballrect.right > dvdrect.right: # Bounce right
            ballspeed[0] = abs(ballspeed[0])
            if dvdspeed[0] > ballspeed[0]:
                ballspeed[0] += dvdspeed[0] + 1
            if ballrect.right > width:
                ballrect.right = dvdrect.left

    # Top side collision
        if ballrect.bottom >= dvdrect.top and ballrect.top < dvdrect.top:
            ballspeed[1] = -abs(ballspeed[1])  # Bounce up
            if dvdspeed[1] < ballspeed[1]:
                ballspeed[1] -= dvdspeed[1] - 1
            if ballrect.top < 0:
                ballrect.top = dvdrect.bottom

    # Bottom side collision
        elif ballrect.top <= dvdrect.bottom and ballrect.bottom > dvdrect.bottom:
            ballspeed[1] = abs(ballspeed[1])  # Bounce down
            if dvdspeed[1] > ballspeed[1]:
                ballspeed[1] -= dvdspeed[1] - 1
            if ballrect.bottom > height:
                ballrect.bottom = dvdrect.top
    
    
    #all of this happens behind the scenes and doesnt get drawn until the screen is cleared and the dvd is drawn again with the new position and blit

    #HERES THE DRAWING CODE WHERE THE STUFF BEFORE GETS DRAWN
    screen.fill(black) #fills the screen with the color black, effectively clearing the screen so that the dvd can be drawn again and not leave a trail
    screen.blit(dvd, dvdrect) #pastes the dvd image surface onto the screen surface at the coordinates of the dvdrect rectangle
    #print(dvdrect.center) #prints the center of the dvdrect rectangle to the console so i can see the position of the dvd
    screen.blit(ball, ballrect) #pastes the ball image surface onto the screen surface at the coordinates of the ballrect rectangle
    pygame.display.flip() #the way this works is theres basically two screens, the one on screen, and the one being made behind the scenes, this funciton flips the two screens
    #so that the one being made behind the scenes is now on screen, and the one that was on screen is now being drawn on behind the scenes

    clock.tick(60) #sets the frame rate of the game to 60 frames per second, so that the game runs at a constant speed and not as fast as it can