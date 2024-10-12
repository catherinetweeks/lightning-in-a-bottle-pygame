import pygame

#Window size
screen = pygame.display.set_mode((960, 540))
#Background
background = pygame.transform.scale(pygame.image.load("images/background.png"), (960, 540))

#Maximum frames per second
FPS = 20