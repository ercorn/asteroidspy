# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for member in updatable:
            member.update(dt)
        
        screen.fill((0, 0, 0))
        
        for member in drawable:
            member.draw(screen)
        
        pygame.display.flip()
        #limit the framerate to 60 fps
        dt = clock.tick(60) / 1000 #pause loop for 1/60th of a second and assign the elapsed time since last call and convert from sec to ms


if __name__ == "__main__":
    main()
