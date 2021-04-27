import pygame
import pygame
import math
import random
width=800
height=600
black=(0,0,0)
white=(255,255,255)
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image=pygame.image.load('data/shot.png')
        self.image.set_colorkey(black)
        self.rect=self.image.get_rect()
        self.rect.y=y
        self.rect.centerx=x+5
        self.speedy=-10

    def update(self):
        self.rect.y+=self.speedy
        if self.rect.bottom<0:
            self.kill()
class Bullet_catch(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image=pygame.image.load('data/catch.png')
        self.image.set_colorkey(black)
        self.rect=self.image.get_rect()
        self.rect.y=y
        self.rect.centerx=x+5
        self.speedy=-10


    def update(self):
        self.rect.y+=self.speedy
        if self.rect.bottom<0:
            self.kill()
