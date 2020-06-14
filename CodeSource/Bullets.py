from CodeSource.OneBullet import *


class Bullets():
    """ Classe que agrupa bullets de um mesmo tipo (uma mesma imagem associada) """
    bullets_positions = []
    bullets = []

    def __init__(self, bullets_positions, img):
        self.bullets_positions = bullets_positions
        self.bullets = []
        self.img = img
        self.def_bullets()

    def def_bullets(self):
        for i in range(len(self.bullets_positions)):
            self.bullets.append(OneBullet(self.bullets_positions[i][0], self.bullets_positions[i][1], self.img, 25))

    def draw_bullets(self):
        for i in range(len(self.bullets)):
            self.bullets[i].print()

    def check_collision(self, player_rect):
        for i in range(len(self.bullets)):
            if self.bullets[i].check_collision(player_rect):
                self.bullets.remove(self.bullets[i])
                self.draw_bullets()
                return True
        return False
