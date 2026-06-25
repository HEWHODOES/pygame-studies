import pygame

pygame.init()
player_image = pygame.image.load("alien.svg")
player_image = pygame.transform.scale(player_image, (40, 60))


# ------ window and level creation ------

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

block = pygame.Rect(100, 300, 40, 60)

platforms = [
    pygame.Rect(200, 330, 200, 20),
    pygame.Rect(800, 280, 180, 20),
    pygame.Rect(1200, 180, 200, 20)
]

LEVEL_WIDTH = 2500

# ------ several variables needed for mechanics ------

clock = pygame.time.Clock()
running = True

#positioning
pos_x = 100
ground_y = 348
pos_y = ground_y

camera_x = 0

#general movement
velocity = 0
vertical = 0
gravity = 0.92
jump_height = 21
jump_cut_multiplier = 2.2
acceleration = 0.85
max_speed = 5
friction = 0.82

#dash mechanics
can_dash = True
last_dash = 0
dash_time_window = 250
dash_cooldown = 1000
last_right_press = 0
last_left_press = 0
dash_multiplier = 7

current_max_speed = max_speed



# ------------ main loop ------------

while running:

    old_y = pos_y 

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        

# ------ controller. actions after buttonpress ------

        if event.type == pygame.KEYDOWN:

# ------ jump mechanics ------

            if event.key in (pygame.K_UP, pygame.K_w, pygame.K_SPACE):
                current_time = pygame.time.get_ticks()
                if on_ground or current_time - last_dash <= 250:
                    vertical = -jump_height

# ------ dash mechanics ------

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

# ------ general movement mechanics ------

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

# ------ 'jump cut' to enable variable jump height ------

    if vertical < 0:
        if not (keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]):
            vertical += gravity + jump_cut_multiplier
        else:
            vertical += gravity

    else:
        vertical += gravity            

    pos_y += vertical

    on_ground = False

# ------ collision and positioning mechanics ------

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

# ------- CAMERA -------

    camera_x = pos_x - WIDTH // 2

    if camera_x < 0:
        camera_x = 0

    if camera_x > LEVEL_WIDTH - WIDTH:
        camera_x = LEVEL_WIDTH - WIDTH    


#-------------
    clock.tick(60)

# ------ graphics ------

    screen.fill((0, 0, 0))

    pygame.draw.line(
        screen, (100, 200, 100),
        (0 - camera_x, 400),
        (LEVEL_WIDTH - camera_x, 400), 8)

    shadow_color = (50, 50, 50)
    shadow_y = 400 - 3
    shadow_width = block.width -8
    shadow_height = 6

    shadow_rect = pygame.Rect(
        block.x - camera_x + 4,
        shadow_y,
        shadow_width,
        shadow_height
    ) 
        
    pygame.draw.rect(screen, shadow_color, shadow_rect)

    for plat in platforms:
        
        screen_rect = pygame.Rect(
            plat.x - camera_x,
            plat.y,
            plat.width,
            plat.height
        )

        pygame.draw.rect(screen, (80, 140, 255), screen_rect)

    screen.blit(
        player_image, 
        (block.x -camera_x, block.y))

    pygame.display.update()

pygame.quit()