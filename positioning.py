import pygame
import settings



def positioning(platforms):

    block = pygame.Rect(100, 300, 40, 60)
    
    settings.on_ground = False
    # ------ collision and positioning mechanics ------
    player_rect = pygame.Rect(int(settings.pos_x), int(settings.pos_y), block.width, block.height)

    if settings.pos_y >= settings.ground_y:

        settings.pos_y = settings.ground_y
        settings.on_ground = True 
        settings.vertical = 0
    

    for plat in platforms:

        old_bottom = settings.old_y + block.height

        if player_rect.colliderect(plat) and settings.vertical >= 0:

            if old_bottom <= (plat.top + 1):

                settings.on_ground = True
                settings.pos_y = plat.top - (block.height - 1)
                settings.vertical = 0

                break
           