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
game_start_time = 0
time_limit = 45000

#Screen text
firefly_yellow = (255, 255, 0)
white = (255, 255, 255)
pixel_font = pygame.font.Font("fonts/PixelifySans.ttf", 32)
smaller_pixel_font = pygame.font.Font("fonts/PixelifySans.ttf", 24)
#Beginning overlay text
press_any_key = pixel_font.render(f"Press any key to start!", False, white)
heading_rect = press_any_key.get_rect(center=(width/2, (height/2)-100))
caption_text = smaller_pixel_font.render(f"Click on a firefly to catch it. Catch as many as you can.", False, white)
caption_rect = caption_text.get_rect(center=(width/2, (height/2)))
#Game pause text
restart_directions = pixel_font.render(f"Press any key to unpause.", None, white)

# initialize entities
grass = ForegroundGrass()

fireflies = pygame.sprite.Group()
for _ in range(firefly_count):
    new_firefly = Firefly(random.randint(0, width), random.randint(0, height))
    fireflies.add(new_firefly)

jar = MouseJar(0, 0)

# Main loop
game_state = start
while running:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle start screen events
        if game_state == start:
            if event.type == pygame.KEYDOWN:
                game_state = game

        # Handle game events
        elif game_state == game:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game_state = paused

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
                mouse_pos = pygame.mouse.get_pos()
                clicked_firefly = None
                for firefly in fireflies:
                    if firefly.rect.collidepoint(mouse_pos):
                        clicked_firefly = firefly
                        break  # We only want to catch one firefly per click

                if clicked_firefly:
                    fireflies.remove(clicked_firefly)
                    fireflies_caught += 1
                    # Optionally add a new firefly
                    new_firefly = Firefly(random.randint(0, width), random.randint(0, height))
                    fireflies.add(new_firefly)

        # Handle paused events
        elif game_state == paused:
            if event.type == pygame.KEYDOWN:  # Any key unpauses
                game_state = game

        # Handle end screen events
        elif game_state == end:
            if event.type == pygame.KEYDOWN:
                game_state = start

       # Timer Logic
    if game_state == game:
        current_time = pygame.time.get_ticks()  # Get the current time
        elapsed_time = current_time - game_start_time  # Calculate elapsed time

        # Check if the time limit (60 seconds) has been reached
        if elapsed_time >= time_limit:
            game_state = end  # Switch to the "end" game state after 60 seconds
   
   
    # Screen Updates
    if game_state == start:
        screen.blit(background, (0, 0))
        screen.blit(grass_frames[0], (0, 0))
        screen.blit(beginning_overlay, (0, 0))
        screen.blit(press_any_key, heading_rect)
        screen.blit(caption_text, caption_rect)

    elif game_state == game:
        screen.blit(background, (0, 0))

        # Update sprites
        counter = pixel_font.render(f"{fireflies_caught}", False, firefly_yellow)
        fireflies.update()
        grass.update()
        jar.update()
        screen.blit(counter, (50, 50))

    elif game_state == paused:
        # Make sure the background is drawn before the overlay
        screen.blit(background, (0, 0))  # Redraw the background when paused
        screen.blit(grass_frames[0], (0, 0))
        fireflies.draw(screen)
        screen.blit(counter, (50, 50))
        screen.blit(beginning_overlay, (0, 0))  # Transparent overlay
        screen.blit(restart_directions, heading_rect)

    elif game_state == end:
        screen.blit(background, (0, 0))  # Redraw the background when paused
        screen.blit(grass_frames[0], (0, 0))
        fireflies.draw(screen)
        screen.blit(counter, (50, 50))
        screen.blit(beginning_overlay, (0, 0))  # Transparent overlay

    # Flip the display to show updates
    pygame.display.flip()

    clock.tick(FPS)  # Control frame rate

pygame.quit()