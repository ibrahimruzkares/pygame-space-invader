import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("background.png")
pygame.display.set_caption("Meribo Games")
pygame.display.set_icon(pygame.image.load("paw.png"))

playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480
playerXchange = 0
playerYchange = 0

enemyImg = pygame.image.load("alien.png")
enemyX = random.randint(0,800)
enemyY = random.randint(20,150)
enemyXchange = 0.5
enemyYchange = 40

bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletXchange = 0
bulletYchange = 10
bulletState = "ready"

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire(x, y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(background,(0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXchange = -2
            if event.key == pygame.K_RIGHT:
                playerXchange = 2
            if event.key == pygame.K_UP:
                playerYchange = -2
            if event.key == pygame.K_DOWN:
                playerYchange = 2
            if event.key == pygame.K_SPACE:
                fire(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXchange = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerYchange = 0



    playerX += playerXchange
    playerY += playerYchange

    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736
    if playerY <= 0:
        playerY = 0
    if playerY >= 536:
        playerY = 536


    enemyX += enemyXchange


    if enemyX <= 0:
        enemyXchange = 0.5
        enemyY += enemyYchange
    if enemyX >= 736:
        enemyXchange = -0.5
        enemyY += enemyYchange

    if bulletState is "fire":
        fire(playerX, bulletY)
        bulletY -= bulletYchange

    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()