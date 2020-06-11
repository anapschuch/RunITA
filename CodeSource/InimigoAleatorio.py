from CodeSource.Personagem import *
from random import randint
import time
BLACK = (0, 0, 0, 255)


class InimigoAleatorio(Personagem):
    def __init__(self, img_path, x_init, y_init):
        super().__init__(img_path, x_init, y_init)
        self.move = 0.5
        self.direction = randint(0, 3)
        self.last_collision = 0

    # definimos as direções como direita, esquerda, sobe e desce.
    # cada uma delas vale entre 0 e 3, nessa ordem
    def define_next_position(self):
        if self.direction == 0:
            self.x_change = self.move
            self.y_change = 0
        elif self.direction == 1:
            self.x_change = 0
            self.y_change = self.move
        elif self.direction == 2:
            self.x_change = -self.move
            self.y_change = 0
        else:
            self.x_change = 0
            self.y_change = - self.move

        if self.check_next_move():
            self.abs_x = self.abs_x + self.x_change
            self.abs_y = self.abs_y + self.y_change
        else:
            self.direction = randint(0, 3)

    def print(self):
        if self.abs_x + Cenario.pos_x < self.screen_x and self.abs_y + Cenario.pos_y < self.screen_y:
            self.screen.blit(self.img, (self.abs_x + Cenario.pos_x, self.abs_y + Cenario.pos_y))

    def check_collision(self, player):
        if self.get_rect().colliderect(player.get_rect()):
            if pygame.time.get_ticks() > self.last_collision + 1500:
                time.sleep(0.4)
                player.decrease_lives()
                self.last_collision = pygame.time.get_ticks()
