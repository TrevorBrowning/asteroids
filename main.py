import pygame
from constants import *

def main():
    pygame.init()

    # Create the display surface (the screen)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the program

        screen.fill((0, 0, 0))  # Fill the display with black

        pygame.display.flip()  # Refresh the screen to show the changes

if __name__ == "__main__":
    main()