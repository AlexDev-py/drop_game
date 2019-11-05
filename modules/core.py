from .handler_tabs import HandlerTabs
from .draw_game import DrawGame
from sprites.player import Player
from sprites.box import Box
import pygame

pygame.init()
clock = pygame.time.Clock()


class Core(HandlerTabs, Player, Box, DrawGame):

    def __init__(self):
        HandlerTabs.__init__(self)
        DrawGame.__init__(self)

        self.player = Player()
        self.box = Box()
        self.lose = False
        self.pause = False

        self.game = True
        self.score = 0

    def start(self):
        while self.game:
            clock.tick(30)
            try:
                self.draw_window()
                tab = self.check()
                if tab:
                    self.game = False
                if not self.lose and not self.pause:
                    self.score += 1

            except Exception as error:
                print(f'{type(error).__name__}: {error}')
