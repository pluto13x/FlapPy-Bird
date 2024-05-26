import pygame
from funkcije import *
from ptica import Ptica
from stub import Stub
from pygame import mixer
import random
  
pygame.init()
mixer.init()

#region muzika
mixer.music.load("assets/ost.ogg")
mixer.music.set_volume(0.7)
mixer.music.play(-1)
#endregion

#region zvucni efekti!!
ping = pygame.mixer.Sound('assets/ping.ogg')
ping.set_volume(0.5)
boom = pygame.mixer.Sound('assets/boom.ogg')
boom.set_volume(1)
whoosh = pygame.mixer.Sound('assets/whoosh.ogg')
whoosh.set_volume(0.5)
#endregion

#region window
pygame.display.set_caption('Flappy Bird')
pygame_icon = pygame.image.load('assets/cvrle.png')
pygame.display.set_icon(pygame_icon)
#endregion

#region ne diraj
screenHeight = 800
screenWidth = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()
running = True
gameover = False
#endregion

#region ostali atributi
crna = (0, 0, 0)
nebo = (179, 230, 255)
rez = 0
#endregion
 
#region pticji atributi
r = 35
gr = 0.6
jump = 1.2
cvrle = Ptica(150, screenHeight / 2, jump, r, 0)
skokf = 0
cvrle.gravity = 0 
skaci = 1
ubrzanje = 0
#endregion

#region stub atributi
a = 180
b = 100 
hsp = 0
boja1 = (0,153,53)
boja2 = (0, 61, 21)
rand = random.randint(a, screenHeight - a)
rand2 = random.randint(a, screenHeight - a)
stubic = [Stub(screenWidth + b / 2, rand, a, b, boja1, boja2), Stub(screenWidth + b / 2 + screenWidth / 2 + b / 2, rand2, a, b, boja1, boja2)]
#endregion

#region score setup
file = open("assets/high.txt","r+")
high = (int)(file.read())
file.close()
#endregion

while running:
    #region izadji iz igrice
    for event in pygame.event.get():
        if event.type == pygame.QUIT:           
            file = open("assets/high.txt","w")
            file.write((str)(high))
            file.close()
            running = False  
    #endregion

    if gameover == False: 
        print(cvrle.gravity)      
        #region setup
        screen.fill(nebo)
        oblak()
        dt = clock.tick(60)
        keys=pygame.key.get_pressed()
        #endregion

        #region ptica movement    
        if keys[pygame.K_SPACE] and cvrle.gravity == 0: #kad tek krece igrica           
            hsp = 5
            ubrzanje = 0.01

        if keys[pygame.K_SPACE] and skaci == 1: #kad skoci
            cvrle.gravity = gr
            skaci = 0
            skokf = 10 #koliko frameova da ide na gore
            pygame.mixer.Sound.play(whoosh)
        elif keys[pygame.K_SPACE] == False: #kad pusti space
            skaci = 1

        if (skokf > 0): #skok animacija
            cvrle.update(dt)
            skokf -= 1
        else:
            cvrle.gravity += ubrzanje
        #endregion

        #region stubic
        for i in range(0,2): 
            if stubic[i].nestao(): #pravi novi stubic
                rand = random.randint(a, screenHeight - a)
                stubic[i] = Stub(screenWidth + stubic[i].b / 2, rand, a, b, boja1, boja2)
            if cvrle.prosao(stubic[i]): #broji score
                rez += 1
                stubic[i].gotov = True
                pygame.mixer.Sound.play(ping)
            if stubic[i].gotov == False: #collision
                if sudar(cvrle, stubic[i]):
                    gameover = True
                    pygame.mixer.Sound.play(boom)
                    if rez > high:
                        high = rez
            stubic[i].draw(screen)
            stubic[i].pomeri(hsp)    
        #endregion       

        cvrle.draw(screen)
        cvrle.gravitacija(dt) 
        ispis(rez, crna, screen, screenWidth)
        highscoreIspis(high, crna, screen)   

        if cvrle.pao():
            gameover = True
            pygame.mixer.Sound.play(boom) 
            if rez > high:
                high = rez              

    #region gameover
    else:
        keys=pygame.key.get_pressed()
        gameOver(screen, screenWidth, screenHeight)
        if keys[pygame.K_r]:
            reset()
            gameover = False
    #endregion
    pygame.display.flip()
