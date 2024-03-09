import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Meribo Games")
pygame.display.set_icon(pygame.image.load("paw.png"))

playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480
playerXchange = 0
playerYchange = 0


def player(x, y):
    screen.blit(playerImg, (x, y))



running = True
while running:

    screen.fill((0, 0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXchange = -0.1
            if event.key == pygame.K_RIGHT:
                playerXchange = 0.1
            if event.key == pygame.K_UP:
                playerYchange = -0.1
            if event.key == pygame.K_DOWN:
                playerYchange = 0.1

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

    player(playerX, playerY)

    pygame.display.update()