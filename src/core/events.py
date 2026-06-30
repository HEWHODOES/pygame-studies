import pygame  
import core.settings as settings


def events():
   
    for event in pygame.event.get():

        
        if event.type == pygame.QUIT:
            return  False
        
        # ------ controller. actions after buttonpress ------

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                mode = 0
            if event.key == pygame.K_LEFT:
                mode = 5
            if event.key == pygame.K_DOWN:
                mode = 1
            if event.key == pygame.K_UP:
                mode = 6
        if event.type == pygame.KEYUP:     # Tasten loslassen
            mode = 0
            
            
    # ------ jump mechanics ------

            if event.key in (pygame.K_UP, pygame.K_w, pygame.K_SPACE):
                current_time = pygame.time.get_ticks()
                if settings.on_ground or current_time - settings.last_dash <= 250:
                    settings.vertical = -settings.jump_height

    # ------ dash mechanics ------

            if event.key in (pygame.K_RIGHT, pygame.K_d):
                current_time = pygame.time.get_ticks()

                if current_time - settings.last_dash >= settings.dash_cooldown:
                    settings.can_dash = True
                    
                if current_time - settings.last_right_press < settings.dash_time_window and settings.can_dash == True:
                    settings.current_max_speed = settings.max_speed * settings.dash_multiplier
                    settings.velocity = settings.max_speed * settings.dash_multiplier  
                    settings.can_dash = False
                    settings.last_dash = current_time
                        
                settings.last_right_press = current_time 

                    

            if event.key in (pygame.K_LEFT, pygame.K_a):
                current_time = pygame.time.get_ticks() 
                    
                if current_time - settings.last_dash >= settings.dash_cooldown:
                    settings.can_dash = True

                if current_time - settings.last_left_press < settings.dash_time_window and settings.can_dash == True:
                    settings.current_max_speed = settings.max_speed * settings.dash_multiplier
                    settings.velocity = -settings.max_speed * settings.dash_multiplier
                    settings.can_dash = False
                    settings.last_dash = current_time

                settings.last_left_press = current_time
        
    return True         