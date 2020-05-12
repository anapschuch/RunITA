from CodeSource.Cenario import *
from CodeSource.Screen import *


class OneBullet(Screen):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.bullet_image = pygame.image.load('img/bullets2.png')
        self.bullet_image = pygame.transform.scale(self.bullet_image, (25, 25))
        self.rect = self.bullet_image.get_rect()
        self.rect = self.rect.move(x, y)

    def draw_bullet(self):
        if - Cenario.pos_x + self.screen_x > self.x > Cenario.pos_x and -Cenario.pos_y + self.screen_y > \
                self.y > Cenario.pos_y:
            self.screen.blit(self.bullet_image, (self.x + Cenario.pos_x,
                                                 self.y + Cenario.pos_y))

    def get_rect(self):
        return self.rect
