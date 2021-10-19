# import the library python and the files skeleton and game_platform
import pygame
import player
import game_map
import view_port
import lives
import spritesheet


class GameState:
    def __init__(self, window_surface, clock, settings, ui_manager):
        # initialise the sprite and the platform
        self.level1 = game_map.GameMap()
        self.level2 = game_map.GameMap()
        self.level3 = game_map.GameMap()
        self.level4 = game_map.GameMap()
        self.level5 = game_map.GameMap()
        self.list_of_levels = [self.level1, self.level2, self.level3, self.level4, self.level5]
        self.level_finished = False
        self.current_level = 0
        self.ui_manager = ui_manager

        self.window_surface = window_surface
        self.clock = clock
        self.transition_target = None
        self.view_port = view_port.ViewPort(window_surface)

        self.background_surf = None

        self.settings = settings
        self.player1 = player.Player(self.settings['selected_sprite'])

        self.lives_sprite = spritesheet.SpriteSheet("spritesheets/icons.png")

        self.level_font = self.ui_manager.get_theme().get_font(['button'])
        self.level_pos_rect = None

        self.is_paused = False

        self.num_jumps = 3

    def start(self):
        self.player1 = player.Player(self.settings['selected_sprite'])
        self.is_paused = False
        self.player1.set_position(110, 300)
        self.player1.gravity.fall()  # applies gravity to player by calling the gravity class
        self.transition_target = None
        self.background_surf = pygame.Surface((800, 600))
        self.player1.num_lives = 3
        self.player1.num_coins = 0

    def stop(self):
        self.background_surf = None

    def game_over(self):
        self.is_paused = True
        self.window_surface.fill((0, 0, 0))
        self.title_text = self.level_font.render('Game Over', True, (255, 255, 255))
        self.title_pos_rect = self.title_text.get_rect()
        self.title_pos_rect.center = (400, 50)
        self.window_surface.blit(self.title_text, self.title_pos_rect)

    def handle_events(self, event):
        # transition to the main menu
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.transition_target = 'main_menu'
            # move the player in the right direction depending on the key pressed
            if event.key == pygame.K_LEFT:
                self.player1.walk_left()
            if event.key == pygame.K_RIGHT:
                self.player1.walk_right()
            if event.key == pygame.K_UP:
                if self.player1.on_ground:
                    self.num_jumps = 1000
                if self.num_jumps != 0:
                    # if the level has been completed, increase the current_level variable and reset the player position
                    self.player1.jump()
                    self.num_jumps -= 1
                    print(self.player1.y)
                self.player1.on_ground = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.player1.stop_walking()

    def current_map(self):
        return self.list_of_levels[self.current_level]

    def update(self, time_delta):
        self.level_text = self.level_font.render('Level ' + str(self.current_level + 1), True, (0, 0, 0))
        self.level_pos_rect = self.level_text.get_rect()
        self.level_pos_rect.center = (400, 50)

        if not self.is_paused:
            self.current_map().update(time_delta, self.view_port)
            self.player1.update(time_delta)
            # applies the method fall to skeleton1 causing it to fall
            self.player1.gravity.fall()
            # calls the handle_floor method on the map to check if the skeleton should be falling
            self.current_map().handle_floor(self.player1, True)
            self.view_port.centre_view_port(self.player1.x, self.player1.y)
            # draws the map
            self.current_map().draw(self.view_port)
            # detect if the player is colliding with any enemies
            if self.current_map().detect_enemy_collision(self.player1):
                # take away a life
                self.player1.num_lives = self.player1.num_lives - 1
                #   call on death method
                self.player1.on_death()

            # checks if the player is colliding with any coins
            self.current_map().detect_coin_collision(self.player1)

            lives.draw_lives(self.player1.num_lives, self.window_surface, self.lives_sprite)  # draw the icons for lives
            # draws the player
            self.player1.draw(self.view_port)
            self.level_finished = self.current_map().end_level(self.player1)
            if self.level_finished:
                self.current_level += 1
                self.player1.set_position(110, 300)

            if self.player1.num_lives == 0:
                self.game_over()
            else:
                self.window_surface.blit(self.level_text, self.level_pos_rect)
