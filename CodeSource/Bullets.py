from CodeSource.OneBullet import *


class Bullets(Cenario):
    bullets_positions = [(310, 380), (30, 845), (890, 585), (680, 265), (325, 205), (660, 815), (945, 30)]
    bullets = []

    def __init__(self, phase):
        super().__init__(phase)
        self.def_bullets()

    def def_bullets(self):
        for i in range(len(self.bullets_positions)):
            self.bullets.append(OneBullet(self.bullets_positions[i][0], self.bullets_positions[i][1]))

    def draw_bullets(self):
        for i in range(len(self.bullets)):
            self.bullets[i].draw_bullet()

    def check_collision(self, player_rect):
        for i in range(len(self.bullets)):
            if self.bullets[i].get_rect().colliderect(player_rect):
                self.bullets.remove(self.bullets[i])
                self.draw_bullets()
                break