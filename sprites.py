import pygame
import random
from constants import screen, height, width

#Load images
grass_frames = [
    pygame.transform.scale(pygame.image.load("images/grass loop/grass1.png"), (960, 540)),
    pygame.transform.scale(pygame.image.load("images/grass loop/grass2.png"), (960, 540)),
    pygame.transform.scale(pygame.image.load("images/grass loop/grass3.png"), (960, 540)),
    pygame.transform.scale(pygame.image.load("images/grass loop/grass3.png"), (960, 540)),
    pygame.transform.scale(pygame.image.load("images/grass loop/grass2.png"), (960, 540)),
    pygame.transform.scale(pygame.image.load("images/grass loop/grass1.png"), (960, 540))
    ]
firefly_frames = [
    pygame.transform.scale(pygame.image.load("images/firefly loop/firefly1.png"), (24, 24)).convert_alpha(),
    pygame.transform.scale(pygame.image.load("images/firefly loop/firefly2.png"), (24, 24)).convert_alpha(),
    pygame.transform.scale(pygame.image.load("images/firefly loop/firefly3.png"), (24, 24)).convert_alpha(),
    pygame.transform.scale(pygame.image.load("images/firefly loop/firefly4.png"), (24, 24)).convert_alpha(),
    pygame.transform.scale(pygame.image.load("images/firefly loop/firefly3.png"), (24, 24)).convert_alpha(),
    pygame.transform.scale(pygame.image.load("images/firefly loop/firefly2.png"), (24, 24)).convert_alpha(),
    pygame.transform.scale(pygame.image.load("images/firefly loop/firefly1.png"), (24, 24)).convert_alpha(),
]

empty_jar_image = pygame.transform.scale(pygame.image.load("images/empty_jar.png"), (64, 64)).convert_alpha()


#Waving grass for the foreground
class ForegroundGrass(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.frame_index = 0
        self.animation_speed = 9  # Adjust for faster/slower animation
        self.frame_timer = 0
        self.image = grass_frames[self.frame_index]

    def update(self):
        self.frame_timer += 1
        if self.frame_timer >= self.animation_speed:
            self.frame_index = (self.frame_index + 1) % len(grass_frames)  # Loop through frames
            self.frame_timer = 0
        screen.blit(grass_frames[self.frame_index], (0,0))


class Firefly(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.frame_index = random.randint(0, 4)
        self.animation_speed = random.randint(3, 10)
        self.frame_timer = 0

        # Using mid-size frame for the get rect function
        self.frames = firefly_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()  # Get rect once
        self.rect.topleft = (x, y)

        # Random movement speeds
        self.speed_x = random.uniform(-2, 2)  # Random speed in x direction
        self.speed_y = random.uniform(-2, 2)  # Random speed in y direction

    def update(self):
        # Firefly animation
        self.frame_timer += 1
        if self.frame_timer >= self.animation_speed:
            self.frame_index = (self.frame_index + 1) % len(firefly_frames)
            self.frame_timer = 0
        self.image = self.frames[self.frame_index]

        # Moving across the screen
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Boundary checks
        if self.rect.right < 0:
            self.rect.left = width
        if self.rect.left > width:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = height
        if self.rect.top > height:
            self.rect.bottom = 0

        # Draw the firefly
        screen.blit(self.image, self.rect)

        

class MouseJar(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()  # Initialize the parent class (Sprite)
        self.image = empty_jar_image  # Load or assign the jar image
        self.rect = self.image.get_rect(topleft=(x, y))  # Create a rectangle for positioning

    def update(self):
        # Get the current mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # Update the jar's position so that the top-left corner of the jar aligns with the mouse
        self.rect.topleft = (mouse_x, mouse_y)
        # Blit the jar image at the updated position
        screen.blit(self.image, self.rect)
