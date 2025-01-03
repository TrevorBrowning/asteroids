import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()

    # Create the display surface (the screen)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    asteroid_field = AsteroidField()


    # Initialize player in center of screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    
    clock = pygame.time.Clock()
    dt = 0



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the program
            
        
            
        updatable.update(dt)   

        

        screen.fill((0, 0, 0))  
        drawable.draw(screen)

        pygame.display.flip() 
        dt = clock.tick(60) / 1000
        
        

if __name__ == "__main__":
    main()