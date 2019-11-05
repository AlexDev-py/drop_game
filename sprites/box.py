import pygame
import random
pygame.init()

load = pygame.image.load
scale = pygame.transform.scale

class Box:
    def __init__(self):
        self.position = None
        self.speed = 20
        self.counter_box = -1
        self.counter_box_end = 0
        self.get_counter_box_end()
        self.last_score = 0

        self.box = scale(load('sprites/img/box.png'), (80, 100))
        self.get_box([1, 1])
        self.rect_box = self.box.get_rect(x=self.position[0], y=self.position[1])

    def get_counter_box_end(self):
        self.counter_box_end = random.randint(1, 5)

    def get_box(self, player_position):
        self.counter_box += 1
        x = random.randint(50, 400)
        if self.counter_box >= self.counter_box_end:
            self.counter_box = 0
            self.get_counter_box_end()
            x = player_position[0]

        self.position = [x, -105]
        self.rect_box = self.box.get_rect(x=self.position[0], y=self.position[1])

    def blit(self, player_position, lose, pause, score):
        if not lose:
            if self.last_score + 300 == score:
                self.last_score = score
                self.speed += 5
            if not pause:
                if self.position[1] < 580:
                    self.position[1] += self.speed

                else:
                    self.get_box(player_position)

            self.rect_box = self.box.get_rect(x=self.position[0], y=self.position[1])
            return self
