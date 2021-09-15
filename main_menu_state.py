# import the pygame library
import pygame

from pygame_gui.elements import UIButton
from pygame_gui import UI_BUTTON_PRESSED


class MainMenuState:
    def __init__(self, window_surface, ui_manager):
        # initialise the variables that control how the main menu displays
        self.transition_target = None
        self.window_surface = window_surface
        self.ui_manager = ui_manager
        self.title_font = pygame.font.Font(None, 128)

        self.background_surf = None
        self.title_text = None
        self.title_pos_rect = None

        self.start_game_button = None
        self.settings_button = None
        self.quit_button = None
        self.tutorial_button = None
        self.background_image = pygame.image.load("tiles/png/BG/BG - Copy.png")

    def start(self):
        self.transition_target = None

        # draw background and title for main menu
        self.background_surf = pygame.Surface((800, 600))
        self.title_text = self.title_font.render('My Game', True, (0, 0, 0))
        self.title_pos_rect = self.title_text.get_rect()
        self.title_pos_rect.center = (400, 50)

        # draw the buttons on the main menu
        self.start_game_button = UIButton(pygame.Rect((325, 240), (150, 30)),
                                          'Start Game',
                                          self.ui_manager)
        self.settings_button = UIButton(pygame.Rect((325, 280), (150, 30)),
                                        'Settings',
                                        self.ui_manager)
        self.tutorial_button = UIButton(pygame.Rect((325, 320), (150, 30)),
                                        'Tutorial',
                                        self.ui_manager)
        self.quit_button = UIButton(pygame.Rect((325, 360), (150, 30)),
                                    'Quit',
                                    self.ui_manager)

    def stop(self):
        # stops the main menu state
        self.background_surf = None
        self.title_text = None
        self.title_pos_rect = None

        self.start_game_button.kill()
        self.start_game_button = None
        self.settings_button.kill()
        self.settings_button = None
        self.tutorial_button.kill()
        self.tutorial_button = None
        self.quit_button.kill()
        self.quit_button = None

    def handle_events(self, event):
        # handles button click events
        if event.type == pygame.USEREVENT and event.user_type == UI_BUTTON_PRESSED:
            # enters game state
            if event.ui_element == self.start_game_button:
                self.transition_target = 'game'
            # enters settings state
            elif event.ui_element == self.settings_button:
                self.transition_target = 'settings'
            # enters tutorial state
            elif event.ui_element == self.tutorial_button:
                self.transition_target = 'tutorial'
            # quits the game
            elif event.ui_element == self.quit_button:
                self.transition_target = 'quit'

    def update(self, time_delta):
        self.window_surface.blit(self.background_surf, (0, 0))  # clears the window to the background surface
        self.window_surface.blit(self.title_text, self.title_pos_rect)  # positions the title at the top
        self.ui_manager.draw_ui(self.window_surface)  # Draw the UI buttons
        self.background_surf.blit(self.background_image, [0, 0])  # draws the background image
