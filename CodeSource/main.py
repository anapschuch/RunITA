from Player import*
from Cenario import*
import pygame
import os

#Inicializando o pygame
pygame.init()
CLOCK = pygame.time.Clock()

cenario = Cenario(1)
player = Player('img/player4.png')

#Title and Icon
pygame.display.set_caption("RunITA")
icon = pygame.image.load('img/logo.png')
pygame.display.set_icon(icon)

#Some game parameters
FPS = 200

#Game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
            pressed_key = pygame.key.name(event.key)
            player.update_pressed_key(pressed_key, event.type)

    player.update_positions()
    cenario.print_cenario()
    player.print_player()
    pygame.display.update()
    CLOCK.tick(FPS)
