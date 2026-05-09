import pygame
import sys
from logger import log_state
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from logger import log_event
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable =  pygame.sprite.Group()
    #----
    Shot.containers = (shots,updatable,drawable)
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
       for space_rock in asteroids:
           for shot in shots:
               if(shot.collides_with(space_rock)):
                   log_event("asteroid_shot")
                   shot.kill()
                   space_rock.kill()
           if(player.collides_with(space_rock)):
               log_event("player_hit")
               print("Game over!")
               sys.exit()
       for drawing in drawable:
           drawing.draw(screen)
       pygame.display.flip()
       dt = clock.tick(60)/1000 
       

if __name__ == "__main__":
    main()
