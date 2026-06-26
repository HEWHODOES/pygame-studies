# ------ settings ------

WIDTH = 800
HEIGHT = 600

LEVEL_WIDTH = 2500

# ------ positioning ------

pos_x = 100
ground_y = 348
pos_y = ground_y
old_y = pos_y
on_ground = False

camera_x = 0

# ------ general movement ------

velocity = 0
vertical = 0
gravity = 0.92
jump_height = 21
jump_cut_multiplier = 2.2
acceleration = 0.85
max_speed = 5
friction = 0.82

# ------ dash mechanics ------

can_dash = True
last_dash = 0
dash_time_window = 250
dash_cooldown = 1000
last_right_press = 0
last_left_press = 0
dash_multiplier = 7

current_max_speed = max_speed