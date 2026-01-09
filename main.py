import pygame
from constants import *
from player import Player 
from logger import log_state
from asteroids import Asteroid

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    gameclock = pygame.time.Clock()
    dt = 0

    #sprite groups 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    #defining player containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    from asteroidfield import AsteroidField
    AsteroidField.containers = (updatable)

    new_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    new_asteroid_field = AsteroidField()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(dt)
        for draw_able in drawable:
            draw_able.draw(screen)
        
        pygame.display.flip()

        dt = gameclock.tick(60)/1000
        

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f'Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}')

if __name__ == "__main__":
    main()
