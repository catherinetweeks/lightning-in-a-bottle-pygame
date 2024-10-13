import pygame
import random
from constants import FPS, screen, background, firefly_count, width, height
from sprites import ForegroundGrass, Firefly

# pygame setup
pygame.init()
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("lightning in a bottle")

#Game states
start = "start"
game = "game"
end = "end"

# initialize entities
grass = ForegroundGrass()

fireflies = pygame.sprite.Group()
for _ in range(firefly_count):
    new_firefly = Firefly(random.randint(0, width), random.randint(0, height))
    fireflies.add(new_firefly)


#Main loop
game_state = start
while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #If user presses X button
            running = False

    #starting game
        if game_state == start:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:  # Press Enter to start
                game_state = game
        elif game_state == end: 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:  # Press Enter to restart
                game_state = start

    #Background
    if game_state == start:
        continue
    elif game_state == game:
        screen.blit(background, (0,0))

        # RENDER YOUR GAME HERE
        #Grass foreground animation
        fireflies.update()
        grass.update()

    elif game_state == end:
        continue

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(FPS)  # limits FPS to 60

pygame.quit()