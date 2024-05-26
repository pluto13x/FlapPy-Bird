import pygame
sqrt2 = 1.42

def ispis(sc, boja, screen, screenWidth):
    font = pygame.font.Font('assets/Minecraft.ttf', 64)
    text = font.render(str(sc), True, boja)
    textRect = text.get_rect(center=(screenWidth // 2, 50))
    screen.blit(text, textRect)

def highscoreIspis(hi, boja, screen):
    font = pygame.font.Font('assets/Minecraft.ttf', 40)
    text = font.render("HI: ", True, boja)
    textRect = text.get_rect(center=(50, 40))
    screen.blit(text, textRect)
    text = font.render(str(hi), True, boja)
    textRect = text.get_rect(midleft = (80, 40))
    screen.blit(text, textRect)

def gameOver(screen, screenWidth, screenHeight, boja):
    font = pygame.font.Font('assets/Minecraft.ttf', 90)
    text = font.render("GAME OVER", True, boja)
    textRect = text.get_rect(center=(screenWidth / 2, screenHeight / 2 - 25))
    screen.blit(text, textRect)

    font = pygame.font.Font('assets/Minecraft.ttf', 40)
    text = font.render("Press R to play again", True, boja)
    textRect = text.get_rect(center=(screenWidth / 2, screenHeight / 2 + 50))
    screen.blit(text, textRect)

    #cvrle.vsp = 0
    #cvrle.gravity = 0

    return 0, 0

def sudar(tica, cev):
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

def crtanje(cvrle, screen, bojaPozadine):
    screen.fill(bojaPozadine)
    cvrle.draw(screen)

def oblak(screen):
    scale = 4

    image = pygame.image.load('assets/oblak1.png')
    SIZE = (64 * scale, 47 * scale)
    image = pygame.transform.scale(image, SIZE)
    screen.blit(image, (400, 60))

    image = pygame.image.load('assets/oblak2.png')
    SIZE = (32 * scale, 32 * scale)
    image = pygame.transform.scale(image, SIZE)
    screen.blit(image, (100, 100))

    image = pygame.image.load('assets/oblak3.png')
    SIZE = (32 * scale, 32 * scale)
    image = pygame.transform.scale(image, SIZE)
    screen.blit(image, (250, 300))
    
    image = pygame.image.load('assets/oblak4.png')
    SIZE = (64 * scale, 64 * scale)
    image = pygame.transform.scale(image, SIZE)
    screen.blit(image, (300, 500))

    image = pygame.image.load('assets/oblak5.png')
    SIZE = (32 * scale, 32 * scale)
    image = pygame.transform.scale(image, SIZE)
    screen.blit(image, (50, 500))
