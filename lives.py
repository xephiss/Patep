import spritesheet


def draw_lives(num_lives, window_surface, life_sprite):
    x = 0
    y = 0
    width = 108
    # get the image at the coordinates from the spritesheet

    sprite = life_sprite.image_at([0, 0, 108, 64])
    # draw an icon at the correct position for each life
    for i in range(0, num_lives):
        window_surface.blit(sprite, [x, y])
        # increase the x position by the width of the icon
        x += width
