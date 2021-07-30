# import the library python and the files skeleton and game_platform
import pygame
import player
import game_map
import view_port
import game_platform


class GameState:
    def __init__(self, window_surface, clock, settings):
        # initialise the skeleton and the platform
        self.map = game_map.GameMap()

        self.clock = clock
        self.transition_target = None
        self.view_port = view_port.ViewPort(window_surface)

        self.background_surf = None

        self.settings = settings
        self.player1 = player.Player(self.settings['selected_sprite'])

        #self.background_IMG = pygame.image.load("tiles/png/BG/BG - Copy.png").convert()

    def start(self):
        self.player1 = player.Player(self.settings['selected_sprite'])

        self.player1.set_position(110, 300)
        self.player1.gravity.fall()   # applies gravity to skeleton1 by calling the gravity class

        self.transition_target = None
        self.background_surf = pygame.Surface((800, 600))


    def stop(self):
        self.background_surf = None


    def handle_events(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.transition_target = 'main_menu'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            self.player1.walk_left()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            self.player1.walk_right()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            self.player1.jump()

    def update(self, time_delta):
        # self.view_port.blit(self.background_IMG, [0, 0])
        self.player1.update(time_delta)
        # applies the method fall to skeleton1 causing it to "fall"
        self.player1.gravity.fall()
        # calls the handle_floor method on the map to check if the skeleton should be falling
        self.map.handle_floor(self.player1)
        self.view_port.centre_view_port(self.player1.x, self.player1.y)
        # draws the map
        self.map.draw(self.view_port)
        # draws the skeleton1
        self.player1.draw(self.view_port)
