import pygame

import core.settings as settings
from core.events import events
from core.controls import controls
from core.camera import camera

from game.player import Player
from game.level import level
from game.positioning import positioning

pygame.init()


screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
background_image = pygame.image.load("assets/images/background.png")


player_image = pygame.image.load("assets/images/alien.svg")
player_image = pygame.transform.scale(player_image, (40, 60))

platforms = [
        pygame.Rect(200, 330, 200, 20),
        pygame.Rect(800, 280, 200, 20),
        pygame.Rect(1200, 180, 200, 20)
        ]
 
left_border = pygame.Rect(0, -10, 5, 500)
right_border = pygame.Rect(2500, -10, 2, 500)
        

clock = pygame.time.Clock()
running = True


# ------------ main loop ------------

while running:
    
    running = events()
    
    settings.old_y = settings.pos_y

    camera()
    controls()
    positioning(platforms, right_border, left_border)
    
    screen.blit(background_image, (0, 0))
    
    level(screen, player_image, platforms)
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()        
