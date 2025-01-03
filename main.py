import pygame
from constants import *
from player import *

def main():
    pygame.init()

    # Create the display surface (the screen)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player_start_pos = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    player = Player(player_start_pos)

    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                return  # Exit the program

        screen.fill((0, 0, 0))  
        player.draw(screen)

        pygame.display.flip() 
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()