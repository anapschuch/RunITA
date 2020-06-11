from CodeSource.Inimigo import *


class InimigoEsperto(Inimigo):
    def __init__(self, img_path, x_init, y_init):
        super().__init__(img_path, x_init, y_init)
        self.has_moved = False
        self.last_change = 0

    # A ideia é tentar aproximar o inimigo do player
    # como se o inimigo seguisse o player
    def define_next_position(self, player):
        if not self.check_next_move() or (
                self.check_next_move() and pygame.time.get_ticks() > self.last_change + 20):

            self.x_change = 0
            self.y_change = 0

            self.has_moved = False

            if self.abs_x < player.abs_x - 2:
                self.x_change = self.move
            elif self.abs_x > player.abs_x + 2:
                self.x_change = -self.move

            if self.check_next_move():
                self.has_moved = True
            else:
                self.x_change = 0

            if self.abs_y < player.abs_y - 2:
                self.y_change = self.move
            elif self.abs_y > player.abs_y + 2:
                self.y_change = -self.move

            if self.check_next_move():
                self.has_moved = True
            else:
                self.y_change = 0

            if self.has_moved:
                self.last_change = pygame.time.get_ticks()

        self.abs_x = self.abs_x + self.x_change
        self.abs_y = self.abs_y + self.y_change
