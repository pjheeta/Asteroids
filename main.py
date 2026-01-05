from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import pygame
from logger import log_state


def main():
    print("Starting Asteroids with pygame version: VERSION!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    while True:
    # Your code here
        log_state() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
        return
        screen.fill((0, 0, 0))  # Fill the screen with black
        pygame.display.flip() 

if __name__ == "__main__":
    main()
