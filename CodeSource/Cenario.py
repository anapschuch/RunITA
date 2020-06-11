from CodeSource.Screen import *

BLACK = (0, 0, 0, 255)


class Cenario(Screen):
    move_image = None
    phase = 0
    pos_x = 0
    pos_y = 0
    size_x = 0
    size_y = 0

    def __init__(self, phase):
        super().__init__()
        Cenario.phase = phase
        Cenario.move_image = pygame.image.load('img/movemap.png')

        # A ideia é carregar os arquivos de imagem para cada fase
        self.cenario_image = pygame.image.load('img/movemap.png')

        Cenario.size_x, Cenario.size_y = self.move_image.convert().get_rect().size

        Cenario.pos_x = 0
        Cenario.pos_y = 0

    @staticmethod
    def get_color(x, y):
        return Cenario.move_image.get_at((int(x), int(y)))

    def print_cenario(self):
        self.screen.blit(self.cenario_image, (Cenario.pos_x, Cenario.pos_y))
