import pygame, sys, random, time

pygame.init()

displayinfor = pygame.display.Info()

width, height = displayinfor.current_w, displayinfor.current_h

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Pong")

GameGo = True

font = pygame.font.Font(None, 36)

player1Score = 0
player2Score = 0

P1Score = font.render(str(player1Score), True, (255, 255, 255))
P2Score = font.render(str(player2Score), True, (255, 255, 255))
ball = pygame.image.load("pong.png")

ball = pygame.transform.scale(ball, (30,30))

player1 = pygame.image.load("pong.png")
player1 = pygame.transform.scale(player1, (30, 200))
player1rect = player1.get_rect(center = (50, height / 2))
player1move = [0, 0]

player2 = pygame.image.load('pong.png')
player2 = pygame.transform.scale(player2, (30, 200))
player2rect = player2.get_rect(center = (width - 50, height / 2))
player2move = [0, 0]               

def ballReset():

    global ballrect, ballspeed

    ballrect = ball.get_rect(center = (width / 2, height / 2))

    ballspeed = [random.choice([-5, 5]), random.randint(-5, 5)]
    player1rect.center = (50, height / 2)
    player2rect.center = (width - 50, height / 2)

ballReset()

clock = pygame.time.Clock()



while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: sys.exit()
            if event.key == pygame.K_RETURN:
                GameGo = True
                ballReset()
                player1Score = 0
                player2Score = 0 
                P1Score = font.render(str(player1Score), True, (255, 255, 255))
                p2Score = font.render(str(player2Score), True, (255, 255, 255))
    '''
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if player1rect.top < 0:
            player1move[1] = 0
        else:
            if player1move[1] > -10:
                player1move[1] += -2


    if keys[pygame.K_s]:
        if player1rect.bottom > height:
            player1move[1] = 0
        else:
            if player1move[1] < 10:
                player1move[1] += 2

            
    if keys[pygame.K_UP]:
        if player2rect.top < 0:
            player2move[1] = 0
        else:
            if player2move[1] > -10:
                player2move[1] += -2
    if keys[pygame.K_DOWN]:
        if player2rect.bottom > height:
            player2move[1] = 0
        else:
            if player2move[1] < 10:
                player2move[1] += 2 '''

    if ballspeed[0] < 0:
        if player1rect.centery > ballrect.centery:
            if player1rect.top < 0:
                player1move[1] = 0
            else:
                if player1move[1] > -10:
                    player1move[1] += -2
        if player1rect.centery < ballrect.centery:
            if player1rect.bottom > height:
                player1move[1] = 0
            else:
                if player1move[1] < 10:
                    player1move[1] += 2

    if ballspeed[0] > 0:
        if player2rect.centery > ballrect.centery:
            if player2rect.top < 0:
                player2move[1] = 0
            else:
                if player2move[1] > -10:
                    player2move[1] += -2
        if player2rect.centery < ballrect.centery:
            if player2rect.bottom > height:
                player2move[1] = 0
            else:
                if player2move[1] < 10:
                    player2move[1] += 2


    if player1rect.top < -50:
        player1move[1] = 0
    if player1rect.bottom > height + 50:
        player1move[1] = 0
    if player2rect.top < -50:
        player2move[1] = 0
    if player2rect.bottom > height + 50:
        player2move[1] = 0


    if player1move[1] < 0:
        player1move[1] += 1
    if player1move[1] > 0:
        player1move[1] -= 1

    if player2move[1] < 0:
        player2move[1] += 1

    if player2move[1]> 0:
        player2move[1] -= 1



    if GameGo == True:

        if ballrect.top < 0 or ballrect.bottom > height:

            ballspeed[1] = -ballspeed[1]



        if ballrect.colliderect(player1rect):

            ballspeed[0] = -ballspeed[0] *1.2
            if ballrect.centery < player1rect.centery - 10:
                if ballrect.centery < player1rect.centery - 50:
                    ballspeed[1] += -3
                    if ballspeed[1] < -6:
                        ballspeed[1] = -6
                if ballrect.centery < player1rect.centery - 100:
                    ballspeed[1] += -4
                    if ballspeed[1] < -6:
                        ballspeed[1] = -6

            if ballrect.centery > player1rect.centery + 10:
                if ballrect.centery > player1rect.centery + 50:
                    ballspeed[1] += 3
                    if ballspeed[1] > 6:
                        ballspeed[1] = 6
                if ballrect.centery < player1rect.centery - 100:
                    ballspeed[1] += 4
                    if ballspeed[1] > 6:
                        ballspeed[1] = 6
                       
                



        if ballrect.colliderect(player2rect):

            ballspeed[0] = -ballspeed[0] * 1.2
            if ballrect.centery < player2rect.centery - 10:
                if ballrect.centery < player2rect.centery - 50:
                    ballspeed[1] += -3
                    if ballspeed[1] < -6:
                        ballspeed[1] = -6
                if ballrect.centery < player2rect.centery - 100:
                    ballspeed[1] += -4
                    if ballspeed[1] < -6:
                        ballspeed[1] = -6

            if ballrect.centery > player2rect.centery + 10:
                if ballrect.centery > player2rect.centery + 50:
                    ballspeed[1] += 3
                    if ballspeed[1] > 6:
                        ballspeed[1] = 6
                if ballrect.centery < player2rect.centery - 100:
                    ballspeed[1] += 4
                    if ballspeed[1] > 6:
                        ballspeed[1] = 6



        if ballrect.left < 0:
            if player1Score < 6:

                player1Score += 1
                P1Score = font.render(str(player1Score), True, (255, 255, 255))
                ballReset()
            else:

                GameGo = False
                player1Score += 1
                P1Score = font.render(str(player1Score), True, (255, 255, 255))

        if ballrect.right > width:
            if player2Score < 6:
                player2Score += 1
                P2Score = font.render(str(player2Score), True, (255, 255, 255))
                ballReset()
            else:

                GameGo = False
                player2Score += 1
                P2Score = font.render(str(player1Score), True, (255, 255, 255))
        

        
        ballrect.move_ip(ballspeed)
        player1rect.move_ip(player1move)
        player2rect.move_ip(player2move)

        screen.fill((0, 0, 0))
        screen.blit(P1Score, (width / 2.5, 100))
        screen.blit(P2Score, (width / 1.5, 100))
        screen.blit(player1, player1rect)
        screen.blit(player2, player2rect)
        screen.blit(ball, ballrect)
        pygame.display.flip()
        clock.tick(60)

    elif GameGo == False:
        screen.fill((0, 0, 0))
        print("Game Over")
        screen.blit(P1Score, (width / 2.5, 100))
        screen.blit(P2Score, (width / 1.5, 100))
        gameover = font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(gameover, (width / 2, height / 2))
    
        pygame.display.flip()
        time.sleep(4)
        GameGo = True
        ballReset()
        player1Score = 0
        player2Score = 0
        clock.tick(120)