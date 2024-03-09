import pygame
from pygame import mixer
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("First Game")
pygame.display.set_icon(pygame.image.load("paw.png"))

mixer.music.load("spacebleep.wav")
mixer.music.play(-1)

font = pygame.font.Font("Sunday Mango.ttf", 32)
score_value = 0
scoreX = 10
scoreY = 10

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x ,y))

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((22,12,123))


    show_score(scoreX, scoreY)

    pygame.display.update()