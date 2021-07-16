# import the library python and the files skeleton and game_platform
import pygame
import skeleton
import game_map
import view_port
import game_platform


class GameState:
    def __init__(self, window_surface, clock):
        # initialise the skeleton and the platform
        self.map = game_map.GameMap()
        self.skeleton1 = skeleton.Skeleton()

        self.clock = clock
        self.transition_target = None
        self.view_port = view_port.ViewPort(window_surface)
        self.title_font = pygame.font.Font(None, 64)
        self.instructions_font = pygame.font.Font(None, 32)

        self.background_surf = None
        self.title_text = None
        self.title_pos_rect = None
        self.instructions_text = None
        self.instructions_text_pos_rect = None

        #self.background_IMG = pygame.image.load("tiles/png/BG/BG - Copy.png").convert()

    def start(self):

        self.skeleton1.set_position(110, 200)
        self.skeleton1.gravity.fall()   # applies gravity to skeleton1 by calling the gravity class

        self.transition_target = None
        self.background_surf = pygame.Surface((800, 600))

        #self.title_text = self.title_font.render('The Game', True, (255, 255, 255))
        #self.title_pos_rect = self.title_text.get_rect()
        #self.title_pos_rect.center = (400, 50)

        #self.instructions_text = self.instructions_font.render('Press ESC to return to main menu',
                                                              # True, (255, 255, 255))

        #self.instructions_text_pos_rect = self.instructions_text.get_rect()
        #self.instructions_text_pos_rect.center = (400, 100)

    def stop(self):
        self.background_surf = None
        #self.title_text = None
        #self.title_pos_rect = None
        #self.instructions_text = None
        #self.instructions_text_pos_rect = None

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.transition_target = 'main_menu'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            self.skeleton1.walk_left()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            self.skeleton1.walk_right()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            self.skeleton1.jump()

    def update(self, time_delta):
        # clear the window to the background surface
        self.view_port.blit(self.background_surf, (0, 0))
        # stick the title at the top
        #self.view_port.blit(self.title_text, self.title_pos_rect)
        # stick the instructions below
        #self.view_port.blit(self.instructions_text, self.instructions_text_pos_rect)
        # self.view_port.blit(self.background_IMG, [0, 0])
        self.skeleton1.update(time_delta)
        # applies the method fall to skeleton1 causing it to "fall"
        self.skeleton1.gravity.fall()
        # draws the map
        self.map.draw(self.view_port,self.skeleton1)
        # draws the skeleton1
        self.skeleton1.draw(self.view_port)
        # calls the handle_floor method on the map to check if the skeleton should be falling
        self.map.handle_floor(self.skeleton1)
        self.view_port.centre_view_port(self.skeleton1.x,self.skeleton1.y)


