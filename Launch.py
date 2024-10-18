import pygame
import random
from constants import FPS, screen, background, firefly_count, width, height
from sprites import ForegroundGrass, Firefly, grass_frames, MouseJar

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

#Screen text
firefly_yellow = (255, 255, 0)
white = (255, 255, 255)
pixel_font = pygame.font.Font("fonts/PixelifySans.ttf", 32)
smaller_pixel_font = pygame.font.Font("fonts/PixelifySans.ttf", 20)
#Beginning overlay text
press_any_key = pixel_font.render(f"Press any key to start!", False, white)
heading_rect = press_any_key.get_rect(center=(width/2, (height/2)-100))
caption_text = smaller_pixel_font.render(f"Click on a firefly to catch it. When the sun rises, the game ends.", False, white)
caption_rect = caption_text.get_rect(center=(width/2, (height/2)))

# initialize entities
grass = ForegroundGrass()

fireflies = pygame.sprite.Group()
for _ in range(firefly_count):
    new_firefly = Firefly(random.randint(0, width), random.randint(0, height))
    fireflies.add(new_firefly)

jar = MouseJar(0, 0)

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


    #Background
    if game_state == start:
        screen.blit(background, (0,0))
        screen.blit(grass_frames[0], (0,0))
        screen.blit(beginning_overlay, (0,0))
        screen.blit(press_any_key, heading_rect)
        screen.blit(caption_text, caption_rect)


    elif game_state == game:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
            mouse_pos = pygame.mouse.get_pos()
            clicked_firefly = None
            for firefly in fireflies:
                if firefly.rect.collidepoint(mouse_pos):
                    clicked_firefly = firefly
                    break  # We only want to catch one firefly per click

            if clicked_firefly:
                fireflies.remove(clicked_firefly)  # Remove the clicked firefly
                fireflies_caught += 1
                # Optionally add a new firefly
                new_firefly = Firefly(random.randint(0, width), random.randint(0, height))
                fireflies.add(new_firefly)


        screen.blit(background, (0,0))

        #Update sprites
        counter = pixel_font.render(f"{fireflies_caught}", False, firefly_yellow)
        fireflies.update()
        grass.update()
        jar.update()
        screen.blit(counter, (50, 50))
    
    elif game_state == paused:
        screen.blit(background, 0,0)
        screen.blit(beginning_overlay, (0,0))

    elif game_state == end:
        continue

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(FPS)  # limits FPS to 60

pygame.quit()