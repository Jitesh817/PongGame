import pygame
import random

pygame.init()

display_width = 1200
display_height = 1000
paddleWidth = 7
paddleHeight = 100
boundary = (display_width * 0.015)+paddleWidth

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Pong - By Cloudsters')

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

img_width = 596

clock = pygame.time.Clock()
crashed = False


def paddle(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def ball(cx, cy, radius, color):
    pygame.draw.circle(gameDisplay, color, (cx, cy), radius, 1)


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def game_loop():
    p1x = (display_width * 0.015)
    p1y = (display_height - paddleHeight)/2

    p2x = display_width - (display_width * 0.015) - paddleWidth
    p2y = (display_height - paddleHeight)/2

    p3x = (display_width - paddleHeight)/2
    p3y = (display_width * 0.015)

    p4x = (display_width - paddleHeight)/2
    p4y = display_height - (display_width * 0.015) - paddleWidth

    cx = (display_width/2)
    cy = (display_height/2)

    vx = (random.randint(150, 250))/100
    vy = (random.randint(150, 250))/100

    speedInc = 0.001

    radius = 5

    p1y_change = 0
    p2y_change = 0
    p3x_change = 0
    p4x_change = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and p1y >= boundary:
                    p1y_change = -5
                elif event.key == pygame.K_DOWN and p1y + paddleHeight <= display_height-boundary:
                    p1y_change = 5
                else:
                    p1y_change = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    p1y_change = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP2 and p2y + paddleHeight <= display_height-boundary:
                    p2y_change = 5
                elif event.key == pygame.K_KP8 and p2y >= boundary:
                    p2y_change = -5
                else:
                    p2y_change = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_KP2 or event.key == pygame.K_KP8:
                    p2y_change = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d and p3x + paddleHeight <= display_width-boundary:
                    p3x_change = 5
                elif event.key == pygame.K_a and p3x >= boundary:
                    p3x_change = -5
                else:
                    p3x_change = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    p3x_change = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m and p4x + paddleHeight <= display_width-boundary:
                    p4x_change = 5
                elif event.key == pygame.K_b and p4x >= boundary:
                    p4x_change = -5
                else:
                    p4x_change = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_b or event.key == pygame.K_m:
                    p4x_change = 0

        p1y += p1y_change
        p2y += p2y_change
        p3x += p3x_change
        p4x += p4x_change

        if cy >= p1y and cy <= p1y + paddleHeight:
            if cx-radius <= p1x + paddleWidth:
                vx *= -1

        if cy >= p2y and cy <= p2y + paddleHeight:
            if cx+radius >= p2x:
                vx *= -1

        if cx >= p3x and cx <= p3x + paddleHeight:
            if cy-radius <= p3y + paddleWidth:
                vy *= -1

        if cx >= p4x and cx <= p4x + paddleHeight:
            if cy+radius >= p4y:
                vy *= -1

        if cx+vx <= 0:
            vx *= -1
        if cy+vy <= 0:
            vy *= -1

        if cx+vx >= display_width:
            vx *= -1
        if cy+vy >= display_height:
            vy *= -1

        cx = cx+vx
        cy = cy+vy

        gameDisplay.fill(black)
        paddle(p1x, p1y, paddleWidth, paddleHeight, white)
        paddle(p2x, p2y, paddleWidth, paddleHeight, blue)
        paddle(p3x, p3y, paddleHeight, paddleWidth, green)
        paddle(p4x, p4y, paddleHeight, paddleWidth, red)
        ball(cx, cy, radius, white)

        if vx > 0:
            vx += speedInc
        else:
            vx = (vx*-1 + speedInc)*-1

        if vy > 0:
            vy += speedInc
        else:
            vy = (vy*-1 + speedInc)*-1

        speedInc /= 1.20

        pygame.display.update()
        clock.tick(60)


pygame.key.set_repeat(1, 1)
game_loop()
pygame.quit()
quit()