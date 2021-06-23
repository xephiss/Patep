import pygame
import skeleton
import game_platform


class GameState:
    def __init__(self, window_surface, clock):
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

    def start(self):
        self.skeleton1.set_position(110, 200)
        # skeleton1.walkLeft()
        self.skeleton1.walk_right()

        self.transition_target = None
        self.background_surf = pygame.Surface((800, 600))
        self.background_surf.fill((0, 0, 0))

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

    def update(self, time_delta):
        # clear the window to the background surface
        self.window_surface.blit(self.background_surf, (0, 0))
        # stick the title at the top
        self.window_surface.blit(self.title_text, self.title_pos_rect)
        # stick the instructions below
        self.window_surface.blit(self.instructions_text, self.instructions_text_pos_rect)
        self.skeleton1.update(time_delta)
        self.skeleton1.draw(self.window_surface)
        self.platform1.draw(self.window_surface)
        self.skeleton1.gravity.fall()
        self.handle_floor(self.skeleton1, self.platform1)

    def handle_floor(self, sprite_that_falls, platform):
        bottom_of_sprite = sprite_that_falls.y + sprite_that_falls.height
        top_of_platform = platform.y + 2
        if platform.x <= sprite_that_falls.x <= platform.x + platform.width:
            if top_of_platform > bottom_of_sprite > top_of_platform - 1:
                sprite_that_falls.gravity.stop_falling()
