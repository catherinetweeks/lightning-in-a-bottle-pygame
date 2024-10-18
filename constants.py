import pygame

#Window size
height = 540
width = 960
screen = pygame.display.set_mode((width, height))

#Background
background = pygame.transform.scale(pygame.image.load("images/background.png"), (960, 540))

#Maximum frames per second
FPS = 30

#How many fireflies / flies are on the screen at a time:
firefly_count = 15
