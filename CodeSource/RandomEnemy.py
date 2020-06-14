from CodeSource.Enemy import*
from random import randint


class RandomEnemy(Enemy):
    """ Inimigo que anda numa mesma direção até não ser mais possível se mover.
    A partir daí, uma nova direção é escolhida aleatoriamente."""
    def __init__(self, img_path, x_init, y_init):
        super().__init__(img_path, x_init, y_init)
        self.direction = randint(0, 3)
        self.last_change = 0

    # definimos as direções como direita, sobe, esquerda e desce.
    # cada uma delas vale entre 0 e 3, nessa ordem
    def define_next_position(self):
        if self.direction == 0:
            self.x_change = self.move
            self.y_change = 0
        elif self.direction == 1:
            self.x_change = 0
            self.y_change = self.move
        elif self.direction == 2:
            self.x_change = - self.move
            self.y_change = 0
        else:
            self.x_change = 0
            self.y_change = - self.move

        if self.check_next_move():
            self.abs_x = self.abs_x + self.x_change
            self.abs_y = self.abs_y + self.y_change
        else:
            self.direction = randint(0, 3)
