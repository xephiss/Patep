
import player

def spriteSelection(sprite):
    if sprite is not None:
        if sprite == "skeleton":
            player.Player.set_sprite_skeleton()
        if sprite == "green_dino":
            player.Player.set_sprite_dino()
    else:
        player.Player.set_sprite_dino()