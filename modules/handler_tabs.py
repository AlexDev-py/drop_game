import pygame
from pygame.locals import *
pygame.init()


class HandlerTabs:
    def __init__(self):

        self.lose = None
        self.pause = None
        self.player = None
        self.box = None
        self.game = None
        self.score = None

    def check(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                return True

            if event.type == KEYDOWN:
                if event.key == K_RIGHT and not self.pause and not self.lose:
                    self.player.move_direction = self.player.player_direction = 'right'

                elif event.key == K_LEFT and not self.pause and not self.lose:
                    self.player.move_direction = self.player.player_direction = 'left'

                elif event.key == K_SPACE:
                    self.pause = False if self.pause else True
                    if self.lose:
                        self.lose = False
                        self.player.move_direction = None
                        self.player.player_direction = 'right'
                        self.player.position = [208, 525]
                        self.box.get_box(self.player.position)
                        self.score = 0
                        self.box.last_score = 0
                        self.box.speed = 20
                        self.pause = False

            elif event.type == KEYUP:
                if event.key == K_RIGHT:
                    self.player.move_direction = None if self.player.player_direction == 'right' else self.player.move_direction

                elif event.key == K_LEFT:
                    self.player.move_direction = None if self.player.player_direction == 'left' else self.player.move_direction
