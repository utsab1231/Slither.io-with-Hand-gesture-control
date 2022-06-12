import pygame

class Fontrenderer():

    pygame.font.init()

    def __init__(self):
        self.color=(255,0,0)
        self.size=80
        self.font=pygame.font.Font(None,self.size)

    def renderfont(self,window,score):
        pygame.font.init()
        text=self.font.render(f"score:{score}",True,self.color)
        window.blit(text,(0,0))

    # def gameendrender(self,window,text,winsize):
    #     pygame.font.init()
    #     text=self.font.render(text,True,self.color)
    #     window.blit(text,(winsize[0]/2,winsize[1]/2))
