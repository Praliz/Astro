import pygame
from logger import log_state
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable =  pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    AsteroidField()
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT /2)
    while(True):
       for event in pygame.event.get():
           if(event.type ==pygame.QUIT):
               return
       log_state()
       screen.fill("black")
       updatable.update(dt)
       for drawing in drawable:
           drawing.draw(screen)
       pygame.display.flip()
       dt = clock.tick(60)/1000 
      

if __name__ == "__main__":
    main()
