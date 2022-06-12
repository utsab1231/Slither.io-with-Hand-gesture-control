import pygame

from cvzone.HandTrackingModule import HandDetector

from Player import Player
from orb import Orb
import random
from camera import Camera
from obstacle import Obstacle
from fontrenderer import Fontrenderer
import cv2
import mediapipe as mp

START_W = 50
START_H = 50
PLAYER_START_X = 0
PLAYER_START_Y = 0
FPS = 60




class MainGame:
    pygame.init()
    pygame.font.init()

    def __init__(self):
        self.background = (58, 90, 64)
        self.winsize = (800, 500)
        self.window = pygame.display.set_mode(self.winsize)
        self.quit = False
        self.clock = pygame.time.Clock()
        self.arr=["images/img2.png","images/black.png","images/1.png"]
        self.player_body=random.choice(self.arr)
        self.camera = Camera(PLAYER_START_X, PLAYER_START_Y, (START_W, START_H), self.winsize)

        self.player = Player(PLAYER_START_X, PLAYER_START_Y, START_W, START_H,self.player_body)

        self.orbs = []
        self.obstacles = []
        self.fontrenderer = Fontrenderer()
        self.pointindex = ()
        self.color=["images/green.png", "images/orange.png", "images/red.png", "images/yellow.png"]


    def play(self):
        while not self.quit:
            self.update()
            self.render()


    def orbpos(self):



        for i in range(100):
            x = random.randint(-self.winsize[0] * 3, self.winsize[0] * 3)
            y = random.randint(-self.winsize[1] * 3, self.winsize[1] * 3)
            START_R = random.randint(15, 25)
            neworb = Orb(x, y, START_R, random.choice(self.color))
            self.orbs.append(neworb)

        for i in range(70):
            x = random.randint(-self.winsize[0] * 3, self.winsize[0] * 3)
            y = random.randint(-self.winsize[1] * 3, self.winsize[1] * 3)
            newobs = Obstacle(x, y, 40, 40, "images/bomb.png")
            self.obstacles.append(newobs)

        self.play()

    def update(self):
        self.clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.quit = True

        self.player.update(self.winsize)
        # orbs update

        for orb in self.orbs:
            if orb.update(self.player):
                self.orbs.remove(orb)
        for obstacle in self.obstacles:
            if obstacle.update(self.player):
                self.quit=True

        # camera update
        self.camera.update(self.player.rect.x, self.player.rect.y)

    def render(self):
        self.window.fill(self.background)
        self.player.draw(self.window, self.camera)
        for orb in self.orbs:
            orb.draw(self.window, self.camera)
        for obstacle in self.obstacles:
            obstacle.draw(self.window, self.camera)
            self.fontrenderer.renderfont(self.window, self.player.score)

        pygame.display.update()


