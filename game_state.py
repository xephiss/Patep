# import the library python and the files skeleton and game_platform
import pygame
import skeleton
import game_platform


class GameState:
    def __init__(self, window_surface, clock):
        # initialise the skeleton and the platform
        self.platform1 = game_platform.Platform(100, 320, 256, 64)
        self.skeleton1 = skeleton.Skeleton()

        self.clock = clock
        self.transition_target = None
        self.window_surface = window_surface

        self.title_font = pygame.font.Font(None, 64)
        self.instructions_font = pygame.font.Font(None, 32)

        self.background_surf = None
        self.title_text = None
        self.title_pos_rect = None
        self.instructions_text = None
        self.instructions_text_pos_rect = None

        self.background_IMG = pygame.image.load("tiles/png/BG/BG - Copy.png").convert()

    def start(self):

        self.skeleton1.set_position(110, 200)
        #self.skeleton1.walk_right()
        # applies gravity to skeleton1 by calling the gravity class
        self.skeleton1.gravity.fall()

        self.transition_target = None
        self.background_surf = pygame.Surface((800, 600))

        self.title_text = self.title_font.render('The Game', True, (255, 255, 255))
        self.title_pos_rect = self.title_text.get_rect()
        self.title_pos_rect.center = (400, 50)

        self.instructions_text = self.instructions_font.render('Press ESC to return to main menu',
                                                               True, (255, 255, 255))

        self.instructions_text_pos_rect = self.instructions_text.get_rect()
        self.instructions_text_pos_rect.center = (400, 100)

    def stop(self):
        self.background_surf = None
        self.title_text = None
        self.title_pos_rect = None
        self.instructions_text = None
        self.instructions_text_pos_rect = None

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.transition_target = 'main_menu'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            self.skeleton1.walk_left()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            self.skeleton1.walk_right()

    def update(self, time_delta):
        # clear the window to the background surface
        self.window_surface.blit(self.background_surf, (0, 0))
        # stick the title at the top
        self.window_surface.blit(self.title_text, self.title_pos_rect)
        # stick the instructions below
        self.window_surface.blit(self.instructions_text, self.instructions_text_pos_rect)
        self.window_surface.blit(self.background_IMG, [0, 0])
        self.skeleton1.update(time_delta)
        # applies the method fall to skeleton1 causing it to "fall"
        self.skeleton1.gravity.fall()
        # draws the skeleton1
        self.skeleton1.draw(self.window_surface)
        # draws the platform1
        self.platform1.draw(self.window_surface)
        # calls the handle_floor method to check whether the sprite should me falling on the skeleton1 by passing in
        # skeleton1 and platform1
        self.handle_floor(self.skeleton1, self.platform1)

    def handle_floor(self, sprite_that_falls, platform):
        # check wether the sprite_that_falls that is passed into the method should be falling or not.
        # set co-ordinate for bottom of sprite
        bottom_of_sprite = sprite_that_falls.y + sprite_that_falls.height
        top_of_platform = platform.y + 2
        if platform.x <= sprite_that_falls.x <= platform.x + platform.width:
            # checks if sprite is colliding with the platform
            if top_of_platform > bottom_of_sprite > top_of_platform - 3:
                # applies the method stop_falling to the sprite_that_falls
                sprite_that_falls.gravity.stop_falling()
