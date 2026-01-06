import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    gameclock = pygame.time.Clock()
    dt = 0


    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()
        
        gameclock.tick(60)
        dt = gameclock.tick_busy_loop()/1000
        
        

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f'Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}')

if __name__ == "__main__":
    main()
