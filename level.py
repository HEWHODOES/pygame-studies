import pygame
import settings
import camera


def level(screen, player_image, platforms):

    #screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))

    block = pygame.Rect(int(settings.pos_x), int(settings.pos_y), 40, 60)

    #platforms = [
        #pygame.Rect(200, 330, 200, 20),
        #pygame.Rect(800, 280, 200, 20),
        #pygame.Rect(1200, 180, 200, 20)
    #]
    #player_image = pygame.image.load("alien.svg")
    #player_image = pygame.transform.scale(player_image, (40, 60))

    screen.fill((0, 0, 0))

    pygame.draw.line(
        screen, (100, 200, 100),
        (0 - settings.camera_x, 400),
        (settings.LEVEL_WIDTH - settings.camera_x, 400), 8)

    shadow_color = (50, 50, 50)
    shadow_y = 400 - 3
    shadow_width = block.width -8
    shadow_height = 6

    shadow_rect = pygame.Rect(
        block.x - settings.camera_x + 4,
        shadow_y,
        shadow_width,
        shadow_height
    ) 
            
    pygame.draw.rect(screen, shadow_color, shadow_rect)

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