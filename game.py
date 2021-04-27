import pygame, random,time
from shoot import  Bullet, Bullet_catch
from catch import Stuff, Stuff_catch
comojogar=True
width=800
height=600
black=(0,0,0)
white=(255,255,255)
blue=(0, 0, 255)
print('LOGS INIT')
pygame.init()
pygame.mixer.init()
print('LOG: pygame init')

tirosound = pygame.mixer.Sound('data/tirodestruir.wav')
tirosound.set_volume(0.25)

catchsound = pygame.mixer.Sound('data/tirocaptura.wav')
catchsound.set_volume(0.25)


"""sound=pygame.mixer.music.load('data/musicfundo.mp3')
pygame.mixer.music.set_volume(5)
pygame.mixer.music.play(-1)"""
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('Falling-fi   beta v0.1')
clock=pygame.time.Clock()
def como_jogar_screen(comojogar):
    print("LOG: SCREEN HOW TO PLAY")
    screen.blit(background,(0,0))
    sair = pygame.image.load("data/telacomojogar/sair.png")
    sair_rect = sair.get_rect()
    sair_rect.centerx = 45
    sair_rect.centery = 30
    waiting = True
    while waiting:
        pygame.display.update()
        screen.blit(sair, sair_rect)
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >=10 and pygame.mouse.get_pos()[1] >= 10:
                    if pygame.mouse.get_pos()[0] <= 75 and pygame.mouse.get_pos()[1] <= 48:
                        print('LOG: CLICK IN RETURN')
                        if comojogar:
                            waiting = False
                            game_end_screen()
                        else:
                            waiting = False
                            game_pause()
                if pygame.mouse.get_pos()[0] >= 700 and pygame.mouse.get_pos()[1] >= 10:
                    if pygame.mouse.get_pos()[0] <= 765 and pygame.mouse.get_pos()[1] <= 48:
                        exit()
                        print('LOG: GAME ENDED')
def game_end_screen():
    print("LOG: SCREEN END SCREEN")
    screen.blit(background, (0, 0))
    fonte = pygame.font.SysFont('Comicsansms', 20, False, False)
    txt1 = fonte.render('HIGHSCORE:{}'.format(str(score)), True, (80, 80, 80))
    screen.blit(txt1, (700,10))
    pygame.draw.rect(screen, black, (324, 200, 65, 38))
    pygame.draw.rect(screen, black, (324, 250, 65, 38))
    pygame.draw.rect(screen, black, (324, 300, 65, 38))
    sair = pygame.image.load("data/telafimjogo/sair.png")
    sair_react=sair.get_rect()
    sair_rect.centerx = 45
    sair_rect.centery = 30


    play = pygame.image.load("data/telafimjogo/playnew.png")
    play_react=play.get_rect()
    play_rect.centerx = 45
    play_rect.centery = 30

    ask = pygame.image.load("data/telafimjogo/ask1.png")
    ask_react=ask.get_rect()

    ask_rect.centerx = 45
    ask_rect.centery = 30
    pygame.display.flip()
    waiting=True
    while waiting:
        screen.blit(play,play_react)
        screen.blit(sair, sair_react)
        screen.blit(ask, ask_react)
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYUP:
                if event.type == pygame.QUIT:
                    pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    waiting=False
                if event.key==pygame.K_TAB:
                    comojogar = True
                    como_jogar_screen(comojogar)
                if event.key==pygame.K_x:
                    print('LOG: GAME ENDED')
                    exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 324 and pygame.mouse.get_pos()[1] >= 200:
                    if pygame.mouse.get_pos()[0] <= 389 and pygame.mouse.get_pos()[1] <= 238:
                        fonte2 = pygame.font.SysFont('Comicsansms', 20, False, False)
                        txt2 = fonte2.render('iniciando novo jogo', True, (80, 80, 80))

                        screen.blit(txt2, (350, 235))

                        pygame.display.update()
                        time.sleep(1)
                        waiting = False
                if pygame.mouse.get_pos()[0] >= 324 and pygame.mouse.get_pos()[1] >= 230:
                    if pygame.mouse.get_pos()[0] <= 389 and pygame.mouse.get_pos()[1] <= 268:
                        comojogar = True
                        como_jogar_screen(comojogar)
                if pygame.mouse.get_pos()[0] >= 324 and pygame.mouse.get_pos()[1] >= 280:
                    if pygame.mouse.get_pos()[0] <= 389 and pygame.mouse.get_pos()[1] <= 418:
                        exit()
                        print('LOG: GAME ENDED')
def about():
    pass


def game_pause():
    player=Player()
    print("LOG: SCREEN PAUSE GAME")
    pause=pygame.image.load("data/jpausado.png")
    soundoff=pygame.image.load("data/telapause/sondoff.png")
    soundoff_rect=soundoff.get_rect()
    soundoff_rect.centerx=(width // 2+40)
    soundoff_rect.centery=350
    soundoon = pygame.image.load("data/telapause/som1.png")
    soundoon_rect=soundoon.get_rect()
    soundoon_rect.centerx=(width // 2-40)
    soundoon_rect.centery=350

    play=pygame.image.load("data/telapause/playnew.png")
    play_rect = play.get_rect()
    play_rect.centerx = (width // 2 - 40)
    play_rect.centery = 250

    ask = pygame.image.load("data/telapause/ask1.png")
    ask_rect=ask.get_rect()
    ask_rect.centerx=(width // 2-40)
    ask_rect.centery=300
    sair = pygame.image.load("data/telapause/sair1.png")
    sair_rect=sair.get_rect()
    sair_rect.centerx=(width // 2-40)
    sair_rect.centery=400
    screen.blit(pause, (0, 0))
    fonte2 = pygame.font.SysFont('Comicsansms', 15, False, False)
    black=(0,0,0)
    pygame.display.flip()
    waiting=True
    music_paused = False
    mostrar = True
    while waiting:
        screen.blit(soundoon, soundoon_rect)
        screen.blit(soundoff, soundoff_rect)
        screen.blit(ask, ask_rect)
        screen.blit(sair,sair_rect)
        screen.blit(play, play_rect)
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0]>=324 and pygame.mouse.get_pos()[1]>=330:
                    if pygame.mouse.get_pos()[0]<= 389 and pygame.mouse.get_pos()[1]<=368:
                        music_paused = not music_paused
                        if music_paused:
                            pygame.mixer.music.set_volume(0)
                            tirosound.set_volume(0)
                            catchsound.set_volume(0)
                            print('LOG: GAME MUTED')
                        else:
                            pygame.mixer.music.set_volume(5)
                            tirosound.set_volume(0.25)
                            catchsound.set_volume(0.25)
                            print('LOG: GAME UNMUTED')
                if pygame.mouse.get_pos()[0] >= 324 and pygame.mouse.get_pos()[1] >= 280:
                    if pygame.mouse.get_pos()[0] <= 389 and pygame.mouse.get_pos()[1] <= 318:
                        comojogar=False
                        como_jogar_screen(comojogar)
                if pygame.mouse.get_pos()[0] >= 324 and pygame.mouse.get_pos()[1] >= 380:
                    if pygame.mouse.get_pos()[0] <= 389 and pygame.mouse.get_pos()[1] <= 418:
                        print('LOG: GAME ENDED')
                        exit()
                if pygame.mouse.get_pos()[0] >= 324 and pygame.mouse.get_pos()[1] >= 230:
                    if pygame.mouse.get_pos()[0] <= 389 and pygame.mouse.get_pos()[1] <= 288:
                        txt2 = fonte2.render('voltando pro jogo', True, (80, 80, 80))
                        screen.blit(txt2, (400, 235))
                        pygame.display.flip()
                        time.sleep(1)
                        waiting = False
                        print('LOG: IN GAME AGAIN')
        pygame.display.update()
def draw_text(surface,text,size,x,y):
    font=pygame.font.SysFont('Comicsansms',size)
    text_surface=font.render(text, True, black)
    text_rect=text_surface.get_rect()
    text_rect.midtop=(x,y)
    surface.blit(text_surface,text_rect)

def game_menu():
    print("LOG: SCREEN MENU")
    screen.blit(background, (0, 0))
    fonte = pygame.font.SysFont('8-BIT WONDER.TTF', 20, False, False)
    txt1 = fonte.render('APERTE ENTER PRA DAR PLAY', True, (80, 80, 80))
    screen.blit(txt1, (700, 10))
    waiting = True
    while waiting:
        pygame.display.update()
        clock.tick(60)
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                exit()
             if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    waiting=False
                    iniciarjogo()
                if event.key == pygame.K_x:
                    print('LOG: GAME ENDED')
                    exit()

def draw_life_bar(surface,y,x,percentage):
    bar_lenght=10
    bar_height=100
    fill=(percentage*bar_height)/100
    border=pygame.Rect(y,x,bar_lenght,bar_height)
    fill=pygame.Rect(y,x,fill,bar_height)
    pygame.draw.rect(surface,blue, fill)
    pygame.draw.rect(surface, white, border,2)

class Player(pygame.sprite.Sprite):
    def __init__(self):
         super().__init__()
         self.image=pygame.image.load('data/Fabricio.png').convert()
         self.image.set_colorkey(black)
         self.image=pygame.transform.scale(self.image,(120,150))
         self.rect=self.image.get_rect()
         self.size1=self.image.get_size()
         print('size:',self.size1)
         self.rect.centerx=width//2
         self.rect.bottom=height+4
         self.speed_x=0
         self.life=100
    def update(self):
        self.speed_x=0
        keystate=pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speed_x=-5
        if keystate[pygame.K_d]:
            self.speed_x=5
        self.rect.x+=self.speed_x
        if self.rect.right >width:
            self.rect.right=width
        if self.rect.left<0:
            self.rect.left=0
    def shoot(self):
        bullet=Bullet(self.rect.centerx,self.rect.top)
        all_sprite.add(bullet)
        bullets.add(bullet)
    def catch(self):
        bullet_catch=Bullet_catch(self.rect.centerx,self.rect.top)
        all_sprite.add(bullet_catch)
        bullets_catch.add(bullet_catch)
background=pygame.image.load('data/cenario1.jpg').convert()
print('LOG: BACKGROUND ADD')

all_sprite = pygame.sprite.Group()
stuffcatch_list = pygame.sprite.Group()
stuff_list = pygame.sprite.Group()
bullets = pygame.sprite.Group()
bullets_catch = pygame.sprite.Group()
player = Player()
all_sprite.add(player)
print('LOG: PLAYER ADD')
for i in range(8):
    stuff = Stuff()
    all_sprite.add(stuff)
    stuff_list.add(stuff)
    print('LOG: STUFF ADD FIRST')
for i in range(4):
    stuffcatch = Stuff_catch()
    all_sprite.add(stuffcatch)
    stuffcatch_list.add(stuffcatch)
    print('LOG: STUFF CATCH ADD FIRST')


def criar_stuff():
    stuff = Stuff()
    all_sprite.add(stuff)
    stuff_list.add(stuff)
    print('LOG: CREATE NEW STUFF')

def criar_stuff_catch():
    stuffcatch = Stuff_catch()
    all_sprite.add(stuffcatch)
    stuffcatch_list.add(stuffcatch)
    print('LOG: CREATE NEW STUFF CATCH')

all_sprite = pygame.sprite.Group()
stuffcatch_list = pygame.sprite.Group()
stuff_list = pygame.sprite.Group()
bullets = pygame.sprite.Group()
bullets_catch = pygame.sprite.Group()
player = Player()
all_sprite.add(player)
print('LOG: PLAYER ADD')
for i in range(8):
    stuff = Stuff()
    all_sprite.add(stuff)
    stuff_list.add(stuff)
    #stuff_list.
    print('LOG: STUFF ADD FIRST')
for i in range(4):
    stuffcatch = Stuff_catch()
    all_sprite.add(stuffcatch)
    stuffcatch_list.add(stuffcatch)
    print('LOG: STUFF CATCH ADD FIRST')

score = 0
run = True
game_end = False

while run:
    clock.tick(70)

    if game_end:
        game_end = False
        game_end_screen()
        all_sprite = pygame.sprite.Group()
        stuffcatch_list = pygame.sprite.Group()
        stuff_list = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        bullets_catch = pygame.sprite.Group()
        player = Player()
        all_sprite.add(player)
        print('LOG: PLAYER ADD (NEWGAME)')
        for i in range(8):
            stuff = Stuff()
            all_sprite.add(stuff)
            stuff_list.add(stuff)
            print('LOG: STUFF ADD (NEWGAME)')
        for i in range(4):
            stuffcatch = Stuff_catch()
            all_sprite.add(stuffcatch)
            stuffcatch_list.add(stuffcatch)
            print('LOG: STUFF CATCH (NEWGAME)')
        score=0
        print('LOG: (NEWGAME)')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                player.shoot()
                tirosound.play()
                print('LOG: PLAYER PRESSED KEY SHOOT STUFF')
            if event.key == pygame.K_ESCAPE:
                game_pause()
            if event.key == pygame.K_e:
                player.catch()
                catchsound.play()
                print('LOG: PLAYER PRESSED KEY CATCH STUFF')
        elif event.type == pygame.MOUSEBUTTONDOWN:
            player.shoot()
            print('LOG: PLAYER PRESSED KEY SHOOT STUFF')

    #colisao stuff e shoot
    hits = pygame.sprite.groupcollide(stuff_list, bullets, True, True, pygame.sprite.collide_mask)
    hits2 = pygame.sprite.groupcollide(stuffcatch_list, bullets, True, True, pygame.sprite.collide_mask)
    for hit2 in hits2:
        player.life -= 10
        score-=2
        if player.life <= 0:
            game_end = True
        criar_stuff_catch()
        print('LOG: PLAYER LOST LIFE -10')
    for hit in hits:
        criar_stuff()
    # colisao stuff e catch
    catch = pygame.sprite.groupcollide(stuffcatch_list, bullets_catch, True, True, pygame.sprite.collide_mask)
    catch2 = pygame.sprite.groupcollide(stuff_list, bullets_catch, True, True, pygame.sprite.collide_mask)
    if catch or catch2:
        for catchs in catch:
            score += 5
            player.life+=5
            if player.life>=100:
                player.life=100
            criar_stuff_catch()
        print('LOG: PLAYER CATCH STUFFCATCH, HIS SCORE:{}'.format(score))
        print('LOG: PLAYER CATCH STUFFCATCH AND HAS RECEIVED +5 OF LIFE')
        for catchs2 in catch2:
            criar_stuff()
            score-=1
            player.life-=1
            print('LOG: PLAYER CATCH STUFF,  HAS LOST -1 OF LIFE AND LOST -1 OF SCORE ')

    hits = pygame.sprite.spritecollide(player, stuff_list, True, pygame.sprite.collide_mask)
    hits2 = pygame.sprite.spritecollide(player, stuffcatch_list, True, pygame.sprite.collide_mask)
    for hit2 in hits2:
        criar_stuff_catch()
    for i in hits:
        player.life -= 25
        criar_stuff()
        print('LOG: PLAYER LOST LIFE -25')
        if player.life <= 0:
            game_end = True
            print('LOG: PLAYER DEATH')
            print('LOG: END GAME')

    screen.blit(background, [0, 0])
    all_sprite.update()
    all_sprite.draw(screen)

    draw_text(screen, 'SCORE:{}'.format(str(score)), 25, 670, 2)
    draw_text(screen, '{}'.format(player.life), 25, 130, 2)
    draw_life_bar(screen, 10, 10, player.life)
    pygame.display.flip()
pygame.quit()