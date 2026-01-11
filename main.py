from constants import *
import pygame
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids with pygame version:", pygame.__version__)
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    clock=pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (asteroids,updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.contain = (updatable)

    pawan=Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    dt=0

  


    while True:
        log_state() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt=clock.tick(60)/1000
        #print(f"dt is {dt}")

        screen.fill((0, 0, 0))  # Fill the screen with black     
        
        updatable.update(dt)

        for item in drawable:
            item.draw(screen)
           
        pygame.display.flip()      
        

if __name__ == "__main__":
    main()

