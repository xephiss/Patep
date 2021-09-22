def draw_lives(num_lives, window_surface, life_sprite):
    x = 10
    y = 10
    # get the image at the coordinates from the spritesheet

    sprite = life_sprite.image_at([84, 4, 28, 24])
    # draw an icon at the correct position for each life
    for i in range(0, num_lives):
        window_surface.blit(sprite, [x + (i*32), y])
        # increase the x position by the width of the icon
