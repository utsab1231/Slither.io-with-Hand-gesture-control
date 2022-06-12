import pygame
import random
from object import Object


class Orb(Object):

    def __init__(self, x, y, r, filepath):
        super().__init__(x, y, r, r, filepath)

    def update(self, player):

        if self.rect.colliderect(player.rect):
            player.score += 5
            return True

        return False
