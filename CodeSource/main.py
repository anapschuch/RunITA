import pygame
import numpy as np

pygame.init()
displaySize = 500
IMAGE = pygame.image.load('coronavirus.png')
IMAGE = pygame.transform.scale(IMAGE, (50, 50))
win = pygame.display.set_mode((displaySize, displaySize))
pygame.display.set_caption("RunITA")
x = 200
y = 200
width = 40
height = 60
vel = 5

isJump = False
jumpCount = 5
run = True

while run:
    pygame.time.delay(25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel

    if keys[pygame.K_RIGHT] and x < displaySize - width - vel:
        x += vel

    if not (isJump):

        if keys[pygame.K_UP] and y > vel:
            y -= vel

        if keys[pygame.K_DOWN] and y < displaySize - height - vel:
            y += vel

        if keys[pygame.K_SPACE]:
            isJump = True

    else:
        if jumpCount >= -5:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 5
            isJump = False

    win.fill((0, 0, 0))
    win.blit(IMAGE, (x,y))
    pygame.display.update()

pygame.quit()
