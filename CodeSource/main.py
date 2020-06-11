from CodeSource.Player import*
from CodeSource.Bullets import*
from CodeSource.InimigoAleatorio import*
from CodeSource.EndPhase import*
import pygame
import os
import sys

pygame.init()
mainClock = pygame.time.Clock()

from pygame.locals import *

pygame.init()
pygame.display.set_caption('RunITA!')
screen = pygame.display.set_mode((640, 360), 0, 32)

font = pygame.font.SysFont('Bauhaus 93', 30)



def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


def main_menu():
    BackGround = Background('img/coronavirus-4.jpg', [0, 0])
    while True:


        screen.fill([255, 255, 255])
        screen.blit(BackGround.image, BackGround.rect)
        draw_text('RunITA! - Menu Inicial', font, (0, 255, 0), screen, 100, 40)
        draw_text('Jogar', font, (0, 255, 0), screen, 270, 110)
        draw_text('Informações', font, (0, 255, 0), screen, 270, 210)
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def game():
    CLOCK = pygame.time.Clock()

    screen = Screen()
    cenario = Cenario(1)
    bullets = Bullets(1)
    player_img = 'img/coronavirus.png'
    enemy_img = 'img/enemy2.png'
    end_img = 'img/endphase.png'
    endPhase = EndPhase(585, 490, end_img)
    player = Player(player_img)

    enemy_list = []
    enemy_list.append(InimigoAleatorio(enemy_img, 95, 140))
    enemy_list.append(InimigoAleatorio(enemy_img, 100, 845))
    enemy_list.append(InimigoAleatorio(enemy_img, 515, 655))

    # Title and Icon
    pygame.display.set_caption("RunITA")
    icon = pygame.image.load('img/coronavirus.png')
    pygame.display.set_icon(icon)

    # Some game parameters
    FPS = 200

    collision_time = -10

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
                pressed_key = pygame.key.name(event.key)
                player.update_pressed_key(pressed_key, event.type)

        player.update_positions()

        for i in range(0, len(enemy_list)):
            enemy_list[i].define_next_position()

        cenario.print_cenario()

        if bullets.check_collision(player.get_rect()):
            collision_time = pygame.time.get_ticks() / 1000
            player.increase_velocity()
            player.increase_points()
        else:
            if pygame.time.get_ticks() / 1000 - collision_time > 7:
                player.set_normal_velocity()

        bullets.draw_bullets()

        for i in range(0, len(enemy_list)):
            enemy_list[i].check_collision(player)

        player.print()

        for i in range(0, len(enemy_list)):
            enemy_list[i].print()

        endPhase.print()

        ### Lugar das informações do jogo
        pygame.draw.rect(screen.screen, BLACK, [0, 0, screen.screen_x, 25], 0)
        pygame.font.init()  # you have to call this at the start,
        fonte = pygame.font.SysFont('comicsansms', 20)
        texto = fonte.render('vidas -', False, (255, 255, 255))
        texto2 = fonte.render('pontuação -', False, (255, 255, 255))
        motivacional = fonte.render('Você é bom!', False, (255, 255, 255))
        vidas = fonte.render(str(player.get_lives()), False, (255, 255, 255))
        pontos = fonte.render(str(player.get_points()), False, (255, 255, 255))
        screen.screen.blit(vidas, (120, 0))
        screen.screen.blit(texto2, (150, 0))
        screen.screen.blit(texto, (50, 0))
        screen.screen.blit(pontos, (265, 0))
        if player.get_points() >= 5:
            screen.screen.blit(motivacional, (305, 0))

        pygame.display.update()
        CLOCK.tick(FPS)

        if player.get_lives() == -1:
            running = False
            gameover()


def options():
    running = True
    BackGround = Background('img/coronavirus-4.jpg', [0, 0])
    while running:

        screen.fill([255, 255, 255])
        screen.blit(BackGround.image, BackGround.rect)
        draw_text('Controles e elementos do jogo:', font, (0, 255, 0), screen, 20, 20)
        draw_text('Setas do teclado - movimentação', font, (0, 255, 0), screen, 40, 80)
        draw_text('Estrela - PowerUps', font, (0, 255, 0), screen, 40, 140)
        draw_text('Fantasma - Inimigo! Corra!', font, (0, 255, 0), screen, 40, 200)
        draw_text('Esc - voltar', font, (0, 255, 0), screen, 40, 300)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


def gameover():
    running = True
    while running:

        screen.fill([0, 0, 0])
        draw_text('Você Morreu!', font, (0, 255, 0), screen, 20, 20)
        draw_text('Não desista! Clique em R para recomeçar', font, (0, 255, 0), screen, 40, 80)
        draw_text('Clique em esc para desistir :(', font, (0, 255, 0), screen, 40, 140)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
            if event.type == KEYDOWN:
                if event.key == K_r:
                    running = False

        pygame.display.update()
        mainClock.tick(60)
    game()


main_menu()

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
