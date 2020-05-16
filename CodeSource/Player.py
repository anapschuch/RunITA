from CodeSource.Cenario import *

BLACK = (0, 0, 0, 255)


class Player(Screen):
    def __init__(self, img_path):
        super().__init__()
        self.abs_x = 33
        self.abs_y = 33
        self.x = self.abs_y
        self.y = self.abs_x
        self.player_x_change = 0
        self.player_y_change = 0
        self.player_img = pygame.image.load(img_path)
        self.player_img = pygame.transform.scale(self.player_img, (20, 20))
        self.player_size_x, self.player_size_y = self.player_img.convert().get_rect().size
        self.move = 1
        self.print_player()

    def update_pressed_key(self, pressed_key, type):
        if type == pygame.KEYDOWN:
            if pressed_key == 'left':
                self.player_x_change = -self.move
            elif pressed_key == 'right':
                self.player_x_change = self.move
            elif pressed_key == 'up':
                self.player_y_change = -self.move
            elif pressed_key == 'down':
                self.player_y_change = self.move
            elif pressed_key == 'r':
                self.move += 0.1
            elif pressed_key == 'l':
                print(self.abs_x, self.abs_y)

        if type == pygame.KEYUP:
            if pressed_key == 'left' or pressed_key == 'right':
                self.player_x_change = 0
            elif pressed_key == 'up' or pressed_key == 'down':
                self.player_y_change = 0

    def check_next_move(self):
        if Cenario.get_color(self.abs_x + self.player_x_change, self.abs_y + self.player_y_change) == BLACK:
            if Cenario.get_color(self.abs_x + self.player_x_change + self.player_size_x,
                                 self.abs_y + self.player_y_change + self.player_size_y) == BLACK:
                if Cenario.get_color(self.abs_x + self.player_x_change + self.player_size_x,
                                     self.abs_y + self.player_y_change) == BLACK:
                    if Cenario.get_color(self.abs_x + self.player_x_change,
                                         self.abs_y + self.player_y_change + self.player_size_y) == BLACK:
                        return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def update_positions(self):
        if self.check_next_move():
            self.abs_x += self.player_x_change
            self.abs_y += self.player_y_change

            if self.abs_x > Cenario.size_x - self.player_size_x:
                self.abs_x = Cenario.size_x - self.player_size_x
            elif self.abs_x < 0:
                self.abs_x = 0

            if self.abs_y > Cenario.size_y - self.player_size_y:
                self.abs_y = Cenario.size_y - self.player_size_y
            elif self.abs_y < 0:
                self.abs_y = 0

            if self.abs_x < self.start_scroll_x:
                self.x = self.abs_x
            elif self.abs_x > Cenario.size_x - self.start_scroll_x:
                self.x = self.abs_x - Cenario.size_x + self.screen_x
            else:
                self.x = self.start_scroll_x
                Cenario.pos_x += -self.player_x_change

            if self.abs_y < self.start_scroll_y:
                self.y = self.abs_y
            elif self.abs_y > Cenario.size_y - self.start_scroll_y:
                self.y = self.abs_y - Cenario.size_y + self.screen_y
            else:
                self.y = self.start_scroll_y
                Cenario.pos_y += -self.player_y_change

    def print_player(self):
        self.screen.blit(self.player_img, (self.x, self.y))

    def get_rect(self):
        rect = self.player_img.get_rect()
        return rect.move(self.abs_x, self.abs_y)

    def increase_velocity(self):
        self.move += 1

    def set_normal_velocity(self):
        self.move = 1
