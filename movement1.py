import pygame


pygame.init()


WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
block = pygame.Rect(100, 300, 50, 100)


clock = pygame.time.Clock()

running = True

pos_x = 100
ground_y = 300
pos_y = ground_y
velocity = 0
vertical = 0
gravity = 0.35
jump_height = 11
acceleration = 0.65
max_speed = 3
friction = 0.82

can_dash = True
last_dash = 0
dash_time_window = 250
dash_cooldown = 1000
last_right_press = 0
last_left_press = 0
dash_multiplier = 7

current_max_speed = max_speed


while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key in (pygame.K_UP, pygame.K_w):
                if pos_y >= ground_y:
                    vertical = -jump_height
                
            if event.key in (pygame.K_RIGHT, pygame.K_d):
                current_time = pygame.time.get_ticks()

                if current_time - last_dash >= dash_cooldown:
                    can_dash = True
                
                if current_time - last_right_press < dash_time_window and can_dash == True:
                    current_max_speed = max_speed * dash_multiplier
                    velocity = max_speed * dash_multiplier  
                    can_dash = False
                    last_dash = current_time
                    
                last_right_press = current_time 

                  

            if event.key in (pygame.K_LEFT, pygame.K_a):
                current_time = pygame.time.get_ticks() 
                
                if current_time - last_dash >= dash_cooldown:
                    can_dash = True

                if current_time - last_left_press < dash_time_window and can_dash == True:
                    current_max_speed = max_speed * dash_multiplier
                    velocity = -max_speed * dash_multiplier
                    can_dash = False
                    last_dash = current_time

                last_left_press = current_time    



    keys = pygame.key.get_pressed() 
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        velocity += acceleration 
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        velocity -= acceleration          

    if velocity > current_max_speed:
        velocity = current_max_speed

    if velocity < -current_max_speed:
        velocity = -current_max_speed    

    pos_x += velocity
    velocity *= friction

    vertical += gravity
    pos_y += vertical

    if pos_y >= ground_y:
        pos_y = ground_y
        vertical = 0

    block.x = int(pos_x)
    block.y = int(pos_y)
    
    clock.tick(60)

    screen.fill((0, 0, 0))

    pygame.draw.line(screen, (100, 200, 100), (0, 400), (WIDTH, 400), 8)

    shadow_color = (50, 50, 50)
    shadow_y = 400 - 3
    shadow_width = block.width -8
    shadow_height = 6

    shadow_rect = pygame.Rect(
        block.x + 4,
        shadow_y,
        shadow_width,
        shadow_height
    ) 
        
    pygame.draw.rect(screen, shadow_color, shadow_rect)
    pygame.draw.rect(screen, (255, 255, 255), block)
    
    pygame.display.update()

    
