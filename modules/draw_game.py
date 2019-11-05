import pygame
pygame.init()

color = pygame.Color


class DrawGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((500, 700))
        pygame.display.set_caption('project')

        self.player = None
        self.box = None
        self.lose = None
        self.pause = None
        self.score = None

    def draw_window(self):
        self.screen.fill(color('White'))
        text = f'очки: {self.score}'
        font = pygame.font.SysFont('oral', 20)
        text = font.render(text, 1, color('Black'))
        self.screen.blit(text, (10, text.get_height()))
        player = self.player.blit(self.lose, self.pause)
        if self.player.check(self.box.rect_box, self.lose, self.pause):
            self.lose = True
        if player:
            self.screen.blit(player[0], player[1])
        box = self.box.blit(self.player.position, self.lose, self.pause, self.score)
        if box:
            self.screen.blit(box.box, box.rect_box)
        pygame.draw.rect(self.screen, color('Brown'), pygame.Rect(0, 665, 500, 700))
        pygame.display.flip()
