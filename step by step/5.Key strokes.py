import pygame


pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Meribo Games")
pygame.display.set_icon(pygame.image.load("paw.png"))

enemyImg = pygame.image.load("bone.png")
enemyX = 200
enemyY = 50

playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480
playerXchange = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

running = True
while running:

    screen.fill((0, 0, 0))
    enemyY += 0.01

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXchange = -0.1
            if event.key == pygame.K_RIGHT:
                playerXchange = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXchange = 0


    playerX += playerXchange
    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()