import pygame
from constants import screen

#Load images
grass_frames = [
    pygame.transform.scale(pygame.image.load("images/grass loop/grass1.png"), (960, 540)),
    pygame.transform.scale(pygame.image.load("images/grass loop/grass2.png"), (960, 540)),
    pygame.transform.scale(pygame.image.load("images/grass loop/grass3.png"), (960, 540)),
    pygame.transform.scale(pygame.image.load("images/grass loop/grass3.png"), (960, 540)),
    pygame.transform.scale(pygame.image.load("images/grass loop/grass2.png"), (960, 540)),
    pygame.transform.scale(pygame.image.load("images/grass loop/grass1.png"), (960, 540))
    ]

#Waving grass in the foreground
class ForegroundGrass(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = grass_frames
        self.frame_index = 0
        self.animation_speed = 1  # Adjust for faster/slower animation
        self.frame_timer = 0

    def update(self):
        self.frame_timer += 1
        if self.frame_timer >= self.animation_speed:
            self.frame_index = (self.frame_index + 1) % len(grass_frames)  # Loop through frames
            self.frame_timer = 0
        screen.blit(grass_frames[self.frame_index], (0,0))