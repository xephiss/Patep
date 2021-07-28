import pygame

from pygame_gui.elements import UIButton
from pygame_gui import UI_BUTTON_PRESSED

class TutorialState:
    def __init__(self,window_surface,ui_manager):
        self.transition_target = None
        self.window_surface = window_surface
        self.ui_manager = ui_manager
        self.title_font = pygame.font.Font(None, 64)

        self.background_surf = None
        self.title_text = None
        self.title_pos_rect = None

        self.back_button = None

        self.background_image = pygame.image.load("tiles/png/BG/BG - Copy.png")
    def start(self):
        # draws the background and the title for the settings menu
        self.transition_target = None
        self.background_surf = pygame.Surface((800, 600))
        self.background_surf.fill((0, 0, 0))
        self.title_text = self.title_font.render('Tutorial', True, (0, 0, 0))
        self.title_pos_rect = self.title_text.get_rect()
        self.title_pos_rect.center = (400, 50)
        # creates buttons
        self.back_button = UIButton(pygame.Rect((550, 550), (200, 30)),
                                    'Back to menu', self.ui_manager)

    def stop(self):
        self.background_surf = None
        self.title_text = None
        self.title_pos_rect = None
        self.back_button.kill()
        self.back_button = None

    def handle_events(self,event):
        if event.type == pygame.USEREVENT and event.user_type == UI_BUTTON_PRESSED:
            # exit to main menu if the back button is pressed
            if event.ui_element == self.back_button:
                self.transition_target = 'main_menu'

    def update(self, time_delta):
        # clear the window to the background surface
        self.window_surface.blit(self.background_surf, (0, 0))
        # stick the title at the top
        self.window_surface.blit(self.title_text, self.title_pos_rect)

        self.ui_manager.draw_ui(self.window_surface)  # Draw the UI Bits
        self.background_surf.blit(self.background_image, [0, 0])