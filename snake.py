import pygame
from object import Object
from segment import Segment


class Snake(Object):
    def __init__(self, x, y, w, h, filepath):
        super().__init__(x, y, w, h, filepath)
        self.speed = 5
        self.previousscore = 0
        self.score = 0
        self.texturepath=filepath

        self.segments = []
        self.direction = []


    def update(self):


        self.rect.x += self.direction[0] * self.speed
        self.rect.y += self.direction[1] * self.speed

        if self.score - self.previousscore >= 20:
            self.previousscore = self.score

            STARTX = self.direction[0] * -1 * self.rect.w / 2
            STARTY = self.direction[1] * -1 * self.rect.h / 2

            if len(self.segments) == 0:
                STARTX += self.rect.x
                STARTY += self.rect.y
            else:
                STARTX += self.segments[-1].rect.x
                STARTY += self.segments[-1].rect.y

            newsegment = Segment(STARTX, STARTY, self.rect.w, self.rect.h, self.texturepath, self.speed)
            self.segments.append(newsegment)

        for i in range(len(self.segments)):
            if i == 0:
                self.segments[i].update((self.rect.x, self.rect.y))
            else:
                self.segments[i].update((self.segments[i - 1].rect.x, self.segments[i - 1].rect.y))

    def draw(self, window, camera):
        window.blit(self.texture, camera.translate(self.rect.x, self.rect.y))

        for segment in self.segments:
            window.blit(segment.texture, camera.translate(segment.rect.x, segment.rect.y))

