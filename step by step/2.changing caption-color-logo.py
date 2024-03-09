import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

#SETTING CAPTION
pygame.display.set_caption("Space Invaders")

#SETTING LOGO
logo = pygame.image.load("bee.png")
pygame.display.set_icon(logo)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #SETTING COLOR
    #RGB = RED - GREEN - BLUE
    screen.fill((0, 0, 0))
    pygame.display.update()