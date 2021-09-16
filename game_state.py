# import the library python and the files skeleton and game_platform
import pygame
import player
import game_map
import view_port
import lives
import spritesheet
import game_over

class GameState:
    def __init__(self, window_surface, clock, settings):
        # initialise the skeleton and the platform
        self.map = game_map.GameMap()
        self.window_surface = window_surface
        self.clock = clock
        self.transition_target = None
        self.view_port = view_port.ViewPort(window_surface)

        self.background_surf = None

        self.settings = settings
        self.player1 = player.Player(self.settings['selected_sprite'])

        self.lives_sprite = spritesheet.SpriteSheet("spritesheets/green_cartoon_ptero.png")

        self.numLives = 3
        self.title_font = pygame.font.Font(None, 128)
        self.title_pos_rect = None

        self.is_paused = False

    def start(self):
        self.is_paused = False
        self.player1 = player.Player(self.settings['selected_sprite'])

        self.player1.set_position(110, 300)
        # self.enemy1.set_position(180,300)
        self.player1.gravity.fall()  # applies gravity to player by calling the gravity class
        # self.enemy1.walk_right()
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

    def update(self, time_delta):
        if not self.is_paused:
            self.map.update(time_delta, self.view_port)
            self.player1.update(time_delta)
            # applies the method fall to skeleton1 causing it to fall
            self.player1.gravity.fall()
            # calls the handle_floor method on the map to check if the skeleton should be falling
            self.map.handle_floor(self.player1)
            self.view_port.centre_view_port(self.player1.x, self.player1.y)
            # draws the map
            self.map.draw(self.view_port)
            # detect if the player is colliding with any enemies
            if self.map.detect_enemy_collision(self.player1):
                # take away a life
                self.player1.numLives = self.player1.numLives - 1
                self.player1.on_death()

            lives.draw_lives(self.player1.numLives, self.window_surface, self.lives_sprite)   # draw the icons for lives
            # draws the player
            self.player1.draw(self.view_port)
            if self.player1.numLives == 0:
               self.game_over()
