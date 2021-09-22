# import the library python and the files skeleton and game_platform
import pygame
import player
import game_map
import view_port
import lives
import spritesheet


class GameState:
    def __init__(self, window_surface, clock, settings):
        # initialise the skeleton and the platform
        self.level1 = game_map.GameMap()
        self.level2 = game_map.GameMap()
        self.level3 = game_map.GameMap()
        self.list_of_levels = [self.level1, self.level2, self.level3]
        self.level_finished = False
        self.current_level = 0

        self.window_surface = window_surface
        self.clock = clock
        self.transition_target = None
        self.view_port = view_port.ViewPort(window_surface)

        self.background_surf = None

        self.settings = settings
        self.player1 = player.Player(self.settings['selected_sprite'])

        self.lives_sprite = spritesheet.SpriteSheet("spritesheets/icons.png")

        self.numLives = 3
        self.title_font = pygame.font.Font(None, 128)
        self.title_pos_rect = None

        self.is_paused = False

    def start(self):
        self.is_paused = False
        self.player1 = player.Player(self.settings['selected_sprite'])

        self.player1.set_position(110, 300)
        self.player1.gravity.fall()  # applies gravity to player by calling the gravity class
        self.transition_target = None
        self.background_surf = pygame.Surface((800, 600))
        self.player1.numLives = 3

    def stop(self):
        self.background_surf = None

    def game_over(self):
        self.is_paused = True
        self.window_surface.fill((0, 0, 0))
        self.title_text = self.title_font.render('Game Over', True, (0, 0, 0))
        self.title_pos_rect = self.title_text.get_rect()
        self.title_pos_rect.center = (400, 50)
        self.window_surface.blit(self.title_text, self.title_pos_rect)

    def handle_events(self, event):
        # transition to the main menu
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.transition_target = 'main_menu'
        # move the player in the right direction depending on the key pressed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            self.player1.walk_left()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            self.player1.walk_right()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            self.player1.jump()
        # if the level has been completed, increase the current_level variable and reset the player position

    def update(self, time_delta):
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
                self.player1.numLives = self.player1.numLives - 1
                #   call on death method
                self.player1.on_death()

            lives.draw_lives(self.player1.numLives, self.window_surface, self.lives_sprite)  # draw the icons for lives
            # draws the player
            self.player1.draw(self.view_port)
            self.level_finished = self.current_map().end_level(self.player1)
            if self.level_finished:
                self.current_level += 1
                self.player1.set_position(110, 300)

            if self.player1.numLives == 0:
                self.game_over()

    def current_map(self):
        return self.list_of_levels[self.current_level]
