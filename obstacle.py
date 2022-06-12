import pygame
import random
from object import Object


class Obstacle(Object):

    def __init__(self, x, y, w,h, filepath):
        super().__init__(x, y, w, h, filepath)

    def update(self, player):

        if self.rect.colliderect(player.rect):

            return True

        return False
