from CodeSource.Cenario import *

BLACK = (0, 0, 0, 255)


# Classe para implementar inimigo e player
# Basicamente define as próximas posições de cada um
class Personagem(Screen):
    def __init__(self, img_path, x_init, y_init):
        super().__init__()
        self.abs_x = x_init
        self.abs_y = y_init
        self.x_change = 0
        self.y_change = 0
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (20, 20))
        self.size_x, self.size_y = self.img.convert().get_rect().size
        self.move = 1
        self.lives = 3

    def check_next_move(self):
        if Cenario.get_color(self.abs_x + self.x_change, self.abs_y + self.y_change) == BLACK:
            if Cenario.get_color(self.abs_x + self.x_change + self.size_x,
                                 self.abs_y + self.y_change + self.size_y) == BLACK:
                if Cenario.get_color(self.abs_x + self.x_change + self.size_x,
                                     self.abs_y + self.y_change) == BLACK:
                    if Cenario.get_color(self.abs_x + self.x_change,
                                         self.abs_y + self.y_change + self.size_y) == BLACK:
                        return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def get_rect(self):
        rect = self.img.get_rect()
        return rect.move(self.abs_x, self.abs_y)

    def increase_velocity(self):
        self.move += 0.5

    def set_normal_velocity(self):
        self.move = 1

    def decrease_lives(self):
        self.lives -= 1

    def get_lives(self):
        return self.lives
