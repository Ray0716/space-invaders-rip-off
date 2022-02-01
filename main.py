import pygame
import random
import math
import time

def flt_int(x):
    x = str(x)
    result = ""
    for a in x:
        if a != ".":
            result = str(result + a)
        else:
            return result

highs = 0

global pausebool
pausebool = False

#timep = pygame.time.get_ticks()

collide = False

point = pygame.time.get_ticks()

whatalien = random.randint(1, 10)
# Intialize the pygame
playing = False
alienres = -55
aspeed = 2
pygame.init()
alienint1 = 5
alienint2 = 5
# create the screen
screen = pygame.display.set_mode((632, 865))
bgsp=1
live = 3
# Title and Icon
pygame.display.set_caption("SPACE DASH")
icon = pygame.image.load('battleship.png')
pygame.display.set_icon(icon)

alienimgall = pygame.image.load('alien1.jpg')
allx = pygame.image.load('output-onlinepngtools.png')
#pygame.image.load('output-onlinepngtools.png')
font = pygame.font.Font("DS-DIGI.TTF", 53)
fonttwo = pygame.font.Font("DS-DIGI.TTF", 23)
#backg = pygame.image.load("oie_FudUxKMQmxR1.jpg")

# Player
playerimg = pygame.image.load('battleship.png')
playerx = 370
playery = 720
playerx_change = 0

# alien

alienimg = alienimgall
alienx = 20
alieny = alienres
alieny_change = 0

# alien2

alienimg2 = allx
alienx2 = 80
alieny2 = alienres
alieny_change2 = 0

# alien3

alienimg3 = alienimgall
alienx3 = 140
alieny3 = alienres
alieny_change3 = 0

# alien4

alienimg4 = allx
alienx4 = 200
alieny4 = alienres
alieny_change4 = 0

# alien5

alienimg5 = alienimgall
alienx5 = 260
alieny5 = alienres
alieny_change5 = 0

# alien6

alienimg6 = allx
alienx6 = 320
alieny6 = alienres
alieny_change6 = 0

# alien7

alienimg7 = alienimgall
alienx7 = 380
alieny7 = alienres
alieny_change7 = 0

# alien8

alienimg8 = pygame.image.load("aal.jpg")
alienx8 = 440
alieny8 = alienres
alieny_change8 = 0

# alien9

alienimg9 = alienimgall
alienx9 = 500
alieny9 = alienres
alieny_change9 = 0

# alien10

alienimg10 = pygame.image.load("aal.jpg")
alienx10 = 560
alieny10 = alienres
alieny_change10 = 0


def pause(x, y):
    pausebool = True

    while pausebool:
        for event in pygame.event.get():

            screen.fill((0, 0, 0))
            pausetext = font.render("PRESS [SPACE]  TO RESUME", True, (255, 255, 255))
            pausetexttwo = font.render("PRESS [Q]  TO QUIT", True, (255, 255, 255))
            screen.blit(pausetext, (x, y))
            screen.blit(pausetexttwo, (x, (y + 50)))
            pygame.display.update()

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:     #COUNTINUE
                    pausebool = False
                    break
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        #screen.fill((0,0,0))






#STAR1

star1i = pygame.image.load("pixil-frame-0 (4).png")
star1x = random.randint(20, 592)
star1y = random.randint(-100, -25)
st1ych = bgsp

#STAR2

star2i = pygame.image.load("pixil-frame-0 (5).png")
star2x = random.randint(20, 592)
star2y = random.randint(-175, -100)
st2ych = bgsp

#STAR3

star3i = pygame.image.load("pixil-frame-0 (6).png")
star3x = random.randint(20, 592)
star3y = random.randint(-250, -175)
st3ych = bgsp

#STAR4

star4i = pygame.image.load("pixil-frame-0 (4).png")
star4x = random.randint(20, 592)
star4y = random.randint(-400, -325)
st4ych = bgsp

#STAR5

star5i = pygame.image.load("pixil-frame-0 (5).png")
star5x = random.randint(20, 592)
star5y = random.randint(-475, -400)
st5ych = bgsp

#STAR6

star6i = pygame.image.load("pixil-frame-0 (6).png")
star6x = random.randint(20, 592)
star6y = random.randint(-550, -475)
st6ych = bgsp

#STAR7

star7i = pygame.image.load("pixil-frame-0 (6).png")
star7x = random.randint(20, 592)
star7y = random.randint(-625, -550)
st7ych = bgsp

#STAR8

star8i = pygame.image.load("pixil-frame-0 (5).png")
star8x = random.randint(20, 592)
star8y = random.randint(-700, -625)
st8ych = bgsp

#STAR9

star9i = pygame.image.load("pixil-frame-0 (5).png")
star9x = random.randint(20, 592)
star9y = random.randint(-775, -700)
st9ych = bgsp


def player():
    screen.blit(playerimg, (playerx, playery))


def alien():
    screen.blit(alienimg, (alienx, alieny))


def alien2():
    screen.blit(alienimg2, (alienx2, alieny2))


def alien3():
    screen.blit(alienimg3, (alienx3, alieny3))


def alien4():
    screen.blit(alienimg4, (alienx4, alieny4))


def alien5():
    screen.blit(alienimg5, (alienx5, alieny5))


def alien6():
    screen.blit(alienimg6, (alienx6, alieny6))


def alien7():
    screen.blit(alienimg7, (alienx7, alieny7))


def alien8():
    screen.blit(alienimg8, (alienx8, alieny8))


def alien9():
    screen.blit(alienimg9, (alienx9, alieny9))


def alien10():
    screen.blit(alienimg10, (alienx10, alieny10))

#STAR FUNC_________________________________________________________________________________________

def star1():
    screen.blit(star1i, (star1x, star1y))

def star2():
    screen.blit(star2i, (star2x, star2y))

def star3():
    screen.blit(star3i, (star3x, star3y))

def star4():
    screen.blit(star4i, (star4x, star4y))

def star5():
    screen.blit(star5i, (star5x, star5y))

def star6():
    screen.blit(star6i, (star6x, star6y))

def star7():
    screen.blit(star7i, (star7x, star7y))

def star8():
    screen.blit(star8i, (star8x, star8y))

def star9():
    screen.blit(star9i, (star9x, star9y))

#COLLISION FUNCTION

def iscol(enemyX, enemyY, playerX, playerY):
    distance = math.sqrt(math.pow(enemyX - playerX, 2) + (math.pow(enemyY - playerY, 2)))
    if distance < 30:
        return True
    else:
        return False

#LIVES DISPLAY--------------------------------------------------

def lives(x, y):
    lll = font.render(str(live), True, (255, 255, 255))
    screen.blit(lll, (x, y))


def points(x, y):
    pointp = font.render(("POINTS : " + str(flt_int(pygame.time.get_ticks() / 200))), True, (255, 255, 255))
    screen.blit(pointp, (x, y))

if point > highs:
    highs = point

def hi(x, y):
    high_ = ("HI: "+str(highs))
    hip = font.render(str(high_), True, (255, 255, 255))
    screen.blit(hip, (x, y))

h2 = pygame.image.load("h2.jpg")

count = 0
# Game Loop
running = True
while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # KEYDOWN EVENT

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            if event.key == pygame.K_LEFT:
                playerx_change = -1.5
            if event.key == pygame.K_RIGHT:
                playerx_change = 1.5
            if event.key == pygame.K_SPACE:
                pause(70,300)
        # KEYUP EVENT
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0

    # PLAYER BOUNDS


    if playerx <= 21:
        playerx = 21
    elif playerx >= 550:
        playerx = 550


# ALIEN RESPAWN AND RANDOM _________________________________-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

    if whatalien == 1:
        alien()
        alieny_change = aspeed
    if alieny == 865:
        alieny = alienres
        alieny_change = 0
        whatalien = random.randint(1, 10)
        pass

    if whatalien == 2:
        alien2()
        alieny_change2 = aspeed
    if alieny2 == 865:
        alieny2 = alienres
        alieny_change2 = 0
        whatalien = random.randint(1, 10)
        pass

    if whatalien == 3:
        alien3()
        alieny_change3 = aspeed
    if alieny3 == 865:
        alieny3 = alienres
        alieny_change3 = 0
        whatalien = random.randint(1, 10)
        pass

    if whatalien == 4:
        alien4()
        alieny_change4 = aspeed
    if alieny4 == 865:
        alieny4 = alienres
        alieny_change4 = 0
        whatalien = random.randint(1, 10)
        pass

    if whatalien == 5:
        alien5()
        alieny_change5 = aspeed
    if alieny5 == 865:
        alieny5 = alienres
        alieny_change5 = 0
        whatalien = random.randint(1, 10)
        pass

    if whatalien == 6:
        alien6()
        alieny_change6 = aspeed
    if alieny6 == 865:
        alieny6 = alienres
        alieny_change6 = 0
        whatalien = random.randint(1, 10)
        pass

    if whatalien == 7:
        alien7()
        alieny_change7 = aspeed
    if alieny7 == 865:
        alieny7 = alienres
        alieny_change7 = 0
        whatalien = random.randint(1, 10)
        pass

    if whatalien == 8:
        alien8()
        alieny_change8 = aspeed
    if alieny8 == 865:
        alieny8 = alienres
        alieny_change8 = 0
        whatalien = random.randint(1, 10)
        pass

    if whatalien == 9:
        alien9()
        alieny_change9 = aspeed
    if alieny9 == 865:
        alieny9 = alienres
        alieny_change9 = 0
        whatalien = random.randint(1, 10)
        pass

    if whatalien == 10:
        alien10()
        alieny_change10 = aspeed
    if alieny10 == 865:
        alieny10 = alienres
        alieny_change10 = 0
        whatalien = random.randint(1, 10)
        pass

    #BACKGROUND

    if star1y >= 880:
        star1y = 0.01
        star1x = random.randint(20, 592)

    if star2y >= 880:
        star2y = 0.01
        star2x = random.randint(20, 592)

    if star3y >= 880:
        star3y = 0.01
        star3x = random.randint(20, 592)

    if star4y >= 880:
        star4y = 0.01
        star4x = random.randint(20, 592)

    if star5y >= 880:
        star5y = 0.01
        star5x = random.randint(20, 592)

    if star6y >= 880:
        star6y = 0.01
        star6x = random.randint(20, 592)

    if star7y >= 880:
        star7y = 0.01
        star7x = random.randint(20, 592)

    if star8y >= 880:
        star8y = 0.01
        star8x = random.randint(20, 592)

    if star9y >= 880:
        star9y = 0.01
        star9x = random.randint(20, 592)


    #ALIEN RANDOM IMAGE GENERATION_______________________________________________________________

    xx = random.randint(1,500)

    if xx == 3:
        xxx = random.randint(1, 10)
        if xxx == 1:
            if alieny <= 0:
                alienimg = pygame.image.load("output-onlinepngtools.png")
        if xxx == 2:
            if alieny2 <= 0:
                alienimg2 = pygame.image.load("output-onlinepngtools.png")
        if xxx == 3:
            if alieny3 <= 0:
                alienimg3 = pygame.image.load("output-onlinepngtools.png")
        if xxx == 4:
            if alieny4 <= 0:
                alienimg4 = pygame.image.load("output-onlinepngtools.png")
        if xxx == 5:
            if alieny5 <= 0:
                alienimg5 = pygame.image.load("output-onlinepngtools.png")
        if xxx == 6:
            if alieny6 <= 0:
                alienimg6 = pygame.image.load("output-onlinepngtools.png")
        if xxx == 7:
            if alieny7 <= 0:
                alienimg7 = pygame.image.load("output-onlinepngtools.png")
        if xxx == 8:
            if alieny8 <= 0:
                alienimg8 = pygame.image.load("output-onlinepngtools.png")
        if xxx == 9:
            if alieny9 <= 0:
                alienimg9 = pygame.image.load("output-onlinepngtools.png")
        if xxx == 10:
            if alieny10 <= 0:
                alienimg10 = pygame.image.load("output-onlinepngtools.png")

    xix = random.randint(1, 500)

    if xix == 3:
        ixxx = random.randint(1, 10)
        if ixxx == 1:
            if alieny <= 0:
                alienimg = pygame.image.load("alien1.jpg")
        if ixxx == 2:
            if alieny2 <= 0:
                alienimg2 = pygame.image.load("alien1.jpg")
        if ixxx == 3:
            if alieny3 <= 0:
                alienimg3 = pygame.image.load("alien1.jpg")
        if ixxx == 4:
            if alieny4 <= 0:
                alienimg4 = pygame.image.load("alien1.jpg")
        if ixxx == 5:
            if alieny5 <= 0:
                alienimg5 = pygame.image.load("alien1.jpg")
        if ixxx == 6:
            if alieny6 <= 0:
                alienimg6 = pygame.image.load("alien1.jpg")
        if ixxx == 7:
            if alieny7 <= 0:
                alienimg7 = pygame.image.load("alien1.jpg")
        if ixxx == 8:
            if alieny8 <= 0:
                alienimg8 = pygame.image.load("alien1.jpg")
        if ixxx == 9:
            if alieny9 <= 0:
                alienimg9 = pygame.image.load("alien1.jpg")
        if ixxx == 10:
            if alieny10 <= 0:
                alienimg10 = pygame.image.load("alien1.jpg")

    xxh = random.randint(1, 500)

    if xxh == 2:
        xxx = random.randint(1, 10)
        if xxx == 1:
            if alieny <= 0:
                alienimg = pygame.image.load("imgonline-com-ua-resize-QNKruO1Q3EfVZ.jpg")
        if xxx == 2:
            if alieny2 <= 0:
                alienimg2 = pygame.image.load("imgonline-com-ua-resize-QNKruO1Q3EfVZ.jpg")
        if xxx == 3:
            if alieny3 <= 0:
                alienimg3 = pygame.image.load("imgonline-com-ua-resize-QNKruO1Q3EfVZ.jpg")
        if xxx == 4:
            if alieny4 <= 0:
                alienimg4 = pygame.image.load("imgonline-com-ua-resize-QNKruO1Q3EfVZ.jpg")
        if xxx == 5:
            if alieny5 <= 0:
                alienimg5 = pygame.image.load("imgonline-com-ua-resize-QNKruO1Q3EfVZ.jpg")
        if xxx == 6:
            if alieny6 <= 0:
                alienimg6 = pygame.image.load("imgonline-com-ua-resize-QNKruO1Q3EfVZ.jpg")
        if xxx == 7:
            if alieny7 <= 0:
                alienimg7 = pygame.image.load("imgonline-com-ua-resize-QNKruO1Q3EfVZ.jpg")
        if xxx == 8:
            if alieny8 <= 0:
               alienimg8 = pygame.image.load("imgonline-com-ua-resize-QNKruO1Q3EfVZ.jpg")
        if xxx == 9:
            if alieny9 <= 0:
                alienimg9 = pygame.image.load("imgonline-com-ua-resize-QNKruO1Q3EfVZ.jpg")
        if xxx == 10:
            if alieny10 <= 0:
                alienimg10 = pygame.image.load("imgonline-com-ua-resize-QNKruO1Q3EfVZ.jpg")

    xxhi = random.randint(1, 500)

    if xxhi == 2:
        xxxi = random.randint(1, 10)
        if xxxi == 1:
            if alieny <= 0:
                alienimg = pygame.image.load("aal.jpg")
        if xxxi == 2:
            if alieny2 <= 0:
                alienimg2 = pygame.image.load("aal.jpg")
        if xxxi == 3:
            if alieny3 <= 0:
                alienimg3 = pygame.image.load("aal.jpg")
        if xxxi == 4:
            if alieny4 <= 0:
                alienimg4 = pygame.image.load("aal.jpg")
        if xxxi == 5:
            if alieny5 <= 0:
                alienimg5 = pygame.image.load("aal.jpg")
        if xxxi == 6:
            if alieny6 <= 0:
                alienimg6 = pygame.image.load("aal.jpg")
        if xxxi == 7:
            if alieny7 <= 0:
                alienimg7 = pygame.image.load("aal.jpg")
        if xxxi == 8:
            if alieny8 <= 0:
                alienimg8 = pygame.image.load("aal.jpg")
        if xxxi == 9:
            if alieny9 <= 0:
                alienimg9 = pygame.image.load("aal.jpg")
        if xxxi == 10:
            if alieny10 <= 0:
                alienimg10 = pygame.image.load("aal.jpg")



    if alieny == random.randint(alienint1, alienint2) or alieny2 == random.randint(alienint1, alienint2) or alieny3 == random.randint(alienint1, alienint2) or alieny4 == random.randint(alienint1, alienint2) or alieny5 == random.randint(alienint1, alienint2) or alieny6 == random.randint(alienint1, alienint2) or alieny7 == random.randint(alienint1, alienint2) or alieny8 == random.randint(alienint1, alienint2) or alieny9 == random.randint(alienint1, alienint2) or alieny10 == random.randint(alienint1, alienint2):
        whatalien = random.randint(1, 10)

#COLLISION

    al1c = iscol(alienx, alieny, playerx, playery)
    al2c = iscol(alienx, alieny, playerx, playery)
    al3c = iscol(alienx, alieny, playerx, playery)
    al4c = iscol(alienx, alieny, playerx, playery)
    al5c = iscol(alienx, alieny, playerx, playery)
    al6c = iscol(alienx, alieny, playerx, playery)
    al7c = iscol(alienx, alieny, playerx, playery)
    al8c = iscol(alienx, alieny, playerx, playery)
    al9c = iscol(alienx, alieny, playerx, playery)
    al10c = iscol(alienx, alieny, playerx, playery)


    #if al1c == True or al2c == True or al3c == True or al4c == True or al5c == True or al6c == True or al7c == True or al1c == True or al1c == True or al1c == True or al1c == True or:
       # live -= 1




    star1()
    star2()
    star3()
    star4()
    star5()
    star6()
    star7()
    star8()
    star9()




    #Collision____________________________________

    playercol = iscol(alienx, alieny, playerx, playery)
    playercol2 = iscol(alienx2, alieny2, playerx, playery)
    playercol3 = iscol(alienx3, alieny3, playerx, playery)
    playercol4 = iscol(alienx4, alieny4, playerx, playery)
    playercol5 = iscol(alienx5, alieny5, playerx, playery)
    playercol6 = iscol(alienx6, alieny6, playerx, playery)
    playercol7 = iscol(alienx7, alieny7, playerx, playery)
    playercol8 = iscol(alienx8, alieny8, playerx, playery)
    playercol9 = iscol(alienx9, alieny9, playerx, playery)
    playercol10 = iscol(alienx10, alieny10, playerx, playery)

    if playercol == True or playercol2 == True or playercol3 == True or playercol4 == True or playercol5 == True or playercol6 == True or playercol7 == True or playercol8 == True or playercol9 == True or playercol10 == True:

        #live -= 1
        print(live)
        playercol == False
        playercol2 == False
        playercol3 == False
        playercol4 == False
        playercol5 == False
        playercol6 == False
        playercol7 == False
        playercol8 == False
        playercol9 == False
        playercol10 == False

        collide = True


    if collide == True :
        live -= 1

        alieny = -55
        alieny2 = -95
        alieny3 = -95
        alieny4 = -95
        alieny5 = -55
        alieny6 = -55
        alieny7 = -95
        alieny8 = -95
        alieny9 = -55
        alieny10 = -76

        #time.sleep(15/10)

        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(80, 25, 52, 48))
        lives(47.5, 20)
        playerimg = pygame.image.load('player_flash.png')
        player()
        pygame.display.update()
        time.sleep(3/10)

        screen.blit(h2, (80, 25))
        lives(47.5, 20)
        playerimg = pygame.image.load('battleship.png')
        player()
        pygame.display.update()
        time.sleep(3 / 10)

        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(80, 25, 52, 48))
        lives(47.5, 20)
        playerimg = pygame.image.load('player_flash.png')
        player()
        pygame.display.update()
        time.sleep(3 / 10)

        screen.blit(h2, (80, 25))
        lives(47.5, 20)
        playerimg = pygame.image.load('battleship.png')
        player()
        pygame.display.update()
        time.sleep(3 / 10)

        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(80, 25, 52, 48))
        lives(47.5, 20)
        playerimg = pygame.image.load('player_flash.png')
        player()
        pygame.display.update()
        time.sleep(3 / 10)

        screen.blit(h2, (80, 25))
        lives(47.5, 20)
        playerimg = pygame.image.load('battleship.png')
        player()
        pygame.display.update()
        time.sleep(3 / 10)

        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(80, 25, 52, 48))
        lives(47.5, 20)
        playerimg = pygame.image.load('player_flash.png')
        player()
        pygame.display.update()
        time.sleep(3 / 10)

        screen.blit(h2, (80, 25))
        lives(47.5, 20)
        playerimg = pygame.image.load('battleship.png')
        player()
        pygame.display.update()

        collide = False


    star1y += st1ych
    star2y += st2ych
    star3y += st3ych
    star4y += st4ych
    star5y += st1ych
    star6y += st6ych
    star7y += st7ych
    star8y += st8ych
    star9y += st9ych

    playerx += playerx_change

    alieny += alieny_change
    alieny2 += alieny_change2
    alieny3 += alieny_change3
    alieny4 += alieny_change4
    alieny5 += alieny_change5
    alieny6 += alieny_change6
    alieny7 += alieny_change7
    alieny8 += alieny_change8
    alieny9 += alieny_change9
    alieny10 += alieny_change10



    player()

    if collide == False and pausebool == False:
        alien()
        alien2()
        alien3()
        alien4()
        alien5()
        alien6()
        alien7()
        alien8()
        alien9()
        alien10()


  # TOP BORDER

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 640, 100))
    pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(0, 100, 640, 5))

    # HEARTS
    screen.blit(h2, (80, 25))
    lives(47.5, 20)

    #POINTS AND HISCORE

    #hi(400, 21)
    points(200, 21)

    pauset = fonttwo.render("PRESS SPACE", True, (255, 255, 255))
    pausett = fonttwo.render("TO PAUSE", True, (255, 255, 255))
    screen.blit(pauset, (500, 21))
    screen.blit(pausett, (500, 46))

    if live <= 0:
        screen.fill('black')

        endtxt = font.render("GAME OVER", True, (255, 255, 255))

        screen.blit(endtxt, (300, 300))

    pygame.display.update()

