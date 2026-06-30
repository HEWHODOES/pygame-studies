import pygame
import core.settings as settings
from core.camera import camera


def level(screen, player_image, platforms):

    block = pygame.Rect(int(settings.pos_x), int(settings.pos_y), 40, 60)


# LEVEL GROUND 
    # pygame.draw.line(
    #     screen, (100, 200, 100),
    #     (0 - settings.camera_x, 400),
    #     (settings.LEVEL_WIDTH - settings.camera_x, 400), 8)
    
# LEVEL GROUND REMASTER

    floor_line = pygame.draw.line(screen, (0, 0, 0), (0, 400), (900, 400), 5)
    


# PLAYER SHADOW (evtl. noch in player.py verschieben)           Fixen: 2ter Schatten muss weg
    shadow_color = (0, 0, 0)
    shadow_y = block.y + block.height + 4
    shadow_width = block.width -4
    shadow_height = 15

    shadow_surface = pygame.Surface((shadow_width, shadow_height), pygame.SRCALPHA)
    shadow_surface.fill((0, 0, 0, 99))  # letzter Wert = Alpha
    screen.blit(shadow_surface, (block.x + 4, shadow_y))
    
    shadow_rect = pygame.Rect(
        block.x - settings.camera_x + 4,
        shadow_y,
        shadow_width,
        shadow_height
    ) 
            
    # pygame.draw.rect(screen, shadow_color, shadow_rect)   # ?

    for plat in platforms:
            
        screen_rect = pygame.Rect(
            plat.x - settings.camera_x,
            plat.y,
            plat.width,
            plat.height
        )

        pygame.draw.rect(screen, (80, 140, 255), screen_rect)

    screen.blit(
        player_image, 
        (block.x -settings.camera_x, block.y))
    
    
    