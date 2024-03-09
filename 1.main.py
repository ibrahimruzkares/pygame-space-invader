import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("background.png")
pygame.display.set_caption("Meribo Games")
pygame.display.set_icon(pygame.image.load("paw.png"))

mixer.music.load("background.wav")
mixer.music.play(-1)

playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480
playerXchange = 0
playerYchange = 0

enemyImg = []
enemyX = []
enemyY = []
enemyXchange = []
enemyYchange = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("alien.png"))
    enemyX.append(random.randint(50, 735))
    enemyY.append(random.randint(50, 150))
    enemyXchange.append(1)
    enemyYchange.append(40)

bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletXchange = 0
bulletYchange = 5
bulletState = "ready"

score_value = 0
font = pygame.font.Font("Sunday Mango.ttf", 32)
textX = 10
textY = 10

over_font = pygame.font.Font("Sunday Mango.ttf", 64)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER!", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire(x, y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX , 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

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
                if bulletState == "ready":
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    bulletX = playerX
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




    for i in range(num_of_enemies):

        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()



        if enemyX[i] <= 0:
            enemyXchange[i] = 1
            enemyY[i] += enemyYchange[i]
        elif enemyX[i] >= 736:
            enemyXchange[i] = -1
            enemyY[i] += enemyYchange[i]

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()
            bulletY = 480
            bulletState = "ready"
            score_value += 1
            enemyX[i] = random.randint(50, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)
        enemyX[i] += enemyXchange[i]

    if bulletY <= 0:
        bulletY = 480
        bulletState = "ready"


    if bulletState == "fire":
        fire(bulletX, bulletY)
        bulletY -= bulletYchange





    player(playerX, playerY)
    show_score(textX, textY)

    pygame.display.update()