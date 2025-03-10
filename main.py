# Pygame game template

import pygame
import sys
import config # Import the config module
import random
import draw # Import the drawing module

def init_game ():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config

    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events ():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def main():
    screen = init_game()
    clock = pygame.time.Clock() # Initialize the clock here
    running = True

    while running:
        running = handle_events()
        screen.fill(config.WHITE) # Use color from config
        
        draw.draw_text(screen, [30,40], "You lose!", 30, bold=True)
        draw.draw_text(screen, [50,70], "You win!", 50, italic=True)
        draw.draw_text(screen, [70,70], "You are annoying!", 10)
        draw.draw_text(screen, [90,40], "Video Game Text", 50)
        intensity = 2
        for i in range(1):
            draw.draw_text(screen, [40 + random.randrange(-1,1) * intensity, 200 + random.randrange(-1,1) * intensity], "OH NO!", 50, bold=True, italic=True)
        pygame.display.flip()

        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS) # Use the clock to control the frame rate

    pygame.quit()

    sys.exit()

if __name__ == "__main__":
    main()