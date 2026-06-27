import pygame
import settings
from events import events
from controls import controls
from positioning import positioning
from level import level
from camera import camera

pygame.init()

screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))

player_image = pygame.image.load("alien.svg")
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
    clock.tick(60)
    controls()
    positioning(platforms, right_border, left_border)
    level(screen, player_image, platforms)
    
    pygame.display.update()

pygame.quit()        
