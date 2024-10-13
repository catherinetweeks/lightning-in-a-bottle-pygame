import pygame
import random
from constants import FPS, screen, background, firefly_count, width, height
from sprites import ForegroundGrass, Firefly

# pygame setup
pygame.init()
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("lightning in a bottle")

# initialize entities
grass = ForegroundGrass()

fireflies = pygame.sprite.Group()
for _ in range(firefly_count):
    new_firefly = Firefly(random.randint(0, width), random.randint(0, height))
    fireflies.add(new_firefly)


#Main loop
while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #If user presses X button
            running = False

    #Background
    screen.blit(background, (0,0))

    # RENDER YOUR GAME HERE
    #Grass foreground animation
    fireflies.update()
    grass.update()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(FPS)  # limits FPS to 60

pygame.quit()