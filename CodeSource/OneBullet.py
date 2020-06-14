from CodeSource.Cenario import *
from CodeSource.Screen import *


class OneBullet(Screen):
    """Classe para inserir no cenario elementos que podem colidir com o player"""
    def __init__(self, x, y, img, scale):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (scale, scale))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)

    def print(self):
        if self.x + Cenario.pos_x < self.screen_x and self.y + Cenario.pos_y < self.screen_y:
            self.screen.blit(self.image, (self.x + Cenario.pos_x, self.y + Cenario.pos_y))

    def check_collision(self, player_rect):
        return self.rect.colliderect(player_rect)
