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
# background_image wird aktuell unten nicht aufgerufen



####################################################################
########################## ANIMATION TESTING #######################
####################################################################

pygame.display.set_caption('Wheelpunk Steam')
timer = pygame.time.Clock()


player_x = 200
player_y = 200
frames = ['assets/images/pixilart-frames/pixil-frame-0.png', 'assets/images/pixilart-frames/pixil-frame-1.png', 
          'assets/images/pixilart-frames/pixil-frame-2.png', 'assets/images/pixilart-frames/pixil-frame-3.png', 
          'assets/images/pixilart-frames/pixil-frame-4.png', 'assets/images/pixilart-frames/pixil-frame-5.png', 
          'assets/images/pixilart-frames/pixil-frame-6.png']
active_frame = 1
mode = 0    # 0 = rechts und standart, 1 = rechtsunten, 2 = rechtsklein, 3 = mitte, 
                     # 4 = linksklein, 5 = links, 6 = linksunten
count = 0

def update_player(mod, counter):
    if count >= 60:
        counter = 0
    if mod == 0:
        if counter < 30:
            act = 0
        if counter >= 30 and counter < 60:
            act = 1
    if mod == 1:
        if counter < 30:
            act = 0
        if counter >= 30 and counter < 60:
            act = 1
    if mod == 2:
        if counter < 30:
            act = 5
        if counter >= 30 and counter < 60:
            act = 6
    if mod == 3:
        act = 3        
    if mod == 4:
        act = 4      
    counter += 1  
    return act, counter
    
    
# player_image = pygame.image.load("assets/images/pixilart-frames/pixil-frame-0.png")
player_image = pygame.transform.scale(pygame.image.load(frames[active_frame]), (150, 150))
screen.blit(player_image, (player_x, player_y))

####################################################################


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
    
    ####################################################################
    ########################## ANIMATION TESTING #######################
    ####################################################################

    dt = clock.tick(settings.fps) / 1000     # kommt mir schneller vor
    screen.blit(background_image, (0, 0)) # Hintergrund auf Bildschirm "kopieren/zeichnen"
    # screen.fill(settings.gray)       # screen.fill((128, 128, 128))
    floor = pygame.draw.rect(screen, (0, 128, 40), [0, 400, 800, 300])
    floor_line = pygame.draw.line(screen, (0, 0, 0), (0, 400), (900, 400), 5)
    active_frame, count = update_player(mode, count)
    player_image = pygame.transform.scale(pygame.image.load(frames[active_frame]), (150, 150))
    screen.blit(player_image, (player_x, player_y))

    ####################################################################
    
    
    level(screen, player_image, platforms)
    
    pygame.display.flip()          # habe .update zu .flip geändert, soll schneller und besser bei Spielen sein
    # clock.tick(60)

pygame.quit()        
