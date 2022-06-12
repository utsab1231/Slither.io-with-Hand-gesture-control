import pygame
from object import Object


class Segment(Object):

    def __init__(self, x, y, w, h, filepath, speed):
        super().__init__(x, y, w, h, filepath)
        self.speed = speed

    def update(self, targetpos):
        direction = [targetpos[0] - self.rect.x, targetpos[1] - self.rect.y]
        length = (direction[0] ** 2 + direction[1] ** 2) ** 0.5
        if length<self.rect.w/2:
            return
        direction[0] /= length
        direction[1] /= length

        self.rect.x += direction[0] * self.speed
        self.rect.y += direction[1] * self.speed
