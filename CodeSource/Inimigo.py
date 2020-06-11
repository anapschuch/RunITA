from CodeSource.Personagem import *


class Inimigo(Personagem):
    def __init__(self, img_path, x_init, y_init):
        super().__init__(img_path, x_init, y_init)
        self.move = 0.5
        self.last_collision = 0

    def print(self):
        if self.abs_x + Cenario.pos_x < self.screen_x and self.abs_y + Cenario.pos_y < self.screen_y:
            self.screen.blit(self.img, (self.abs_x + Cenario.pos_x, self.abs_y + Cenario.pos_y))

    def check_collision(self, player):
        if self.get_rect().colliderect(player.get_rect()):
            if pygame.time.get_ticks() > self.last_collision + 1500:
                player.decrease_lives()
                self.last_collision = pygame.time.get_ticks()
                return True
            return False
        return False
