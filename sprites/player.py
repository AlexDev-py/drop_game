import pygame
pygame.init()

load = pygame.image.load
scale = pygame.transform.scale

class Player:

    def __init__(self):
        self.position = [208, 525]

        self.move_direction = None
        self.player_direction = 'right'
        self.leg = 1
        self.animation_time = 0

        self.r_r = scale(load('sprites/img/r_r.png'), (83, 140))
        self.r_l = scale(load('sprites/img/r_l.png'), (83, 140))
        self.r_t = scale(load('sprites/img/r_t.png'), (83, 140))

        self.l_r = scale(load('sprites/img/l_r.png'), (83, 140))
        self.l_l = scale(load('sprites/img/l_l.png'), (83, 140))
        self.l_t = scale(load('sprites/img/l_t.png'), (83, 140))

        self.lose_l = scale(load('sprites/img/lose_l.png'), (83, 70))
        self.lose_r = scale(load('sprites/img/lose_r.png'), (83, 70))

        self.rect_r_r = self.r_r.get_rect(x=self.position[0], y=self.position[1])
        self.rect_r_l = self.r_l.get_rect(x=self.position[0], y=self.position[1])
        self.rect_r_t = self.r_t.get_rect(x=self.position[0], y=self.position[1])

        self.rect_l_r = self.l_r.get_rect(x=self.position[0], y=self.position[1])
        self.rect_l_l = self.l_l.get_rect(x=self.position[0], y=self.position[1])
        self.rect_l_t = self.l_t.get_rect(x=self.position[0], y=self.position[1])

        self.rect_lose_l = self.lose_l.get_rect(x=self.position[0], y=596)
        self.rect_lose_r = self.lose_r.get_rect(x=self.position[0], y=596)

    def update_rect(self):
        self.rect_r_r = self.r_r.get_rect(x=self.position[0], y=self.position[1])
        self.rect_r_l = self.r_l.get_rect(x=self.position[0], y=self.position[1])
        self.rect_r_t = self.r_t.get_rect(x=self.position[0], y=self.position[1])

        self.rect_l_r = self.l_r.get_rect(x=self.position[0], y=self.position[1])
        self.rect_l_l = self.l_l.get_rect(x=self.position[0], y=self.position[1])
        self.rect_l_t = self.l_t.get_rect(x=self.position[0], y=self.position[1])

        self.rect_lose_l = self.lose_l.get_rect(x=self.position[0], y=596)
        self.rect_lose_r = self.lose_r.get_rect(x=self.position[0], y=596)

    def blit(self, lose, pause):
        if self.position[0] + 83 >= 500 and self.move_direction == 'right' or self.position[0] <= 0 and self.move_direction == 'left':
            if self.move_direction and self.move_direction == self.player_direction:
                self.player_direction = 'left' if self.player_direction == 'right' else 'right'
                self.move_direction = None
            self.move_direction = None
            return [self.l_t, self.rect_l_t] if self.player_direction == 'left' else [self.r_t, self.rect_r_t]

        if lose:
            return [self.lose_l, self.rect_lose_l] if self.player_direction == 'left' else [self.lose_r, self.rect_lose_r]

        if pause:
            return [self.l_t, self.rect_l_t] if self.player_direction == 'left' else [self.r_t, self.rect_r_t]

        if self.move_direction is not None:
            if self.animation_time >= 5:
                self.animation_time = 0
                self.leg = 1 if self.leg == 2 else 2

            if self.player_direction == 'right':
                self.position[0] += 15
                self.animation_time += 1
                self.update_rect()
                return [self.r_l, self.rect_r_l] if self.leg == 2 else [self.r_r, self.rect_r_r]

            elif self.player_direction == 'left':
                self.position[0] -= 15
                self.animation_time += 1
                self.update_rect()
                return [self.l_l, self.rect_l_l] if self.leg == 2 else [self.l_r, self.rect_l_r]

        else:
            return [self.l_t, self.rect_l_t] if self.player_direction == 'left' else [self.r_t, self.rect_r_t]

    def check(self, box, lose, pause):
        if not lose and not pause:
            self.update_rect()
            if self.rect_r_t.right >= box.left >= self.rect_r_t.left or self.rect_r_t.right >= box.right >= self.rect_r_t.left:
                if self.rect_r_t.top < box.bottom:
                    return True
