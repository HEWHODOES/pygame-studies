import settings

def camera():
    settings.camera_x = settings.pos_x - settings.WIDTH // 2

    if settings.camera_x < 0:
        settings.camera_x = 0

    if settings.camera_x > settings.LEVEL_WIDTH - settings.WIDTH:
        settings.camera_x = settings.LEVEL_WIDTH - settings.WIDTH