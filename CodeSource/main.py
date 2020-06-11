from CodeSource.Player import*
from CodeSource.Bullets import*
from CodeSource.InimigoAleatorio import*
from CodeSource.EndPhase import*
import pygame

#Inicializando o pygame
pygame.init()
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

    for i in range(0, len(enemy_list)):
        enemy_list[i].define_next_position()

    cenario.print_cenario()

    if bullets.check_collision(player.get_rect()):
        collision_time = pygame.time.get_ticks()/1000
        player.increase_velocity()
    else:
        if pygame.time.get_ticks()/1000 - collision_time > 7:
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
    texto = fonte.render('Colocar informações do jogo aqui?', False, (255, 255, 255))
    vidas = fonte.render(str(player.get_lives()), False, (255, 255, 255))
    screen.screen.blit(vidas, (350, 5))
    screen.screen.blit(texto, (50, 5))

    pygame.display.update()
    CLOCK.tick(FPS)
