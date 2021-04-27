import pygame,random
width=800
height=600
black=(0,0,0)
white=(255,255,255)

class Stuff_catch(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('data/stuffy.png').convert()
        self.image.set_colorkey(black)
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(width - self.rect.width)
        self.rect.y=random.randrange(-100,-40)
        self.speedy=random.randrange(1,10)
        self.speedx=random.randrange(-5,5)
    def update(self):
        self.rect.y+=self.speedy
        self.rect.x+=self.speedx
        if self.rect.top>height+10 or self.rect.left<-150 or self.rect.right>width+150:
            self.rect.x = random.randrange(width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 10)
            self.speedx = random.randrange(-5, 5)


class Stuff(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('data/stuff.png').convert()
        self.image.set_colorkey(black)
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(width - self.rect.width)
        self.rect.y=random.randrange(-100,-40)
        self.speedy=random.randrange(1,5)
        self.speedx=random.randrange(-2,4)
    def update(self):
        self.rect.y+=self.speedy
        self.rect.x+=self.speedx
        if self.rect.top>height+10 or self.rect.left<-150 or self.rect.right>width+150:
            self.rect.x = random.randrange(width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 10)
            self.speedx = random.randrange(-5, 5)
