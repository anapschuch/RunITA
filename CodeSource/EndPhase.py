from CodeSource.Cenario import *


class EndPhase(Screen):
    def __init__(self, x, y, img):
        super().__init__()
        self.x = x
        self.y = y
        self.img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.img, (60, 60))

    def print(self):
        if self.x + Cenario.pos_x < self.screen_x and self.y + Cenario.pos_y < self.screen_y:
            self.screen.blit(self.img, (self.x + Cenario.pos_x, self.y + Cenario.pos_y))
