import pygame
import core.settings as settings



def positioning(platforms, left_border, right_border): 

    block = pygame.Rect(100, 300, 40, 60)
    
    
    # ------ collision and positioning mechanics ------

    settings.on_ground = False
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

    
    
    if player_rect.colliderect(right_border):
        
        settings.pos_x = 0 + (player_rect.width * 2)
        settings.velocity *= -0.25
                
    if player_rect.colliderect(left_border):    
        settings.pos_x = settings.LEVEL_WIDTH - (player_rect.width * 2)
        settings.velocity *= -0.25 

        

           