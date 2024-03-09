import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Meribo Games")
pygame.display.set_icon(pygame.image.load("paw.png"))


playerImage = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480

def player():
    screen.blit(playerImage, (playerX, playerY))                #ekrana bir resim ekleme metodudur blit

running = True
while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()