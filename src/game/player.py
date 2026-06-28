import pygame
import math
import core.settings as settings

class Player:
    def __init__(self, x=None, y=None, width=40, height=60 ):
        
        if x is None:
            x = settings.pos_x
        if y is None:
            y = settings.pos_y    

        self.rect = pygame.Rect(x, y, width, height)

# ------ movement and positioning values ------

        self.pos_x = x
        self.pos_y = y
        self.velocity = settings.velocity
        self.vertical = settings.vertical
        self.on_ground = settings.on_ground

# ------ attacking variables ------

        self.attacking = False
        self.attack_frame = 0
        self.ATTACK_DURATION = 13
        self.ATTACK_COOLDOWN = 28
        self.attack_cooldown_timer = 0
        self.sword_angle = 0
        self.attack_direction = 0

        self.attack_radius = 68
        self.sword_length = 57

# ------ syncing variables back to settings to avoid errors ------

    def sync_to_settings(self):

        settings.pos_x = self.pos_x
        settings.pos_y = self.pos_y
        settings.velocity = self.velocity
        settings.vertical = self.vertical
        settings.on_ground = self.on_ground