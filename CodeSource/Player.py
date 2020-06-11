from CodeSource.Personagem import *

BLACK = (0, 0, 0, 255)


class Player(Personagem):
    def __init__(self, img_path):
        super().__init__(img_path, 33, 80)
        self.x = self.abs_x
        self.y = self.abs_y

    def update_positions(self):
        if self.check_next_move():
            self.abs_x += self.x_change
            self.abs_y += self.y_change

            if self.abs_x > Cenario.size_x - self.size_x:
                self.abs_x = Cenario.size_x - self.size_x
            elif self.abs_x < 0:
                self.abs_x = 0

            if self.abs_y > Cenario.size_y - self.size_y:
                self.abs_y = Cenario.size_y - self.size_y
            elif self.abs_y < 0:
                self.abs_y = 0

            if self.abs_x < self.start_scroll_x:
                self.x = self.abs_x
            elif self.abs_x > Cenario.size_x - self.start_scroll_x:
                self.x = self.abs_x - Cenario.size_x + self.screen_x
            else:
                self.x = self.start_scroll_x
                Cenario.pos_x += -self.x_change

            if self.abs_y < self.start_scroll_y:
                self.y = self.abs_y
            elif self.abs_y > Cenario.size_y - self.start_scroll_y:
                self.y = self.abs_y - Cenario.size_y + self.screen_y
            else:
                self.y = self.start_scroll_y
                Cenario.pos_y += -self.y_change

    def update_pressed_key(self, pressed_key, type):
        if type == pygame.KEYDOWN:
            if pressed_key == 'left':
                self.x_change = -self.move
            elif pressed_key == 'right':
                self.x_change = self.move
            elif pressed_key == 'up':
                self.y_change = -self.move
            elif pressed_key == 'down':
                self.y_change = self.move
            elif pressed_key == 'r':
                self.move += 0.1
            elif pressed_key == 'l':
                print(self.abs_x, self.abs_y)

        if type == pygame.KEYUP:
            if pressed_key == 'left' or pressed_key == 'right':
                self.x_change = 0
            elif pressed_key == 'up' or pressed_key == 'down':
                self.y_change = 0

    def print(self):
        self.screen.blit(self.img, (self.x, self.y))
