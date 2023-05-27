import pygame
from ptica import Ptica
from stub import Stub
import random
  
pygame.init()

pygame.display.set_caption('Flappy Bird')

screenHeight = 800
screenWidth = 600

screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()
running = True

a = 240
b = 100
r = 35
gr = 0.6
vsp = 1.2

boja1 = (0,153,53)
crna = (0, 0, 0)
 

nebo = (179, 230, 255)
cvrle = Ptica(150, screenHeight / 2, vsp, r, 0)
skaci = 1
skokf = 0
cvrle.gravity = 0 
vsp = 0
gameover = False
rand = random.randint(a, screenHeight - a)
rand2 = random.randint(a, screenHeight - a)
stubic = [Stub(screenWidth + b / 2, rand, a, b, boja1), Stub(screenWidth + b / 2 + screenWidth / 2 + b / 2, rand2, a, b, boja1)]
rez = 0
sqrt2 = 1.42

def ispis(sc):
    font = pygame.font.Font('freesansbold.ttf', 64)
    text = font.render(str(sc), True, crna)
    textRect = text.get_rect(center=(screenWidth // 2, 50))
    screen.blit(text, textRect)

def gameOver():
    global vsp
    cvrle.vsp = 0
    cvrle.gravity = 0
    vsp = 0

    font = pygame.font.Font('freesansbold.ttf', 90)
    text = font.render("GAME OVER", True, crna)
    textRect = text.get_rect(center=(screenWidth / 2, screenHeight / 2))
    screen.blit(text, textRect)

def sudar(tica, cev):
    sluppod = False
    slupvrh = False
    res = False
    r = tica.radius * sqrt2 / 2
    c = pygame.Vector2(tica.x, tica.y)
    vrh = pygame.Rect(cev.x - cev.b / 2, 0, cev.b, cev.a1)
    pod = pygame.Rect(cev.x - cev.b / 2, cev.y + cev.a / 2, cev.b, cev.a2)
    if c.x + r >= vrh.left and c.y - r <= vrh.bottom:
        res = True
    if c.x + r >= pod.left and c.y + r >= pod.top:
        res = True
    return res

def crtanje():
    screen.fill(nebo)
    cvrle.draw(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  

    if gameover == False:
        screen.fill(nebo)
        dt = clock.tick(60)
        keys=pygame.key.get_pressed()
            
        if keys[pygame.K_SPACE] and cvrle.gravity == 0:
            cvrle.gravity = gr
            vsp = 5

        if keys[pygame.K_SPACE] and skaci == 1:
            skaci = 0
            skokf = 10
        elif keys[pygame.K_SPACE] == False:
            skaci = 1

        if (skokf > 0):
            cvrle.update(dt)
            skokf -= 1

        for i in range(0,2): #stubic loop
            if stubic[i].nestao():
                rand = random.randint(a, screenHeight - a)
                stubic[i] = Stub(screenWidth + stubic[i].b / 2, rand, a, b, boja1)
            if cvrle.prosao(stubic[i]):
                rez += 1
                ispis(rez) 
                print (rez)
                stubic[i].gotov = True
            if stubic[i].gotov == False:
                if sudar(cvrle, stubic[i]):
                    gameover = True 
            stubic[i].draw(screen)
            stubic[i].pomeri(vsp)            

        cvrle.draw(screen)
        cvrle.gravitacija(dt) 
        ispis(rez)   

        if cvrle.pao():
            gameover = True               

    else:
        gameOver()

    pygame.display.flip()