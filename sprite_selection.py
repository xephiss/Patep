import player


class SpriteSelection:
    def select_sprite(self, sprite):
        if sprite is not None:
            if sprite == "skeleton":
                player.Player.set_sprite_skeleton(self)
            if sprite == "green_dino":
                player.Player.set_sprite_dino(self)
        else:
            player.Player.set_sprite_dino(self)
