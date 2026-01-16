import sys
from logger import log_event
import pygame
from constants import *
from player import Player 
from logger import log_state
from asteroids import Asteroid
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameclock = pygame.time.Clock()
    dt = 0

    #sprite groups 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #defining player containers  a
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)  

    from asteroidfield import AsteroidField
    AsteroidField.containers = (updatable)

    new_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    new_asteroid_field = AsteroidField()

    while True:
        dt = gameclock.tick(60)/1000

        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(dt)

        for asteroid in asteroids:
            if new_player.collides_with(asteroid):
                log_event("player hit!")
                print("Game Over!")
                sys.exit()

        for draw_able in drawable:
            draw_able.draw(screen)
        
        pygame.display.flip()

        

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f'Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}')

if __name__ == "__main__":
    main()
