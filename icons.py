import spritesheet


class Icons:
    def __init__(self, ui_manager):
        self.lives_sprite = spritesheet.SpriteSheet("spritesheets/icons.png")
        self.y = 10
        self.coin_font = ui_manager.get_theme().get_font(['#level_text'])

    def draw_lives(self, num_lives, window_surface):
        x = 10
        # get the image at the coordinates from the spritesheet
        sprite = self.lives_sprite.image_at([84, 4, 28, 24])
        # draw an icon at the correct position for each life
        for i in range(0, num_lives):
            window_surface.blit(sprite, [x + (i*32), self.y])
            # increase the x position by the width of the icon

    def draw_num_coins(self, num_coins, window_surface):
        coin_text = self.coin_font.render(str(num_coins), True, (0, 0, 0))
        window_surface.blit(coin_text, (200, self.y))

