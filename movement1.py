import pygame


pygame.init()


WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
block = pygame.Rect(100, 300, 50, 100)
platforms = [
    pygame.Rect(200, 380, 200, 20),
    pygame.Rect(500, 280, 180, 20),
    pygame.Rect(100, 180, 200, 20)
]


clock = pygame.time.Clock()

running = True

pos_x = 100
ground_y = 300
pos_y = ground_y
velocity = 0
vertical = 0
gravity = 0.92
jump_height = 21
jump_cut_multiplier = 2.2
acceleration = 0.85
max_speed = 5
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

        old_y = pos_y

        if event.type == pygame.KEYDOWN:

            if event.key in (pygame.K_UP, pygame.K_w, pygame.K_SPACE):
                current_time = pygame.time.get_ticks()
                if on_ground or current_time - last_dash <= 250:
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

    if vertical < 0:
        if not (keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]):
            vertical += gravity + jump_cut_multiplier
        else:
            vertical += gravity

    else:
        vertical += gravity            

    pos_y += vertical

    on_ground = False
    player_rect = pygame.Rect(int(pos_x), int(pos_y), block.width, block.height)

    if pos_y >= ground_y:
        pos_y = ground_y
        on_ground = True
        vertical = 0

    for plat in platforms:
        old_bottom = old_y + block.height

        if player_rect.colliderect(plat) and vertical >= 0:

            if old_bottom <= (plat.top + 1):

                on_ground = True
                pos_y = plat.top - (block.height - 1)
                vertical = 0
                
                break    

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

    for plat in platforms:
        pygame.draw.rect(screen, (80, 140, 255), plat)

    pygame.draw.rect(screen, (255, 255, 255), block)
    
    pygame.display.update()

    
