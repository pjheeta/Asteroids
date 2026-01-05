from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import pygame
from logger import log_state
from player import Player

def main():
    print("Starting Asteroids with pygame version: VERSION!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    clock=pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pawan=Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    dt=0

    while True:
        log_state() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))  # Fill the screen with black
        
        
        pawan.draw(screen)
        pygame.display.flip() 
        dt=clock.tick(60)/1000
        
        #print(f"dt is {dt}")
        

if __name__ == "__main__":
    main()

