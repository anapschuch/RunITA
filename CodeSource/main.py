from CodeSource.Player import*
from CodeSource.Cenario import*
from CodeSource.Bullets import*
import pygame
import os

#Inicializando o pygame
pygame.init()
CLOCK = pygame.time.Clock()

cenario = Cenario(1)
bullets = Bullets(1)
player_img = 'img/coronavirus.png'
player = Player(player_img)

#Title and Icon
pygame.display.set_caption("RunITA")
icon = pygame.image.load('img/coronavirus.png')
pygame.display.set_icon(icon)

#Some game parameters
FPS = 200

collision_time = -10

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

    if bullets.check_collision(player.get_rect()):
        collision_time = pygame.time.get_ticks()/1000
        player.increase_velocity()
    else:
        if pygame.time.get_ticks()/1000 - collision_time > 7:
            player.set_normal_velocity()

    bullets.draw_bullets()

    player.print_player()
    pygame.display.update()
    CLOCK.tick(FPS)
