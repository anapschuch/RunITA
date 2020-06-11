import pygame


class Screen(object):
    """Classe que seta os parâmetros principais da tela de jogo"""

    def __init__(self):
        self.screen_x = 640
        self.screen_y = 360
        self.screen = pygame.display.set_mode((self.screen_x, self.screen_y))
        self.start_scroll_x = self.screen_x / 2
        self.start_scroll_y = self.screen_y / 2
