import pygame
import core.settings as settings

def controls():

    # ------ general movement mechanics ------
    

        keys = pygame.key.get_pressed() 
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            settings.velocity += settings.acceleration 
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            settings.velocity -= settings.acceleration          

        if settings.velocity > settings.current_max_speed:
            settings.velocity = settings.current_max_speed

        if settings.velocity < -settings.current_max_speed:
            settings.velocity = -settings.current_max_speed    

        settings.pos_x += settings.velocity
        settings.velocity *= settings.friction

    # ------ 'jump cut' to enable variable jump height ------

        if settings.vertical < 0:
            if not (keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]):
                settings.vertical += settings.gravity + settings.jump_cut_multiplier
            else:
                settings.vertical += settings.gravity

        else:
            settings.vertical += settings.gravity            

        settings.pos_y += settings.vertical

        