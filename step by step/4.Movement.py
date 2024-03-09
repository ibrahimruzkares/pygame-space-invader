import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Meribo Games")
pygame.display.set_icon(pygame.image.load("paw.png"))


playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480

def player(x, y):                               #burada yaptığımız atamalar sayesinde
    screen.blit(playerImg, (x, y))

running = True
while running:

    screen.fill((0, 0, 0))
    playerY -= 0.02                             #movement mechanic kazandı
    playerX -= 0.01

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player(playerX, playerY)

    pygame.display.update()