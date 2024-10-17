import pygame
import random
from constants import FPS, screen, background, firefly_count, width, height
from sprites import ForegroundGrass, Firefly, grass_frames, Jar

# pygame setup
pygame.init()
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("lightning in a bottle")

beginning_overlay = pygame.transform.scale(pygame.image.load('images/overlay.png'), (960, 540))

#Game states
start = "start"
game = "game"
end = "end"
paused = "paused"

#initialize game-specific counters
fireflies_caught = 0

# initialize entities
grass = ForegroundGrass()

fireflies = pygame.sprite.Group()
for _ in range(firefly_count):
    new_firefly = Firefly(random.randint(0, width), random.randint(0, height))
    fireflies.add(new_firefly)

jar = Jar(0, 0)

#Main loop
game_state = start
while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #If user presses X button
            running = False

        #starting game
        if game_state == start:
            if event.type == pygame.KEYDOWN: #press any key to start
                game_state = game
        elif game_state == end: 
            if event.type == pygame.KEYDOWN: # and event.key == pygame.K_RETURN: #enter to restart
                game_state = start

        #game pauses at escape
        if game_state == game and event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game_state = paused
        if game_state == paused and event.type == pygame.KEYDOWN:
            game_state = game
        

        #Game logic here
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Left click
            mouse_pos = pygame.mouse.get_pos()
            # Check for collision with any firefly
            for firefly in fireflies:
                if firefly.rect.collidepoint(mouse_pos):
                    fireflies.remove(firefly)  # Remove the firefly if clicked
                    fireflies_caught += 1
                    new_firefly = Firefly(random.randint(0, width), random.randint(0, height))
                    fireflies.add(new_firefly)


    #Background
    if game_state == start:
        screen.blit(background, (0,0))
        screen.blit(grass_frames[0], (0,0))
        screen.blit(beginning_overlay, (0,0))


    elif game_state == game:
        screen.blit(background, (0,0))

        #Update sprites
        fireflies.update()
        grass.update()
        jar.update()
    
    elif game_state == paused:
        screen.blit(background, 0,0)

    elif game_state == end:
        continue

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(FPS)  # limits FPS to 60

pygame.quit()