import pygame
from constants import FPS, screen, background
from sprites import ForegroundGrass

# pygame setup
pygame.init()
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("lightning in a bottle")

# initialize entities
grass = ForegroundGrass()


while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #If user presses X button
            running = False

    #Background
    screen.blit(background, (0,0))

    # RENDER YOUR GAME HERE
    #Grass foreground animation
    grass.update()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(FPS)  # limits FPS to 60

pygame.quit()