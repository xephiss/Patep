# import the library pygame
import pygame
import player

from pygame_gui.elements import UIButton
from pygame_gui import UI_BUTTON_PRESSED


class SettingsState:
    def __init__(self, window_surface, ui_manager):
        # initalises the variables that control the settings display
        self.transition_target = None
        self.window_surface = window_surface
        self.ui_manager = ui_manager
        self.title_font = pygame.font.Font(None, 64)

        self.background_surf = None
        self.title_text = None
        self.title_pos_rect = None

        self.back_button = None
        self.button1 = None
        self.button2 = None
        self.background_image = pygame.image.load("tiles/png/BG/BG - Copy.png")
        self.green_dino_selection = player.Player.set_sprite_dino()
        self.skeleton_selection = player.Player.set_sprite_skeleton()
        self.sprite = None

    def start(self):
        # draws the background and the title for the settings menu
        self.transition_target = None
        self.background_surf = pygame.Surface((800, 600))
        self.background_surf.fill((0, 0, 0))
        self.title_text = self.title_font.render('Settings', True, (0, 0, 0))
        self.title_pos_rect = self.title_text.get_rect()
        self.title_pos_rect.center = (400, 50)
        # creates buttons
        self.back_button = UIButton(pygame.Rect((550, 550), (200, 30)),
                                    'Back to menu', self.ui_manager)
        #self.button1 = UIButton(pygame.Rect((325, 240), (150, 30)),
                               # 'button1', self.ui_manager)
        #self.button2 = UIButton(pygame.Rect((325, 280), (150, 30)),
                               # 'button2', self.ui_manager)
        self.background_surf.blit(self.green_dino_selection,(325,240))
        self.background_surf.blit(self.skeleton_selection,(325,280))

    def stop(self):
        #stops the settings state
        self.background_surf = None
        self.title_text = None
        self.title_pos_rect = None
        self.back_button.kill()
        self.back_button = None
        #self.button1.kill()
        #self.button1 = None
        #self.button2.kill()
        #self.button2 = None

    def handle_events(self, event):
        if event.type == pygame.USEREVENT and event.user_type == UI_BUTTON_PRESSED:
            # exit to main menu if the back button is pressed
            if event.ui_element == self.back_button:
                self.transition_target = 'main_menu'
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            if 375 >= position >=325 and 260 <= position >= 280:
                self.sprite = "green_dino"
            if 375 >= position >= 325 and 220 <= position >= 240:
                self.sprite = "skeleton"

    def update(self, time_delta):
        # clear the window to the background surface
        self.window_surface.blit(self.background_surf, (0, 0))
        # stick the title at the top
        self.window_surface.blit(self.title_text, self.title_pos_rect)

        self.ui_manager.draw_ui(self.window_surface)  # Draw the UI Bits
        self.background_surf.blit(self.background_image, [0, 0])
