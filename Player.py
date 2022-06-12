import pygame
import pygame.constants

# from test import fuck
from snake import Snake
from segment import Segment


class Player(Snake):
    def __init__(self, x, y, w, h, filepath):
        super().__init__(x, y, w, h, filepath)

    def update(self, winsize):
        self.calculatedirection(winsize)
        super().update()

    def calculatedirection(self, winsize):
        mousepos = pygame.mouse.get_pos()
        worldpos = (mousepos[0] - winsize[0] / 2 + self.rect.x, mousepos[1] - winsize[1] / 2 + self.rect.y)

        self.direction = [worldpos[0] - self.rect.x, worldpos[1] - self.rect.y]

        length = (self.direction[0] ** 2 + self.direction[1] ** 2) ** 0.5

        self.direction = [self.direction[0] / length, self.direction[1] / length]
