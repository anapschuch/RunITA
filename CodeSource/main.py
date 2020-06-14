from CodeSource.Player import *
from CodeSource.Bullets import *
from CodeSource.RandomEnemy import *
from CodeSource.SmartEnemy import *
from pygame.locals import *
import pygame
import ast
import sys


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


def main_menu():
    click = False
    BackGround = Background('img/coronavirus-4.jpg', [0, 0])
    pygame.mixer.init()
    pygame.mixer.music.load('trilha_sonora.wav')
    pygame.mixer.music.play(-1)
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
    lives = 4
    points = 0
    CLOCK = pygame.time.Clock()

    arquivo = open('dados.txt', 'r')
    dados = arquivo.read()
    dados = ast.literal_eval(dados)

    player_img = 'img/coronavirus.png'
    enemy_img = 'img/enemy2.png'
    end_img = 'img/endphase.png'
    heart_img = 'img/heart.png'
    bullet_img = 'img/bullets2.png'
    bullets_points_img = 'img/bullets_points.png'

    lives_img = pygame.image.load(heart_img)
    lives_img = pygame.transform.scale(lives_img, (15, 15))

    num_phases = len(dados)
    phase = 0

    while phase < num_phases:
        running = True
        dados_phase = dados[phase]

        screen = Screen()
        cenario = Cenario(phase)
        bullets = Bullets(dados_phase['bullets'], bullet_img)
        bullets_points = Bullets(dados_phase['bullets2'], bullets_points_img)
        endPhase = OneBullet(dados_phase['end_phase'][0], dados_phase['end_phase'][1], end_img, 60)

        player = Player(player_img, dados_phase['player'][0], dados_phase['player'][1], lives, points)

        smart_enemy_list = []
        for i in range(len(dados_phase['inimigo_esperto'])):
            pos = dados_phase['inimigo_esperto'][i]
            smart_enemy_list.append(SmartEnemy(enemy_img, pos[0], pos[1]))

        enemy_rand_list = []
        for i in range(len(dados_phase['inimigo_aleatorio'])):
            pos = dados_phase['inimigo_aleatorio'][i]
            enemy_rand_list.append(RandomEnemy(enemy_img, pos[0], pos[1]))

        # Title and Icon
        pygame.display.set_caption("RunITA")
        icon = pygame.image.load('img/coronavirus.png')
        pygame.display.set_icon(icon)

        # Some game parameters
        FPS = 200

        collision_time = -10

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
                    pressed_key = pygame.key.name(event.key)
                    player.update_pressed_key(pressed_key, event.type)

            player.update_positions()

            for i in range(len(enemy_rand_list)):
                enemy_rand_list[i].define_next_position()

            for i in range(len(smart_enemy_list)):
                smart_enemy_list[i].define_next_position(player)

            cenario.print_cenario()

            if bullets_points.check_collision(player.get_rect()):
                player.increase_points()

            if bullets.check_collision(player.get_rect()):
                collision_time = pygame.time.get_ticks() / 1000
                player.increase_velocity()
                player.increase_points()
            else:
                if pygame.time.get_ticks() / 1000 - collision_time > 7:
                    player.set_normal_velocity()

            bullets.draw_bullets()
            bullets_points.draw_bullets()

            for i in range(len(enemy_rand_list)):
                if enemy_rand_list[i].check_collision(player):
                    break

            for i in range(len(smart_enemy_list)):
                if smart_enemy_list[i].check_collision(player):
                    break

            player.print()

            for i in range(0, len(enemy_rand_list)):
                enemy_rand_list[i].print()

            for i in range(0, len(smart_enemy_list)):
                smart_enemy_list[i].print()

            endPhase.print()

            ### Lugar das informações do jogo
            pygame.draw.rect(screen.screen, BLACK, [0, 0, screen.screen_x, 25], 0)
            pygame.font.init()  # you have to call this at the start,
            fonte = pygame.font.SysFont('comicsansms', 20)
            texto = fonte.render('vidas -', False, (255, 255, 255))
            texto2 = fonte.render('pontuação -', False, (255, 255, 255))
            motivacional = fonte.render('Você é bom!', False, (255, 255, 255))
            pontos = fonte.render(str(player.get_points()), False, (255, 255, 255))

            vidas = player.get_lives()
            for i in range(vidas):
                screen.screen.blit(lives_img, (110+15*i, 0))

            screen.screen.blit(texto2, (190, 0))
            screen.screen.blit(texto, (50, 0))
            screen.screen.blit(pontos, (300, 0))
            if player.get_points() >= 500:
                screen.screen.blit(motivacional, (380, 0))

            pygame.display.update()
            CLOCK.tick(FPS)

            if endPhase.check_collision(player.get_rect()):
                lives = player.get_lives()
                points = player.get_points()
                running = False
            if player.get_lives() == -1:
                running = False
                gameover()

        phase += 1

    win()


def options():
    running = True
    BackGround = Background('img/coronavirus-4.jpg', [0, 0])
    while running:

        screen.fill([255, 255, 255])
        screen.blit(BackGround.image, BackGround.rect)
        draw_text('Controles e elementos do jogo:', font, (0, 255, 0), screen, 20, 20)
        draw_text('Setas do teclado - Movimentação', font, (0, 255, 0), screen, 40, 80)
        draw_text('Estrela - Aumento da velocidade do player', font, (0, 255, 0), screen, 40, 140)
        draw_text('Floco de neve - Aumento da pontuação', font, (0, 255, 0), screen, 40, 200)
        draw_text('Médico - Inimigo! Corra!', font, (0, 255, 0), screen, 40, 260)
        draw_text('Esc - Voltar', font, (0, 255, 0), screen, 40, 320)
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
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
                if event.key == K_r:
                    running = False

        pygame.display.update()
        mainClock.tick(60)
    game()


def win():
    running = True
    while running:
        screen.fill([0, 0, 0])
        draw_text('Você Venceu!', font, (0, 255, 0), screen, 20, 20)
        draw_text('Clique em R para recomeçar', font, (0, 255, 0), screen, 40, 80)
        draw_text('Clique em esc para sair :)', font, (0, 255, 0), screen, 40, 140)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
                if event.key == K_r:
                    running = False

        pygame.display.update()
        mainClock.tick(60)
    game()


pygame.init()
mainClock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption('RunITA!')
screen = pygame.display.set_mode((640, 360), 0, 32)
pygame.mixer.init()

font = pygame.font.SysFont('Bauhaus 93', 30)
main_menu()
