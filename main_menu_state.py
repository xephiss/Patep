import pygame

from pygame_gui.elements import UIButton
from pygame_gui import UI_BUTTON_PRESSED


class MainMenuState:
    def __init__(self, window_surface, ui_manager):
        self.transition_target = None
        self.window_surface = window_surface
        self.ui_manager = ui_manager
        self.title_font = pygame.font.Font(None, 64)

        self.background_surf = None
        self.title_text = None
        self.title_pos_rect = None

        self.start_game_button = None
        self.settings_button = None
        self.quit_button = None

    def start(self):
        self.transition_target = None
        self.background_surf = pygame.Surface((800, 600))
        self.background_surf.fill((0, 0, 0))
        self.title_text = self.title_font.render('Main Menu', True, (255, 255, 255))
        self.title_pos_rect = self.title_text.get_rect()
        self.title_pos_rect.center = (400, 50)

        self.start_game_button = UIButton(pygame.Rect((325, 240), (150, 30)),
                                          'Start Game',
                                          self.ui_manager)
        self.settings_button = UIButton(pygame.Rect((325, 280), (150, 30)),
                                        'Settings',
                                        self.ui_manager)
        self.quit_button = UIButton(pygame.Rect((325, 320), (150, 30)),
                                    'Quit',
                                    self.ui_manager)

    def stop(self):
        self.background_surf = None
        self.title_text = None
        self.title_pos_rect = None

        self.start_game_button.kill()
        self.start_game_button = None
        self.settings_button.kill()
        self.settings_button = None
        self.quit_button.kill()
        self.quit_button = None

    def handle_events(self, event):
        if event.type == pygame.USEREVENT and event.user_type == UI_BUTTON_PRESSED:
            if event.ui_element == self.start_game_button:
                self.transition_target = 'game'
            elif event.ui_element == self.settings_button:
                self.transition_target = 'settings'
            elif event.ui_element == self.quit_button:
                self.transition_target = 'quit'

    def update(self, time_delta):
        # clear the window to the background surface
        self.window_surface.blit(self.background_surf, (0, 0))
        # stick the title at the top
        self.window_surface.blit(self.title_text, self.title_pos_rect)

        self.ui_manager.draw_ui(self.window_surface)  # Draw the UI Bits
